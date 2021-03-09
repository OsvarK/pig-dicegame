from bot import Bot


class Game:
    """
    Class represents the dice game, pig.
    This class controlls the logic and the flow of the game.
    """
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def start_game(self, players):
        """Takes list of players and starts the gameloop.
        Returns false if game was not able to be created
        """
        if len(players) in range(2, 5):
            self.__game_loop(players)
            return True
        return False

    def __game_loop(self, players):
        """This function controlls the flow of the game (the game loop)
        arg (list:player): list of players
        """
        player_index = 0
        turn_cycle = 0
        while True:
            player = players[player_index]
            self.user_interface.display_whos_turn(player)
            if isinstance(player, Bot):
                points = player.get_dice_throws()
            else:
                points_accumulated = self.user_interface.\
                    throw_dice_loop(player)
                player.is_higest_score_in_one_turn(points_accumulated)
                points = points_accumulated
            player.score += points
            if player_index == (len(players) - 1):
                player_index = 0
                turn_cycle += 1
            else:
                player_index += 1
            if player.score >= 100:
                self.game_over(player, turn_cycle)
                break

    def game_over(self, player, turn_cycle):
        """Fucntion to end the gameloop and declares a winner.
            arg1 (Player): the winner of the game.
            arg2 (int): on what turn cycle the game was ended.
        """
        self.user_interface.game_ended(player)
        player.i_win(turn_cycle)
