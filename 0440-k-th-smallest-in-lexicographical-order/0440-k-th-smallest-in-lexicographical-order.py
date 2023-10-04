class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        length = len(str(n))
        answer = []
        while k > 1:

            start = 1 if not answer else 0
            cur_nth = 0
            prev = "".join(answer)

            if answer:
                k -= 1

            for num in range(start, 10):
                num_count = 0
                for nth in range(length - len(answer)):
                    top_value = int(prev + str(num + 1) + ("0" * nth))
                    if top_value <= n:
                        num_count += int(str(1) + ("0" * nth))
                    else:
                        num_count += max(-1, (n - int(prev + str(num) + ("0" * nth)))) + 1

                if cur_nth + num_count >= k:
                    answer.append(str(num))
                    k -= cur_nth
                    break
                else:
                    cur_nth += num_count

        return int("".join(answer) if answer else 1)