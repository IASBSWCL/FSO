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

    def __del__(self):
        print("Class deleted")

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


class fieldArray(field):
    array = []

    def __init__(self, arraySize, fieldSize):
        self.arraySize = arraySize
        self.fieldSize = fieldSize
        self.array = [field(fieldSize, 0) for x in range(arraySize)]

    def fillRandom(self):
        for i in range(self.arraySize):
            self.array[i].setValue(random.random() % self.fieldSize)
    def fillWithSpecificDensity(self):
        pass

    def density(self):
        tempCounter = 0
        for i in range(self.arraySize):
            if(self.array[i] == 0):
                tempCounter += 1
        return tempCounter / self.arraySize

    def setValue(self, position, value):
        # control the value of te position ( out of bound problem)
        assert(position > self.arraySize), "position is bigger than the array size"
        assert(value > self.fieldSize), "value must be bounded by field size"
        self.array[position] = value

    # override plus
    def __add__(self, other):
        assert(self.arraySize ==
               other.arraySize), "array size must be eqaul which is not here!"
        assert(self.fieldSize == other.getFieldSize()
               ), "field size must be eqaul which is not here!"
        tempFieldArray = fieldArray(self.arraySize, self.fieldSize)

        for i in range(self.arraySize):
            tempFieldArray.setValue(i, self.array[i] + other.array[i])

        return tempFieldArray
    # override multiplication

    def __mul__(self, other):
        # check the array size, They must be the same
        assert(self.arraySize ==
               other.arraySize), "array size must be eqaul which is not here!"
        assert(self.fieldSize == other.getFieldSize()
               ), "field size must be eqaul which is not here!"
        tempFieldArray = fieldArray(self.arraySize, self.fieldSize)

        for i in range(self.arraySize):
            tempFieldArray.setValue(i, self.array[i] * other.array[i])
        return tempFieldArray


if __name__ == "__main__":

    varJ = fieldArray(10, 10)
    varJ.fillRandom()
    varA = field(10, 7)
    varB = field(10, 5)
    varC = varA + varB
    varD = varA * varC
    print(varC.getValue())
    print(varD.getValue())
