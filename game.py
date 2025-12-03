import time
import random


class Game:
    # initialize the game parameters
    def __init__(self):
        # number of turns or rounds
        self.noOfRounds = 5

        # player name
        self.player = 'Player'

        # computerChoices
        self.computerChocies = []

        # playerChoices
        self.playerChoices = []

        # turnStatuses
        self.turnStatus = []

    def generateStats(self):
        pass

    def play(self):
        print('Game Begins. Best of Luck!')
        # play for the defined rounds or turns

        round = 1
        choices = ['Rock', 'Paper', 'Scissor']

        while True:
            # print the round number
            print('----Round:', round, '------')
            print('Rounds left:', self.noOfRounds)

            # ask the user to enter his or her choice from one of 'rock', 'paper', 'scissor'
            playerChoice = choices[int(
                input('What\'s your choice?\n1.Rock\n2.Paper\n3.Scissor'))-1]

            # generate the computer's choice
            computerChoice = random.choice(choices)

            print(playerChoice, computerChoice)

            # decide who wins the turn

            # record the decision

            # ensure that there are enough turns
            # if there are no turns, we end the game
            if round == self.noOfRounds:
                # stop the game
                break

            # update the number of rounds remaining
            round = round + 1
        # generate the final stats
        # self.generateStats()

    def begin(self):
        # print the opening stats
        print('-----Welcome to Rock Paper Scissor Game-------')
        print()
        print('Rules of the Game:\n\n1. Player chooses how many turns the game has to have.\n2. In every turn, the player will be asked to choose one of the choices from Rock, Paper, or Scissor.\n3. The Computer\'s choice will be random.\n4. Based on the following choices between computer vs player, the decision of who wins the turn is decided.\n5. The following are the possible choices and result. \n\n\tRock - Paper: Paper Wins\n\tRock-Scissor: Rock Wins\n\tPaper-Scissor: Scissor Wins')
        # print the rules of the game
        # get the user's choice to start the game or quit the game.

        self.player = input('What\'s your name? ')

        self.noOfRounds = input('How many turns you want to play? ')

        seconds = 3
        while seconds > 0:
            time.sleep(1)
            print('Game begins in', seconds, 'seconds...')
            seconds = seconds - 1

        # start the game
        self.play()


game = Game()
game.begin()
