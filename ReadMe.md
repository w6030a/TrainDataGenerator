# Train Data Generator
 
    # P.S. all amounts normalized by dividing by init chips (without reload)
    # Total of 55 features
    
	## record owner info
    #     0. current chips in hand
	#     1. total round bet
	#     2. current bet
    #     3. remaining chips (hand + reloads)
    #   4-9. action encoding [call, bet, raise, allin, fold, check]
	#    10. is small blind
	#    11. is big blind
    #    12. hand score (chen formula score)
	# 13-22. set possibilities (only calculated for Flop, Turn, and River stages)
	                           [High Card, Pair, Two Pair, Three of a Kind, Straight,
							    Flush, Full House, Four of a Kind, Straight Flush, Royal Flush]
	#    23. win possibility against any other hand (only calculated for Turn and River stages)

    ## table info
    # 24-27. round stage encoding [Deal, Flop, Turn, River]
    #    28. total bet on table
    #    29. num of raises from all players
    #    30. num of bets from all players
	#    31. small blind amount
	#    32. big blind amount
	
    ## opponent info
	#    33. most raise count from one unfolded opponent
	#    34. most amount raised
	#    35. most portion raised: most amount raised / owners chips in hand
	#    36. most amount bet
	#    37. most portion bet: most round bet / owners chips in hand
	#    37. # of unfolded opponent raise count = 1
	#    38. # of unfolded opponent raise count = 2
	#    40. # of unfolded opponent raise count = 3
	#    41. # of unfolded opponent raise count = 4
	#    42. # of unfolded opponent raise count >= 5
    #    43. # of unfolded opponent call count = 1
	#    44. # of unfolded opponent call count = 2
	#    45. # of unfolded opponent call count = 3
	#    46. # of unfolded opponent call count >= 4
    #    47. # of unfolded opponents
    #    48. # of survive opponents
    #    49. # of all-in opponents
    #    50. # of online opponents
    
    ## game info
    #  51-53. game stage encoding; # of rounds / # of initial players [early if < 1, mid if < 2, late if else]
	
	## reward
	#     54. reward: [0] if record owner folded (to avoid punishing folding by assigning all folds with a negative reward),
	#                 otherwise [money win for the round] - [current total past bet in the round] - [current bet]
    
