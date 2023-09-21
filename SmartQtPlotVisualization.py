from pyqtgraph.widgets import PlotWidget

from SmartQtPlotData import SmartQtPlotData


class SmartQtPlotVisualization(SmartQtPlotData):
    def __init__(self, pw: PlotWidget):
        super().__init__()

        self.pw = pw

        self._current_x = None
        self._current_y = None

    def visualize_all(self, yAxis, xAxis=None):
        self._current_x = xAxis
        self._current_y = yAxis

        for key in self.data:
            if self.data[key].item is None:

                xData, yData = self.prepare_axis_data(self.data[key], xAxis, yAxis)

                self.data[key].item = self.pw.plot(x=xData, y=yData)
            else:
                self.data[key].item.setVisible(True)

    def hide_all(self):
        for key in self.data:
            if self.data[key].item is not None:
                self.data[key].item.setVisible(False)

