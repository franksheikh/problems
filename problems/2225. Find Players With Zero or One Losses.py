
'''
ans[0] = not lost any matches
ans[1] = only lost one match

winners = (
1
2
10
)

losers = (
 3:2
 4:1
 6:2
 7:1
 5:1
 8:1
 9:1
)

STEPS:
winners = set
losers = map

if winner not in losers:
    add winner to winners
if loser in winners:
    remove loser from winner
else if loser not in losers:
    add loser to losers 
'''
from collections import defaultdict 
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)

        for match in matches:
            winner, loser = match
            losers[loser] -= 1

            if winner not in losers:
                losers[winner] = 0
        
        return [
            sorted([k for k,v in losers.items() if v == 0]),
            sorted([k for k,v in losers.items() if v == -1])
        ]
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)

        for match in matches:
            winner, loser = match
            
            losers[loser] += 1

            if winner not in losers:
                winners.add(winner)
            if loser in winners:
                winners.remove(loser)
        
        return [
            sorted(list(winners)),
            sorted([
                k for k,v in losers.items() if v == 1
            ])
        ]
        