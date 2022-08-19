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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [[1,2,3], [45,3,1]]
    b = [1,2,3,43,5345]
    npArray = getNumpyArray(a)
    # print(getNumpyArray(a))
    print(getDiemnsion(npArray))
    print(getShape(getNumpyArray(b)))
    print(type(npArray))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
