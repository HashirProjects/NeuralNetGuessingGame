"""Fetches the model and evalutes accuracy
user entry is a string of numbers (similar to __init__ of trainmodel)
Play divides entry into X,Y pairs, runs the model on each and then computes accuracy
"""
from src.LoadData import load, InsufficientDataError

class PlayModel():
	def __init__(self,userInput):

		if len(userInput) < 20:
			raise InsufficientDataError("Too little data for NN to provide accurate results, Please provide more than 20 entries")
			return

		self.x, self.y =load(userInput)

	def play(self):

		from tensorflow import keras

		model = keras.models.load_model('C:/Users/hashi/OneDrive/Desktop/Programming/NN_GuessingGame/src/UserModel')

		numberOfEntries = len(self.x)
		correct = 0

		guess = model(self.x)
		results=[]
		expectedResults=[]

		for entry in guess:
			maxindex=0
			maxvalue=0
			for i in range(len(entry)):
				if entry[i] > maxvalue:
					maxvalue = entry[i]
					maxindex = i

			results.append(maxindex)

		for entry in self.y:
			maxindex=0
			maxvalue=0
			for i in range(len(entry)):
				if entry[i] > maxvalue:
					maxvalue = entry[i]
					maxindex = i

			expectedResults.append(maxindex)

		print(results, expectedResults)

		for i in range (numberOfEntries):
			if results[i] == expectedResults[i]:
				correct +=1

		accuracy = correct/numberOfEntries

		if accuracy > 0.15:
			print(f"the computer won with an accuracy of {accuracy}")
		else:
			print(f"You won! The computer had an accuracy of {accuracy}")