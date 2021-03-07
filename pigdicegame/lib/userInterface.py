import highscore


class User_interface():
    """
    This class controlls the input and output to the player.
    """

    # Ref to higescore class
    higescore = None

    @staticmethod
    def start():
        """Start of program"""
        User_interface.higescore = highscore.Highscore()
        User_interface.higescore.create_players()
        User_interface.main_menu()

    @staticmethod
    def game_setup_menu():
        """Setups up the game, how many players and how many bots"""
        pass

    @staticmethod
    def main_menu():
        """Main menu of the program"""
        print("1. Play game")
        print("2. Create player profile")
        print("3. Change player profile")
        print("4. Exit")

    @staticmethod
    def throw_dice_loop(player):
        """
        This function controlls the flow of the dice loop,
        the players ability to throw dices.
        """
        # TODO: Make it possible to throw dice
        # and the logic to return points
        # return the points as a list
        return True

    @staticmethod
    def display_whos_turn(player):
        """Display whos turn it is"""
        print("New turn: " + player.username)
        # Varje turn så måste vi veta vems turn det är
        pass

    @staticmethod
    def display_dice_throw(player, dice):
        """Display a dice throw"""
        print(player.username + f" rolled: {dice}")
        pass

    @staticmethod
    def create_player_profiel():
        """Creates a player profile"""
        User_interface.create_highscore()   # Saves data after creation
        pass

    @staticmethod
    def change_player_profiel():
        """Change a player profile"""
        User_interface.create_highscore()   # Saves data after change
        pass

    @staticmethod
    def input_handler_string(question):
        """Handles input from user with error handling,
        returning input as string
        """
        pass

    @staticmethod
    def input_handler_int_range(question, min, max):
        """Handles int input from user with error handling and checks if int
        is in range of min & max param, returning int inputed int.
        """
        value = None
        while True:
            try:
                value = int(input(question))
                if value in range(min, max + 1):
                    return value
                else:
                    print(f"Input has to in range of {min} - {max}")
            except ValueError:
                print("Input has to be an integer")

    @staticmethod
    def game_ended(player):
        """Method that displays taht the game ended"""
        # player is ref to winner
        User_interface.create_highscore()   # Saves data after game


User_interface.input_handler_int_range("he", 0, 1)