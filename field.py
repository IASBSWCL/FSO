import random


class field(object):
    value = 0
    # parameterized constructor
    # default value for having multiple constructor

    def __init__(self, fieldSize, value=0):
        if(fieldSize < value):
            print("you can't set the value greater than your filed size")
        else:
            self.fieldSize = fieldSize
            self.value = value

    def displaySize(self):
        print(self.fieldSize)

    def setValue(self, value):
        if (value < self.fieldSize):
            self.value = value
        else:
            print("Unacceptable range.")
        #  return

    def getValue(self):
        return self.value

    def getFieldSize(self):
        return self.fieldSize

    # def __del__(self):
    #     print("Class deleted")

    def __add__(self, other):
        # handle this with assert
        if(self.fieldSize == other.getFieldSize()):
            tempValue = (self.value + other.value) % self.fieldSize
            return field(self.fieldSize, tempValue)
        else:
            print("To add two different value their filed size must be the same.")

    def __mul__(self, other):
        if(self.fieldSize == other.getFieldSize()):
            tempValue = (self.value * other.value) % self.fieldSize
            return field(self.fieldSize, tempValue)
        else:
            print("To add two different value their filed size must be the same.")