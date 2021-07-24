import src.TrainModel

if __name__ = "__main__":
	print("Welcome to the ML guessing game! type 'TRAIN' to train the NN or 'PLAY' to have the NN make a guess")
    while True:
        command = input("> ")
        if command.upper() == "EXIT":
            break
        try:
            if command.upper() == "TRAIN":
            	Model = TrainModel(input("Enter some random numbers (at least 100)."))
            if command.upper() == "PLAY":
            	print("Play not yet implemented")
            if command.upper() == "CHECK_IF_TRAINED":
            	print("check if played not yet implemented")
        except Exception as e:
            
    print("Exit Message")