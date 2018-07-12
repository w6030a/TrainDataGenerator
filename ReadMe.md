# Train Data Generator
 
    # P.S. all amounts normalized by dividing by init chips (without reload)
    
    ## table info
    -# . round stage encoding [deal, flop, turn, river]
    -# . total bet on table
    -# . # of raises
    -# . # of bets
	-# . small blind
	-# . big blind
	
    ## record owner info
    -# . current chips in hand
	-# . total round bet
	-# . current bet
    -# . remaining chips (hand + reloads)
    -# . action encoding [call, bet, raise, allin, fold]
     # . hand score
    
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
    
    -# . # of unfolded opponents
    -# . # of survive opponents
    -# . # of all-in opponents
    -# . # of online opponents
    
    ## game info
    -# . game stage encoding; # of rounds / # of initial players [early if < 1, mid if < 2, late if else]
	
	## reward
	-# . reward: [0] if record owner folded (to avoid punishing folding by assigning all folds with a negative reward),
	#            otherwise [money win for the round] - [current total past bet in the round] - [current bet]
    
