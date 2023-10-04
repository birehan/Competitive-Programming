class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if k == 1:
            return 1

        length = len(str(n))
        answer = []
        count = 100
        while k > 0 and count:
            count -= 1

            start = 1 if not answer else 0
            cur_nth = 0

            if answer and k == 1:
                return int("".join(answer))

            if answer and k != 1:
                k -= 1


            for num in range(start, 10):
                
                num_count = 0
                prev = "".join(answer)
                for nth in range(length - len(answer)):
                    top_value = int(prev + str(num + 1) + str("0" * nth))
                    if top_value <= n:
                        num_count += int(str(1) + str("0") * nth)
                    else:
                        val = (n - int(prev + str(num) + str("0" * nth)))
                        if val >= 0:
                            num_count += (val + 1)

                if cur_nth + num_count >= k:
                    answer.append(str(num))
                    k -= cur_nth
                    break
                else:
                    cur_nth += num_count

        return int("".join(answer))
        # 