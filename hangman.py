# Hangman game
# Object_Oriented

import random


class HangmanGame:
    __TURNS = 10  # Turns is a constant to control the number of turns each player can use to guess the word.
    # player_list is a list of all the usernames added by the users.
    player_list = []
    # __answers is a list of potential answers, from which the secret word will be chosen randomly.
    # I intentionally didn't make the list long to make the answers easier to guess so the code can be easier to test.
    __answers = ["Sunset", "Abroad", "Budget"]

    def __init__(self):
        self.name = input("What's your name? ")
        HangmanGame.player_list.append(self)
        self.new_game()

    # The reason that new_game is defined as a separate method is that other than initializing an object, it's also needed to reset the game variables if a user chooses to play another game after the last game has just ended. (See GameController)
    def new_game(self):
        self.index = random.randint(0, len(HangmanGame.__answers) - 1)
        self.__answer = HangmanGame.__answers[self.index]
        self.__turns_left = HangmanGame.__TURNS
        # Technically, self.win and self.lose can be combined in one variable. But I decided to keep both in case I want to develop the code further and add features like keeping score, later.
        self.__win = False
        self.__lose = False

        self.__answer = self.__answer.lower()
        # self.__answer_to_list is the list form of answer. It is used to compare answer to output to determine if a user has won all the characters correctly yet or not.
        self.__answer_to_list = []
        for ch in self.__answer:
            self.__answer_to_list.append(ch)

        # self.output is used to show the length of the secret answer and the characters guessed correctly so far to the user.
        self.output = []
        for i in range(len(self.__answer)):
            self.output.append("-")

    # one_turn carries out one turn of Hangman for one player.
    # At the end of the turn it checks to see if there's a winner and if the turns of a player are over.
    def one_turn(self):
        if self.__turns_left <= 0:
            self.__lose = True
            print(
                """Sorry""",
                self.name,
                """ Your time is up!
            The answer was """,
                self.__answer,
                """.""",
            )
        else:
            # string s is just used to convert output to a string.
            s = ""
            correct = False

            print(self.name, "You have ", self.__turns_left, " guess[es] left.")
            print(s.join(self.output))
            user_guess = input("Guess a letter!")

            self.__turns_left -= 1
            if (user_guess.isalpha() and len(user_guess) == 1) == False:
                print("Wrong input! You must enter a single character!")

            else:
                for i in range(len(self.__answer)):
                    if self.__answer[i] == user_guess.lower():
                        correct = True
                        self.output[i] = user_guess.lower()

                if correct == False:
                    print("Wrong guess!")

                else:
                    print("Correct guess!")
                    if self.output == self.__answer_to_list:
                        self.__win = True
                        print(
                            """Congrats """,
                            self.name,
                            """on winning the Hangman!""",
                            """The answer is """,
                            self.__answer,
                            """ and you guessed it!""",
                        )

            return self.__win

    @classmethod
    def game_over(cls):
        if any(player.__win == True for player in cls.player_list) or any(
            player.__lose == True for player in cls.player_list
        ):
            return True
        else:
            return False


class GameController:
    def __init__(self):
        # If user choosese to go back to play another game after a game has just ended, the variables related to the game (such as __win, turns_left, answer,...) need to be reset.
        if HangmanGame.game_over():
            for player in HangmanGame.player_list:
                player.new_game()

        while not (HangmanGame.game_over()):
            for player in HangmanGame.player_list:
                if not (HangmanGame.game_over()):
                    player.one_turn()


if __name__ == "__main__":
    print("Welcome to Hangman!")
    print("First, you need to add a new player.")
    HangmanGame()
    while True:
        order = input(
            "What do you want to do, next? Press A for adding a new player, P for playing Hangman and E to exit."
        )
        if order == "A" or order == "a":
            HangmanGame()
        elif order == "P" or order == "p":
            GameController()
        elif order == "E" or order == "e":
            break
