import json
import os
import pickle
import re
from pathlib import Path

import qtawesome as qta
import qtpy.QtGui as qtg
from qtpy.QtWidgets import QFileDialog, QProgressDialog
from qtpy.QtCore import *

import utilities as utils
from database.translations_widget import TranslationsWidget
from plugin_interface import Plugin
from translation_editor.editor_tab import EditorTab


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:
    finished: No data
    error: tuple (exctype, value, traceback.format_exc() )
    result: object data returned from processing, anything
    progress: int indicating % progress
    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    '''
    Worker thread

    :param editor: Reference to the EditorTab instance
    :param path: Path to the file to be imported
    '''

    def __init__(self, editor, path):
        super(Worker, self).__init__()
        self.editor = editor
        self.path = path
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        '''
        Run the worker thread.
        '''
        try:
            data = self.load_data()
            total_entries = len(data)
            if self.path.endswith(".json"):
                self.import_data(data, total_entries, json_format=True)
            else:
                self.import_data(data, total_entries, json_format=False)

            self.editor.update_string_list()
            self.signals.result.emit('DB_IMPORTED')
        except Exception as e:
            self.signals.error.emit((type(e), e, e.__traceback__))
        finally:
            self.signals.finished.emit()

    def load_data(self):
        '''
        Load data from the specified path.
        '''
        data = {}
        if self.path.endswith(".json"):
            with open(self.path, 'r', encoding='utf-8') as file:
                f = json.load(file)
                for entry in f:
                    data[entry['original']] = entry
        else:
            with open(self.path, 'rb') as file:
                f = pickle.load(file)
                for entry in f:
                    data[entry.original_string] = entry
        return data

    def import_data(self, data, total_entries, json_format):
        '''
        Import data into the editor.
        '''
        i = 0
        
        for tree_item, string in self.editor.items.items():
            if string.status != utils.String.Status.TranslationComplete:
                try:
                    if json_format:
                        if data[string.original_string]['string'] != string.original_string:
                            string.translated_string = data[string.original_string]['string']
                            string.status = utils.String.Status.TranslationIncomplete
                    else:
                        if data[string.original_string]:
                            string.translated_string = data[string.original_string].translated_string
                            string.status = data[string.original_string].status

                    tree_item.setText(4, utils.trim_string(string.translated_string))
                except KeyError:
                    continue
                
            progress = int((i + 1) / total_entries * 100)
            self.signals.progress.emit(progress)
            i = i + 1

class EditorAddon(QObject):
    def __init__(self, editor: EditorTab):
        super(EditorAddon, self).__init__()
        self.editor = editor
        self.threadpool = QThreadPool()
        self.progress_dialog = None  # Initialize progress dialog as None

    def load_from_db(self, path=None):
        self.progress_dialog = QProgressDialog("Loading data...", "Cancel", 0, 100, self.editor)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setAutoClose(True)
        self.progress_dialog.setAutoReset(True)
        self.progress_dialog.show()

        worker = Worker(self.editor, path)
        worker.signals.finished.connect(self.on_load_finished)
        worker.signals.result.connect(self.update_gui_with_data)  # Connect result signal to a new slot
        worker.signals.error.connect(self.handle_error)
        worker.signals.progress.connect(self.update_progress)  # Connect progress signal
        self.threadpool.start(worker)

    @Slot(int)
    def update_progress(self, progress):
        if self.progress_dialog:
            self.progress_dialog.setValue(progress)

    @Slot()
    def on_load_finished(self):
        if self.progress_dialog:
            self.progress_dialog.setValue(100)
            self.progress_dialog.close()
        self.editor.changes_signal.emit()
        print("Loading finished")

    @Slot(object)
    def update_gui_with_data(self, data):
        for tree_item, string in self.editor.items.items():
            if string.status != utils.String.Status.TranslationComplete:
                try:
                    if string.original_string in data:
                        string.translated_string = data[string.original_string].translated_string
                        string.status = data[string.original_string].status
                        tree_item.setText(4, utils.trim_string(string.translated_string))
                except KeyError:
                    continue

        self.editor.update_string_list()
        self.editor.changes_signal.emit()
        print('DB_IMPORTED')

    @Slot(tuple)
    def handle_error(self, error):
        exctype, value, tb = error
        print(f"Error: {exctype}, {value}")

    def execute_this_fn(self):
        print("Hello!")

    def oh_no(self):
        worker = Worker(self.editor, self.get_file_path())
        worker.signals.result.connect(self.handle_result)
        self.threadpool.start(worker)

    def export_json(self, full: bool = False) -> object:
        self.editor.log.info("Extracting to JSON...")
        data = []

        # Generate the data list
        for i, (tree_item, string) in enumerate(self.editor.items.items()):
            if full or string.status != utils.String.Status.TranslationComplete:
                group = string.type
                original_string = string.original_string
                translated_string = string.translated_string
                entry = {"index": i, "type": group, "original": original_string, "string": translated_string}
                data.append(entry)

        # Define the output path
        path = self.editor.app.data_path / "user" / "export" / self.editor.plugin_name
        output_path = str(path) + '.json'

        # Write the data to a JSON file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('[')

            for idx, entry in enumerate(data):
                json.dump(entry, f, ensure_ascii=False, separators=(',', ':'))

                # Add a comma after each entry except the last one
                if idx < len(data) - 1:
                    f.write(',\n')
                else:
                    f.write('\n')

            f.write(']')

        self.editor.log.info("Translation file exported to the export folder.")

    def import_json(self, only_edid: bool = False) -> object:
        self.editor.log.info("Extracting to json...")
        fdialog = QFileDialog()
        fdialog.setFileMode(fdialog.FileMode.ExistingFile)
        fdialog.setNameFilters(["*.json", "*.ats"])
        fdialog.setWindowTitle("Import Json File")

        if fdialog.exec() == fdialog.DialogCode.Rejected:
            return

        selected_files = fdialog.selectedFiles()

        if not selected_files:
            return

        selected_file = selected_files[0]
        self.load_from_db(selected_file)

    def import_esp(self, only_edid: bool = False) -> object:
        print("import ESP")
        fdialog = QFileDialog()
        fdialog.setFileMode(fdialog.FileMode.ExistingFile)
        fdialog.setNameFilters(["Bethesda Plugin (*.esp *.esm *.esl)"])
        fdialog.setWindowTitle("Import ESP File")

        if fdialog.exec() == fdialog.DialogCode.Rejected:
            return

        selected_files = fdialog.selectedFiles()

        if selected_files:
            self.editor.log.info("Importing translation...")
            file = Path(selected_files[0])

            translation_strings = self.extract_translation_strings(file, only_edid)

            for tree_item, string in self.editor.items.items():
                if string.status == utils.String.Status.TranslationComplete:
                    continue

                key = (
                    (string.editor_id, string.type)
                    if only_edid
                    else (string.editor_id, string.form_id, string.type)
                )
                if string.editor_id is None and only_edid:
                    continue

                if key in translation_strings:
                    if len(translation_strings[key]) > 1:
                        translations = [trans for trans in translation_strings[key] if trans.index == string.index]

                        if not translations:
                            continue

                        translation = translations[0]
                    else:
                        translation = translation_strings[key][0]

                    string.translated_string = translation.original_string
                    string.status = utils.String.Status.TranslationIncomplete

                    tree_item.setText(4, utils.trim_string(translation.original_string))

            self.editor.update_string_list()
            self.editor.changes_signal.emit()

    def import_gui(self):
        import_shortcut = qtg.QShortcut(qtg.QKeySequence("Ctrl+I"), self.editor)
        import_shortcut.activated.connect(self.import_esp)

        import_edid_shortcut = qtg.QShortcut(qtg.QKeySequence("Ctrl+L"), self.editor)
        import_edid_shortcut.activated.connect(lambda: self.import_esp(True))

        search_edid_shortcut = qtg.QShortcut(qtg.QKeySequence("Ctrl+F"), self.editor)
        search_edid_shortcut.activated.connect(self.editor.search_and_replace)

        import_json_shortcut = qtg.QShortcut(qtg.QKeySequence("Alt+I"), self.editor)
        import_json_shortcut.activated.connect(self.import_json)

        export_json_shortcut = qtg.QShortcut(qtg.QKeySequence("Alt+J"), self.editor)
        export_json_shortcut.activated.connect(self.export_json)

        export_json_full_shortcut = qtg.QShortcut(qtg.QKeySequence("Alt+F"), self.editor)
        export_json_full_shortcut.activated.connect(lambda: self.export_json(True))

        load_db_shortcut = qtg.QShortcut(qtg.QKeySequence("Ctrl+E"), self.editor)
        load_db_shortcut.activated.connect(lambda: self.load_from_db())

    def extract_translation_strings(self, translation_plugin: Path, only_edid=False) -> dict:
        plugin = Plugin(translation_plugin)
        translation_strings = plugin.extract_strings()
    
        translations_dict = {}
        for string in translation_strings:
            key = (
                (string.editor_id, string.type)
                if only_edid
                else (string.editor_id, string.form_id, string.type)
            )

            if key not in translations_dict:
                translations_dict[key] = []

            translations_dict[key].append(string)

        return translations_dict

"""
After
        self.app = app
        self.loc = app.loc
        self.mloc = app.loc.editor
        self.translation = translation
        self.plugin_name = plugin_name

in Editor.py

Add
from translation_editor.addons import EditorAddon
self.esp_importer = EditorAddon(self)
self.esp_importer.import_gui()
"""
