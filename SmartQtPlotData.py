import polars as pl
import pandas as pd
import numpy as np
from loguru import logger


class SingleSmartQtPart:
    def __init__(self, this_id: str, item=None, xAxis: str | None = None, yAxis: str | None = None):
        """

        :param this_id:     this parts id
        :param item:        this parts PlotItem or None if not exists
        :param xAxis:       visualized x-axis or None (=index)
        :param yAxis:       visualized y-axis
        """
        self.id = this_id
        self.item = item
        self.xAxis = xAxis
        self.yAxis = yAxis
        self._data = {}

    def axis(self, name: str) -> np.ndarray:
        return self._data[name]

    def idx(self, ref: str) -> np.ndarray:
        length = len(self._data[ref])
        return np.arange(0, length, 1.0)

    def add_axis(self, name: str, value: np.ndarray | list):
        """ Add new part axis """

        if name in self._data:
            raise KeyError(f"Axis {name} already defined")

        value = self._parse_array(value)

        self._data[name] = value

    def update_axis(self, name: str, value: np.ndarray):
        if name not in self._data:
            raise KeyError(f"Axis {name} not defined")

        value = self._parse_array(value)

        self._data[name] = value

    @staticmethod
    def _parse_array(value):
        # convert to numpy
        if isinstance(value, np.ndarray):
            ...
        elif isinstance(value, list):
            value = np.array(value)

        # convert to 1D
        if len(value.shape) == 1:
            ...
        else:
            logger.warning(f"Invalid shape for axis. Expected 1D array but got {value.shape}. Trying ravel ...")
            value = value.ravel()

        return value


class SmartQtPlotData:
    def __init__(self):
        super().__init__()

        self.data = {}

    def add(self, data: pl.DataFrame | pd.DataFrame):
        """ Add new data to visualization dataset """

        if isinstance(data, pl.DataFrame):
            self._add_polars(data)
        elif isinstance(data, pd.DataFrame):
            self._add_pandas(data)
        else:
            raise TypeError(f"Invalid data type: {type(data)}")

        logger.info("data added")

    def _add_polars(self, data: pl.DataFrame):
        """ Add data from polars dataset """

        ...

    def _add_pandas(self, data: pd.DataFrame):
        """ Add data from pandas dataset """

        data.apply(self._add_pandas_row, axis=1)

    def _add_pandas_row(self, row: pd.Series):
        """ Add single row form pandas dataset """
        this_id = row['ID']

        if this_id in self.data:
            logger.warning(f"Curve {this_id} already in dataset. Skipping...")
            return

        self.data[this_id] = SingleSmartQtPart(this_id=this_id)

        for axis in self._row_axes_pandas(row):
            self.data[this_id].add_axis(axis, row[f'CURVE_{axis}'])

    @staticmethod
    def _row_axes_pandas(row: pd.Series) -> list:
        axes = []
        for col in row.keys().tolist():
            if col.startswith('CURVE_'):
                axes.append(col[6:])
        return axes

    @staticmethod
    def prepare_axis_data(part, xAxis, yAxis):
        yData = part.axis(yAxis)
        if xAxis is None:
            xData = part.idx(yAxis)
        else:
            xData = part.axis(xAxis)

        return xData, yData