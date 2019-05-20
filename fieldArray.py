from field import field
import random


class fieldArray(field):
    array = []

    def __init__(self, arraySize, fieldSize):
        self.arraySize = arraySize
        self.fieldSize = fieldSize
        self.array = [field(fieldSize, 0) for x in range(arraySize)]

    def fillRandom(self):
        for i in range(self.arraySize):
            self.array[i].setValue(random.randint(0, self.fieldSize-1))

    def fillWithSpecificDensity(self):
        pass

    def density(self):
        tempCounter = 0
        for i in range(self.arraySize):
            if(self.array[i] == 0):
                tempCounter += 1
        return tempCounter / self.arraySize

    def setValue(self, position, other):
        # control the value of te position ( out of bound problem)
        assert(position < self.arraySize), "position is bigger than the array size"
        assert(other.getValue() <
               self.fieldSize), "value must be bounded by field size"
        self.array[position] = other.getValue()

    # override plus
    def __add__(self, other):
        assert(self.arraySize ==
               other.arraySize), "array size must be eqaul which is not here!"
        assert(self.fieldSize == other.getFieldSize()
               ), "field size must be eqaul which is not here!"
        tempFieldArray = fieldArray(self.arraySize,
                                    self.fieldSize)

        for i in range(self.arraySize):
            tempFieldArray.array[i] = self.array[i] + other.array[i]

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
            tempField = self.array[i] * other.array[i]
            tempFieldArray.array[i] = tempField
        return tempFieldArray

    def show(self):
        string = "["
        for i in range(self.arraySize - 1):
            string += str(self.array[i].getValue()) + ','

        string += str(self.array[self.arraySize - 1].getValue()) + ']'
        print(string)


if __name__ == "__main__":

    varJ = fieldArray(10, 10)
    varJ.fillRandom()
    varJ.show()

    varK = fieldArray(10, 10)
    varK.fillRandom()
    varK.show()

    varTest = varK * varJ
    varTest.show()
    varA = field(10, 7)
    varB = field(10, 5)
    varC = varA + varB
    varD = varA * varC
    print(varC.getValue())
    print(varD.getValue())
