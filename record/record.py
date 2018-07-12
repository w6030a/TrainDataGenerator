class Record:
    
    # P.S. all amounts normalized by dividing by init chips (without reload)
    
    ## table info
    # . round stage encoding [preflop, flop, river...]
    # . total bet on table
    
    ## record owner info
    # . current bet
    # . current chips in hand
    # . remaining chips (hand + reloads)
    # . action encoding [call, bet, raise, allin, fold]
    # . action amount
    
    ## opponent info
    # . richest unfolded opponent's chips in hand
    # . richest unfolded opponent's remaining chips (hand + reloads)
    # . poorest unfolded opponent's chips in hand
    # . poorest unfolded opponent's remaining chips (hand + reloads)
    # . avg. of unfolded opponents' chips in hand
    # . avg. of unfolded opponents' remaining chips (hand + reloads)
    # . richest unfolded most aggressive(most raise) opponent's chips in hand
    # . richest unfolded most defensive(most call) opponent's remaining chips (hand + reloads)
    # . poorest unfolded most aggressive(most raise) opponent's chips in hand
    # . poorest unfolded most defensive(most call) opponent's remaining chips (hand + reloads)
    
    # . # of unfolded players
    # . # of survive players
    # . # of all-in opponents
    # . # of raises / 
    # . # of bets
    # . # of calls
    
    ## game info
    # . game stage encoding; # of rounds / # of initial players [early if < 1, mid if < 2, late if else]
    
    def __init__(self):
        pass
        
    def set_table_info(self, table_info):
        self.table_id = table_info['tableNumber']
        self.stage = table_info['roundName']
        self.round_count = table_info['roundCount']
        self.raise_count = table_info['raiseCount']
        self.bet_count = table_info['betCount']
        self.total_bet = table_info['totalBet']
        self.init_chips = table_info['initChips']
        self.max_reload_count = table_info['maxReloadCount']
        self.board_card = table_info['board']
        self.small_blind = table_info['smallBlind']
        self.big_blind = table_info['bigBlind']
        
    def set_player_info(self, player_info):
        for player in player_info:
            if self.player_name == player['playerName']:
                self.chips = player['chips']
                self.folded = player['folded']
                self.allin = player['allIn']
                self.cards = player['cards']
                self.is_survive = player['isSurvive']
                self.reload_count = player['reloadCount']
                self.round_bet = player['roundBet']
                self.bet = player['bet']
                self.isOnline = player['isOnline']
                self.isHuman = player['isHuman']

    def set_action_info(self, action_info):
        self.action = action_info['action']
        self.player_name = action_info['playerName']
        self.chips = action_info['chips']
        
        if 'amount' not in action_info:
            self.amount = 0
        else:
            self.amount = action_info['amount']
        
    def get_table_id(self):
        return self.table_id
    
    def get_player_info(self):
        return self.player_info
    
    def get_player_name(self):
        return self.player_name
    
    def set_reward(self, reward):
        self.reward = reward
        