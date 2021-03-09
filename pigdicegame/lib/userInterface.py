import highscore
import player
import bot
import game


class Userinterface():
    """
    This class controlls the input and output to the player.
    """

    # Ref to higescore class
    higescore = None

    @staticmethod
    def start():
        """Start of program"""
        Userinterface.higescore = highscore.Highscore()
        Userinterface.higescore.create_players()
        Userinterface.main_menu()

    @staticmethod
    def game_setup_menu():
        """Setups up the game, how many players and how many bots
        and adds them to a list"""
        players = []
        the_player = Userinterface.find_player()
        the_player.append(player)
        bots = range(Userinterface.input_handler_int_range(
            "Enter the number of bots (min 1, max 4) you'd like to play " +
            "against: ", 1, 4))
        for _ in bots:
            players.append(bot.Bot(""))
        game.Game.start_game(players)


    @staticmethod
    def main_menu():
        """Main menu of the program"""
        option = Userinterface.input_handler_int_range(
            "1. Play game \n" +
            "2. Create player profile \n" +
            "3. Change player profile \n" +
            "4. Exit \n",
            1, 4
        )
        if option == 1:
            Userinterface.game_setup_menu()
        elif option == 2:
            Userinterface.create_player_profile()
        elif option == 3:
            Userinterface.change_player_profil()
        elif option == 4:
            Userinterface.higescore.create_highscore()
            quit()

    @staticmethod
    def throw_dice_loop(player_ref):
        """
        This function controlls the flow of the dice loop,
        the players ability to throw dices.
        """
        choice = ""
        points_accumulated = 0
        while choice != "N":
            choice = Userinterface.throw_dice_input()
            dice_result = player_ref.throw_dice()
            if dice_result == 1:
                print("You rolled a 1. You lost your score" +
                      "and it's the next players turn")
                return 0
            points_accumulated += dice_result
        return points_accumulated

    @staticmethod
    def throw_dice_input():
        """docstring"""
        while True:
            try:
                user_input = str(
                    input("Do you wish to throw the dice? (Y/N): "))
                user_input.capitalize()
                if user_input == "Y" or user_input == "N":
                    return user_input
                print("You need to enter Y to throw the dice or N to hold")
            except ValueError:
                print("You need to enter Y or N")


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
            in_from_client = input("Enter a username for this player: ")
            if in_from_client == "quit":
                Userinterface.main_menu()
                return
            new_player = player.Player(in_from_client)
            exist_flag = False
            print(Userinterface.higescore.players)
            for p in Userinterface.higescore.players:
                if p.username == new_player.username:
                    print("Player with that name already exist!")
                    print("Type 'quit' to cancel")
                    exist_flag = True
            if not exist_flag:
                break
        Userinterface.higescore.players.append(new_player)
        # TODO: Saves higescore.players
        Userinterface.higescore.create_highscore()
        Userinterface.main_menu()

    @staticmethod
    def change_player_profil():
        """Change a player profile's username """
        the_player = Userinterface.find_player()
        old_name = the_player.username
        try:
            user = str(input("Enter the username you wish to change to: "))
        except ValueError:
            print("InputError in change_player_profil")
        player.username = user
        Userinterface.higescore.create_highscore()
        print("Username succesfully changed from " +
              f"{old_name} to {the_player.username}")
        Userinterface.main_menu()

    @staticmethod
    def input_handler_int_range(question, min_int, max_int):
        """Handles int input from user with error handling and checks if int
        is in range of min & max param, returning int inputed int.
        """
        value = None
        while True:
            try:
                value = int(input(question))
                if value in range(min_int, max_int):
                    return value
                else:
                    print(f"Input has to in range of {min_int} - {max_int}")
            except ValueError:
                print("Input has to be an integer")

    @staticmethod
    def game_ended(player_ref):
        """Method that displays that the game ended"""
        # player is ref to winner
        print(player_ref.username + " won the game!")
        Userinterface.higescore.create_highscore()
        #User_interface.higescore.create_highscore()

    @staticmethod
    def find_player():
        """Docstring"""
        the_player = None
        while the_player is None:
            try:
                user = str(input("Enter the username of your profile: "))
                for profile in Userinterface.higescore.players:
                    if profile.username.lower() == user.lower():
                        the_player = profile
                        return profile
                if the_player is None:
                    print("Player profile cannot be found. Please try again")
            except ValueError:
                print("Error in find_player")


Userinterface.start()
