import highscore
import player


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
        # TODO: load higescore.players
        User_interface.main_menu()

    @staticmethod
    def game_setup_menu():
        """Setups up the game, how many players and how many bots"""
        # Här kan man säga till vilka spelar profiler som ska vara med i spelet &
        # hur många botar
        pass

    @staticmethod
    def main_menu():
        """Main menu of the program"""
        option = User_interface.input_handler_int_range(
            "1. Play game \n" +
            "2. Create player profile \n" +
            "3. Change player profile \n" +
            "4. Exit \n",
            1, 4
        )
        if option == 1:
            User_interface.game_setup_menu()
        elif option == 2:
            User_interface.create_player_profile()
        elif option == 3:
            User_interface.change_player_profil()
        elif option == 4:
            User_interface.higescore.create_players()
            quit()

    @staticmethod
    def throw_dice_loop(player_ref):
        """
        This function controlls the flow of the dice loop,
        the players ability to throw dices.
        """
        # TODO: Make it possible to throw dice
        # and the logic to return points
        # return the points as a list
        return True

    @staticmethod
    def display_whos_turn(player_ref):
        """Display whos turn it is"""
        print("New turn: " + player_ref.username)
        # Varje turn så måste vi veta vems turn det är
        pass

    @staticmethod
    def create_player_profile():
        """Creates a player profile"""
        while True:
            in_from_client = input("Enter a username for this player:")
            if in_from_client == "quit":
                User_interface.main_menu()
                return
            new_player = player.Player(in_from_client)
            exist_flag = False
            print(User_interface.higescore.players)
            for p in User_interface.higescore.players:
                if p.username == new_player.username:
                    print("Player with that name already exist!")
                    print("Type 'quit' to cancel")
                    exist_flag = True
            if not exist_flag:
                break
        User_interface.higescore.players.add(new_player)
        # TODO: Saves higescore.players
        User_interface.main_menu()

    @staticmethod
    def change_player_profil():
        """Change a player profile"""
        # TODO: Saves higescore.players after creation
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
                if value in range(min + 1, max + 1):
                    return value
                else:
                    print(f"Input has to in range of {min} - {max}")
            except ValueError:
                print("Input has to be an integer")

    @staticmethod
    def game_ended(player_ref):
        """Method that displays taht the game ended"""
        # player is ref to winner
        print(player_ref.username + " won the game!")
        # TODO: Saves higescore.players after creation


#User_interface.start()
