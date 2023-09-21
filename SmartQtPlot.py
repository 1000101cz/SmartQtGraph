"""
Class for smarter management of visualized data.

Each curve is accessible by its key.


self.data  inside SmartQtPlot
 {
    'id1': {
                'plot':  PlotItem or None
                'xAxis': string (name of visualized x-axis)
                'yAxis': string (name of visualized y-axis)
                'data': {
                            'axis1': 1D numpy array
                            'axis2': 1D numpy array
                            ...
                        }
            }
    ...


"""
from pyqtgraph import PlotWidget

from SmartQtPlotVisualization import SmartQtPlotVisualization


class SmartQtPlot(SmartQtPlotVisualization):
    def __init__(self, pw: PlotWidget, style=None):
        super().__init__(pw=pw)

        self._init_style(style)

    def _init_style(self, style):
        ...
