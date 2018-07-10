class Player:
    
    def __init__(self, player_id, total_chips, round_bet, reload_remain, survive, folded, allin, small_blind, big_blind):
        self.player_id = player_id
        self.total_chips = total_chips
        self.round_bet = round_bet
        self.reload_remain = reload_remain
        self.survive = survive
        self.folded = folded
        self.allin = allin
        self.small_blind = small_blind
        self.big_blind = big_blind
