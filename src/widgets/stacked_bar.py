"""
This file is part of SSE Auto Translator
by Cutleast and falls under the license
Attribution-NonCommercial-NoDerivatives 4.0 International.
"""

import qtpy.QtCharts as qtd
import qtpy.QtCore as qtc
import qtpy.QtGui as qtg


class StackedBar(qtd.QChartView):
    """
    Class for stacked bar for displaying data ratios.
    """

    def __init__(self, values: list[int], colors: list = None):
        super().__init__()

        self.setRubberBand(self.RubberBand.NoRubberBand)
        self.setResizeAnchor(self.ViewportAnchor.AnchorViewCenter)
        self.setContentsMargins(0, 0, 0, 0)
        self.setRenderHint(qtg.QPainter.RenderHint.LosslessImageRendering)

        self._chart = qtd.QChart()
        self._chart.setMargins(qtc.QMargins(0, 0, 0, 0))
        self._chart.layout().setContentsMargins(0, 0, 0, 0)
        self._chart.setBackgroundRoundness(0)
        self._chart.setBackgroundVisible(False)
        self._chart.legend().hide()
        self._chart.setAnimationOptions(qtd.QChart.AnimationOption.SeriesAnimations)
        self.setChart(self._chart)
        self.__series = qtd.QHorizontalPercentBarSeries()
        self.__series.setBarWidth(2)
        self._chart.addSeries(self.__series)

        self.__bar_sets: list[qtd.QBarSet] = []
        for v, value in enumerate(values):
            bar_set = qtd.QBarSet("")
            bar_set.append(value)

            if colors is not None:
                color = colors[v]
                if color is None:
                    color = qtc.Qt.GlobalColor.lightGray
                bar_set.setColor(color)

            bar_set.setBorderColor(qtc.Qt.GlobalColor.transparent)
            self.__series.append(bar_set)
            self.__bar_sets.append(bar_set)

    def setValues(self, values: list[int]):
        for v, value in enumerate(values):
            bar_set = self.__bar_sets[v]
            bar_set.remove(0)
            bar_set.append(value)

    def setColors(self, colors: list):
        for c, color in enumerate(colors):
            bar_set = self.__bar_sets[c]
            if color is None:
                color = qtc.Qt.GlobalColor.lightGray
            bar_set.setColor(color)
