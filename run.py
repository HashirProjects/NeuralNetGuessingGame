from src.TrainModel import TrainModel
from src.Play import PlayModel

if __name__ == "__main__":
    print("Welcome to the ML guessing game! type 'TRAIN' to train the NN or 'PLAY' to have the NN make a guess")

    while True:
        command = input("> ")
        if command.upper() == "EXIT":
            break
        try:
            if command.upper() == "TRAIN":
                Model = TrainModel(input("Enter some random numbers (at least 100)."))
                Model.Train()
                print("Completed training.")        
            if command.upper() == "PLAY":
                UserGuess = PlayModel(input("Enter some random numbers (at least 20)."))
                UserGuess.play()
            if command.upper() == "CHECK_IF_TRAINED":
                print("check if played not yet implemented")
            else:
                print("Type either 'TRAIN' or 'PLAY' or 'CHECK_IF_TRAINED'")
        except Exception as e:
            print ("Try again.")
            
    print("Exit Message")