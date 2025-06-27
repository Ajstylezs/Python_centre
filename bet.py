# BET COINS
#Bets are placed by the players
class BETS:
    def __init__(self):
        self.p = {}
    def place_your_bet(self):
        for bet in range(1,3+1):
            player_bet= input(f"Please place your bet player{bet} : \n$")
            plays = {"player1":bet}
            self.p[f"player{bet}"]=player_bet

