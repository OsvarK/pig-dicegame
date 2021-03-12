import highscore
import player
import bot
import game


class UserInterface():
    """
    This class controlls the input and output to the player.
    """

    # Ref to highscore class
    highscore = highscore.Highscore()

    @staticmethod
    def start():
        """Start of program"""
        UserInterface.highscore = highscore.Highscore()
        UserInterface.highscore.create_players()
        UserInterface.main_menu()

    @staticmethod
    def game_setup_menu():
        """Set up the game, how many players and how many bots
        and then adds them to a list"""
        players = []
        for i in range(UserInterface.input_handler_int_range(
            "Enter the number of PLAYERS (min 1, max 4) you'd like to play " +
            "with: ", 1, 4)):
            print(f"For player {i} --------------------------------------------")
            players.append(UserInterface.find_player())
        bots = range(UserInterface.input_handler_int_range(
            "Enter the number of BOTS (min 1, max 4) you'd like to play " +
            "against: ", 1, 4))

        for i in bots:
            players.append(bot.Bot(None, UserInterface.input_handler_int_range(
                f"Enter the risk factor bot [{i}] (1 - 5)," +
                "the lower the number equals less risk ", 1, 5)))
        new_game = game.Game(UserInterface)
        new_game.start_game(players)

    @staticmethod
    def main_menu():
        """---Main Menu---"""
        option = UserInterface.input_handler_int_range(
            "1. Play game \n" +
            "2. Create player profile \n" +
            "3. Change player profile \n" +
            "4. See highscore \n" +
            "5. Exit \n",
            1, 5
        )
        if option == 1:
            UserInterface.game_setup_menu()
        elif option == 2:
            UserInterface.create_player_profile()
        elif option == 3:
            UserInterface.change_player_profil()
        elif option == 4:
            UserInterface.highscore.show_highscore()
            UserInterface.main_menu()
        elif option == 5:
            UserInterface.highscore.create_highscore()
            quit()

    @staticmethod
    def throw_dice_loop(player_ref):
        """
        This function controlls the flow of the dice loop,
        the players ability to throw dices.
        """
        choice = ""
        points_accumulated = 0
        while choice.upper() != "N":
            choice = UserInterface.throw_dice_input()
            if choice.upper() == "Y":
                dice_result = player_ref.throw_dice()
                if dice_result == 1:
                    print("You rolled a 1. You lost your score" +
                          " and it's the next players turn")
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
                if user_input.upper() == "Y" or user_input.upper() == "N":
                    return user_input
                print("Enter Y to throw the dice or N to hold")
            except ValueError:
                print("You need to enter Y or N")

    @staticmethod
    def display_whos_turn(player_ref):
        """Display whose turn it is"""
        print("New turn: " + player_ref.username)

    @staticmethod
    def create_player_profile():
        """Creates a player profile"""
        while True:
            in_from_client = input("Enter a username for this player: ")
            if in_from_client == "quit":
                UserInterface.main_menu()
                return
            new_player = player.Player(in_from_client)
            exist_flag = False
            for p in UserInterface.highscore.players:
                if p.username == new_player.username:
                    print("Player with that name already exist!")
                    print("Type 'quit' to cancel")
                    exist_flag = True
            if not exist_flag:
                break
        UserInterface.highscore.players.append(new_player)
        UserInterface.highscore.create_highscore()
        UserInterface.main_menu()

    @staticmethod
    def change_player_profil():
        """Change a player profile's username """
        the_player = UserInterface.find_player()
        old_name = the_player.username
        try:
            user = str(input("Enter the username you wish to change to: "))
        except ValueError:
            print("InputError in change_player_profile")
        the_player.username = user
        UserInterface.highscore.create_highscore()
        print("Username successfully changed from " +
              f"{old_name} to {the_player.username}")
        UserInterface.main_menu()

    @staticmethod
    def input_handler_int_range(question, min_int, max_int):
        """Handles int input from user with error handling and checks if int
        is in range of min & max param, returning int inputed int.
        """
        value = None
        while True:
            try:
                value = int(input(question))
                if value in range(min_int, max_int + 1):
                    return value
                else:
                    print(
                        f"Input has to be in range of ({min_int} - {max_int})")
            except ValueError as ex:
                print("Input has to be an integer")
                raise ValueError from ex

    @staticmethod
    def game_ended(player_ref):
        """Method that displays that the game ended"""
        print(player_ref.username + " won the game!")
        UserInterface.highscore.create_highscore()

    @staticmethod
    def find_player():
        """Docstring"""
        the_player = None
        while the_player is None:
            try:
                user = str(input("Enter the username of your profile: "))
                for profile in UserInterface.highscore.players:
                    if profile.username.lower() == user.lower():
                        the_player = profile
                        return profile
                if the_player is None:
                    print("Player profile cannot be found. Please try again")
            except ValueError:
                print("Error in find_player")
