class Record:
    
    def __init__(self, table_id, stage, total_bet, init_chips, max_reload):
        # table info
        self.table_id = table_id
        self.stage = stage
        self.totla_bet = total_bet
        self.init_chips = init_chips
        self.max_reload = max_reload
        
        # record owner info
        #self.player = 
        
        # opponent info
        self.num_of_unfolded_opponent = 0
        self.players = []
        
    def addPlayer(self, player):
        pass
        
