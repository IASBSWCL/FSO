from fieldArray import *
from field import field


def most_frequent(List):
    ''' returns the mostFrequent item and frequency percentage'''
    mostFrequentValue = 0
    mostFrequentItem = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > mostFrequentValue):
            mostFrequentValue = curr_frequency
            mostFrequentItem = i

    frequencyPercentage = mostFrequentValue / len(List)
    return mostFrequentItem , frequencyPercentage


if __name__ == "__main__":

    ARRAY_SIZE = 20
    FIELD_SIZE = 2

    EXAMINATION_NUMBER = 1000
    zeroExpected = 0
    frequentExpected = 0
    print(len([2,1,2]))

    for i in range(EXAMINATION_NUMBER):
        varJ = fieldArray(ARRAY_SIZE, FIELD_SIZE)
        varJ.fillRandom()
        # varJ.show()
        zeroExpected += varJ.getExactDensity()
        mostFrequentItem , frequencyPercentage = most_frequent(varJ.giveArraySimpleForm())
        frequentExpected += frequencyPercentage
        # print(most_frequent(varJ.giveArraySimpleForm()))
        print("Density is equal to: ", varJ.getExactDensity())

    print("Expected zero Value :", (zeroExpected / EXAMINATION_NUMBER)*100,"%")
    print("Ordinary zero Chance :", (1 / FIELD_SIZE)*100,"%")
    print("New method upperbound Value :", (frequentExpected / EXAMINATION_NUMBER)*100,"%")
