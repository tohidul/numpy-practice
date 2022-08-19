# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def getNumpyArray(aList: list, dtype = 'int32') -> np.ndarray:
    return np.array(aList, dtype=dtype)

def getDiemnsion(npArray: np.ndarray) -> int:
    return npArray.ndim

def getShape(npArray: np.ndarray) -> tuple:
    return npArray.shape

def getDtataType(array: np.ndarray):
    return array.dtype


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [[1,2,3], [45,3,1]]
    b = [1,2,3,43,5345]
    npArray = getNumpyArray(a)
    npArray2 = getNumpyArray(a, 'int8')
    npArray3 = getNumpyArray(a, 'int16')
    # print(getNumpyArray(a))
    print(getDtataType(npArray2))
    print(getDtataType(npArray3))
    print(getDtataType(npArray))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
