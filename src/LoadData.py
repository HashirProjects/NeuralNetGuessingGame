from numpy import array

class InsufficientDataError(Exception):
    pass

def load(userInput):
	def splitString(string):
		return [char for char in string]

	dataSet= splitString(userInput)
	dataX = []
	dataY = []

	for i in range(len(dataSet)-10):
		dataX.append(dataSet[i:i+10])
		dataY.append(dataSet[i+10])

	return array(dataX) ,array(dataY)