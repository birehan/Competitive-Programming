from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 1
        counter = right
        count = 1
        while right < len(chars):
            if chars[left] == chars[right]:
                count += 1
                c = count
                co = counter
                x = [int(a) for a in str(c)]

                for i in x:
                    chars[co] = str(i)
                    co += 1

                if count > 2 and right >= co:
                    chars.pop(right)
                else:
                    right += 1
            else:
                left = right
                right += 1
                counter = right
                count = 1

        return len(chars)