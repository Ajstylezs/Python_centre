class Player:
    def __init__(self):
        self.player_list = []
    def players_involved (self):
        no_of_players = input("how many players are playing which is inclusive of the dealer : \n")
        length_player = int(no_of_players)
        for no in range(length_player):
            if no == 0:
                no = "dealer"
                self.player_list.append(no)
            else:
                enter_players_name = input()
                self.player_list.append(enter_players_name)


    # def shuffle():
