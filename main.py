# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

#convert a python list to a numpy array
def getNumpyArray(aList: list, dtype = 'int32') -> np.ndarray:
    return np.array(aList, dtype=dtype)

#get the dimention of a numpy array
def getDiemnsion(npArray: np.ndarray) -> int:
    return npArray.ndim

#get the shape of of a numpy array
def getShape(npArray: np.ndarray) -> tuple:
    return npArray.shape

#get the data type of the elements in a numpy array
def getDtataType(array: np.ndarray):
    return array.dtype

#get byte size of each element in array
def getItemSize(array: np.ndarray) -> int:
    return array.itemsize

#get total number of elements of a numpy array
def getNumberOfElements(array: np.ndarray) -> int:
    return array.size

#get total byte size of all elements in array
def getByteSize(array: np.ndarray) -> int:
    return array.nbytes

#this function do the same thing as getByteSize do
def getByteSize2(array: np.ndarray) -> int:
    return getNumberOfElements(array)*getItemSize(array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [[1,2,3], [45,3,1]]
    b = [1,2,3,43,53,33,1,2]
    npArray = getNumpyArray(a)
    npArray2 = getNumpyArray(b)
    npArray3 = getNumpyArray(a, 'int16')
    # print(getNumpyArray(a))
    print(getByteSize2(npArray3))
    print(getByteSize2(npArray3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
