# Train Data Generator
 
    # P.S. all amounts normalized by dividing by init chips (without reload)
    
    ## table info
    # . round stage encoding [deal, flop, turn, river]
    # . total bet on table
    # . # of raises from all players
    # . # of bets from all players
	# . small blind amount
	# . big blind amount
	
    ## record owner info
    # . current chips in hand
	# . total round bet
	# . current bet
    # . remaining chips (hand + reloads)
    # . action encoding [call, bet, raise, allin, fold]
	# . is small blind
	# . is big blind
    X# . hand score
	X# . set score
    
    ## opponent info
	# . most raise count from one unfolded opponent
	# . most amount raised
	# . most portion raised: most amount raised / owners chips in hand
	# . most amount bet
	# . most portion bet: most round bet / owners chips in hand
	# . # of unfolded opponent raise count = 1
	# . # of unfolded opponent raise count = 2
	# . # of unfolded opponent raise count = 3
	# . # of unfolded opponent raise count = 4
	# . # of unfolded opponent raise count >= 5
    # . # of unfolded opponent call count = 1
	# . # of unfolded opponent call count = 2
	# . # of unfolded opponent call count = 3
	# . # of unfolded opponent call count >= 4
    
    # . # of unfolded opponents
    # . # of survive opponents
    # . # of all-in opponents
    # . # of online opponents
    
    ## game info
    # . game stage encoding; # of rounds / # of initial players [early if < 1, mid if < 2, late if else]
	
	## reward
	# . reward: [0] if record owner folded (to avoid punishing folding by assigning all folds with a negative reward),
	#            otherwise [money win for the round] - [current total past bet in the round] - [current bet]
    
