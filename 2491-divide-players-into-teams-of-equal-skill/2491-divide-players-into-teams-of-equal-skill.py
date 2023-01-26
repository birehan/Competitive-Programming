class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        left, right = 0, len(skill)-1
        pair_sum = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] != pair_sum:
                return -1

            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry