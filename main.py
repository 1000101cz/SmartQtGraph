import sys

import numpy as np
import pandas as pd
from PyQt5 import QtWidgets, uic
import pyqtgraph as pg

from SmartQtPlot import SmartQtPlot

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('window.ui', self)
        self.show()

        time_array = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        force_array0 = np.array([1.1, 1.2, 1.4, 1.55, 1.89, 2.65, 3.33])
        force_array1 = np.array([1.0, 1.3, 1.32, 1.32, 1.40, 2.46, 4.38])
        force_array2 = np.array([0.8, 6.2, 3.4, 3.55, 3.89, 4.65, 4.97])

        df = pd.DataFrame({'ID': ['123456789', '456789123', '789456132'],
                           'CURVE_Time': [time_array, time_array, time_array],
                           'CURVE_Force': [force_array0, force_array1, force_array2]})

        self.smartPlot = SmartQtPlot(self.graphicsView)
        self.smartPlot.add(df)

        self.smartPlot.visualize_all(yAxis='Force', xAxis='Time')
        self.smartPlot.hide_all()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
