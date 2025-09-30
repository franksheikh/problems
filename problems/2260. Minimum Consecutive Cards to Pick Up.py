class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        o = defaultdict(int)
        min_pickups = inf

        for i,card in enumerate(cards):
            if card in o:
                min_pickups = min(min_pickups, i - o[card] + 1)
            o[card] = i
        
        return -1 if min_pickups == inf else min_pickups
