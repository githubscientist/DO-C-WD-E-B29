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
        print('Game ended!')
        print('------Game Stats:------')
        print('Rounds:', self.noOfRounds)
        playerWinCounts = self.turnStatus.count('player')
        computerWinCounts = self.turnStatus.count('computer')

        # add each round status as well
        # not implemented yet

        if (playerWinCounts > computerWinCounts):
            print(self.player, 'won the game. Congratulations!!')
        elif (playerWinCounts < computerWinCounts):
            print('Sorry!', self.player, 'lost the game.')
        else:
            print('The game is a draw. You scored equal points with the Computer')

    def getDecision(self, playerChoice, computerChoice):
        '''
            computerChoice = 'Rock'         player
                    playerChoice = 'Paper'

                    computerChoice = 'Rock'         computer
                    playerChoice = 'Scissor'

                    computerChoice = 'Paper'        player
                    playerChoice = 'Scissor'
        '''
        if computerChoice == 'Rock':
            if playerChoice == 'Paper':
                return 'player'
            elif playerChoice == 'Scissor':
                return 'computer'
            else:
                return 'tie'
        elif computerChoice == 'Paper':
            if playerChoice == 'Rock':
                return 'computer'
            elif playerChoice == 'Scissor':
                return 'player'
            else:
                return 'tie'
        elif computerChoice == 'Scissor':
            if playerChoice == 'Rock':
                return 'player'
            elif playerChoice == 'Paper':
                return 'computer'
            else:
                return 'tie'

    def play(self):
        print('Game Begins. Best of Luck!')
        # play for the defined rounds or turns

        round = 1
        choices = ['Rock', 'Paper', 'Scissor']

        while True:
            # print the round number
            print('----Round:', round, '------')
            print('Rounds left:', self.noOfRounds - round)

            # decide who wins the turn
            '''
                When the choices are same:
                    computerChoice = 'Rock'
                    playerChoice = 'Rock'

                    computerChoice = 'Paper'
                    playerChoice = 'Paper'

                    computerChoice = 'Scissor'
                    playerChoice = 'Scissor'

                        should we discard the turn? we should not increase the round
                        round = round - 1

                
                When the choices are different:
                    computerChoice = 'Rock'         player
                    playerChoice = 'Paper'

                    computerChoice = 'Rock'         computer
                    playerChoice = 'Scissor'

                    computerChoice = 'Paper'        player
                    playerChoice = 'Scissor'

                From this decision, what do we want?

                    - who wins that turn? player or computer
                    - record the same in the turnStatus list as player or computer -- in draw cases, we can record it as 'draw'
            '''
            # ask the user to enter his or her choice from one of 'rock', 'paper', 'scissor'
            playerChoice = choices[int(
                input('What\'s your choice?\n1.Rock\n2.Paper\n3.Scissor\n'))-1]

            # generate the computer's choice
            computerChoice = random.choice(choices)

            print('Player\'s choice:', playerChoice)
            print('Computer\'s choice:', computerChoice)

            while True:
                if self.getDecision(playerChoice, computerChoice) != 'tie':
                    break

                print('It\'s a tie. Make your choice again!')

                # ask the user to enter his or her choice from one of 'rock', 'paper', 'scissor'
                playerChoice = choices[int(
                    input('What\'s your choice?\n1.Rock\n2.Paper\n3.Scissor\n'))-1]

                # generate the computer's choice
                computerChoice = random.choice(choices)

                print('Player\'s choice:', playerChoice)
                print('Computer\'s choice:', computerChoice)

            # record the decision
            self.turnStatus.append(self.getDecision(
                playerChoice, computerChoice))

            # record the player choice and computer choice
            self.playerChoices.append(playerChoice)
            self.computerChocies.append(computerChoice)

            # print the turn stats
            print(self.getDecision(playerChoice, computerChoice), 'wins this turn')

            seconds = 3
            while seconds > 0:
                time.sleep(1)
                print('Next turn in', seconds, 'seconds...')
                seconds = seconds - 1

            # ensure that there are enough turns
            # if there are no turns, we end the game
            if round == self.noOfRounds:
                # stop the game
                break

            # update the number of rounds remaining
            round = round + 1

        # generate the final stats
        self.generateStats()

    def begin(self):
        # print the opening stats
        print('-----Welcome to Rock Paper Scissor Game-------')
        print()
        print('Rules of the Game:\n\n1. Player chooses how many turns the game has to have.\n2. In every turn, the player will be asked to choose one of the choices from Rock, Paper, or Scissor.\n3. The Computer\'s choice will be random.\n4. Based on the following choices between computer vs player, the decision of who wins the turn is decided.\n5. The following are the possible choices and result. \n\n\tRock - Paper: Paper Wins\n\tRock-Scissor: Rock Wins\n\tPaper-Scissor: Scissor Wins')
        # print the rules of the game
        # get the user's choice to start the game or quit the game.

        self.player = input('What\'s your name? ')

        self.noOfRounds = int(input('How many turns you want to play? '))

        seconds = 3
        while seconds > 0:
            time.sleep(1)
            print('Game begins in', seconds, 'seconds...')
            seconds = seconds - 1

        # start the game
        self.play()


game = Game()
game.begin()
