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

    @classmethod
    def getValue(self):
        return self.value

    def getFieldSize(self):
        return self.fieldSize

    def __del__(self):
        print("Class deleted")

    # overwriting methods = add two value in specific field size
    # what should we do with carry
    def __add__(self, other):
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


class fieldArray(field):
    array = []

    def __init__(self, arraySize, fieldSize):
        self.arraySize = arraySize
        self.fieldSize = fieldSize
        self.array = [field(fieldSize, 0) for x in range(arraySize)]

    def fillRandom(self):
        for i in range(self.arraySize):
            self.array[i] = random.random() % self.fieldSize

    def density(self):
        tempCounter = 0
        for i in range(self.arraySize):
            if(self.array[i] == 0):
                tempCounter += 1
        return tempCounter / self.arraySize
    # override plus

    # override multiplication
    def __mul__(self, other):
        # check the array size, They must be the same 
        for i in range (self.arraySize):
            pass


if __name__ == "__main__":
    varA = field(10, 7)
    varB = field(10, 5)
    varC = varA + varB

    varD = varA * varC
    print(varC.getValue())
    print(varD.getValue())
