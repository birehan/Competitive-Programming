class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p_ind = t_ind = 0
        pairs = 0

        while p_ind < len(players) and t_ind < len(trainers):
            if players[p_ind] <= trainers[t_ind]:
                pairs += 1
                p_ind += 1
            t_ind += 1
        
        return pairs