from numpy import array

class InsufficientDataError(Exception):
    pass

def load(userInput):
	def splitString(string):
		return [int(char) for char in string]

	dataSet= splitString(userInput)
	dataX = []
	dataY = []

	for i in range(len(dataSet)-10):
		dataX.append(dataSet[i:i+10])
		emptyYentry = [0,0,0,0,0,0,0,0,0,0]
		emptyYentry[dataSet[i+10]] = 1
		dataY.append(emptyYentry)

	return array(dataX) ,array(dataY)