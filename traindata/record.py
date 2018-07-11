class Record:
    
    # P.S. all amounts normalized by dividing by init total chips
    
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
    
    # . # of unfolded opponents
    # . # of survive opponents
    # . # of all-in opponents
    # . # of raises / 
    # . # of bets
    # . # of calls
    
    ## game info
    # . game stage encoding; # of rounds / # of initial players [early if < 1, mid if < 2, late if else]
    
    def __init__(self, table_id, stage, total_bet, init_chips, max_reload):
        # table info
        self.table_id = table_id
        self.stage = stage
        
        #TODO: normalize
        self.totla_bet = total_bet
        
        #TODO: may want to combine these to total initChips for Chips bet % feautre
        self.init_chips = init_chips
        self.max_reload = max_reload
        
        # record owner info
        #self.player = 
        
        # opponent info
        self.num_of_unfolded_opponent = 0
        self.players = []
        
    def addPlayer(self, player):
        pass
        
