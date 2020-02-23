import os
import pandas as pd
import numpy as np
import sys

class PlotData:

    def __init__(self):
        self.df = None

    def loadData(self, path):
        self.df = pd.read_csv(path)

    def returnData(self, col):
        d = self.df[col]
        return d



if __name__ == '__main__':
    _plotData = PlotData()
    _plotData.loadData('./data/iris.csv')
    print([ i for i in _plotData.returnData('x1')])
    print(_plotData.returnData('sp'))

    

