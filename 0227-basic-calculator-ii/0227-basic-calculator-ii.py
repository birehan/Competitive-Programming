class Solution:
    def calculate(self, s: str) -> int:
        nums = []
        ops = []
        s = list(s.replace(" ", ""))
        index = 0


        while index < len(s):
            if s[index].isnumeric():
                cur_num = [s[index]]
                while index+1 < len(s) and s[index+1].isnumeric():
                    cur_num.append(s[index+1])
                    index += 1
                cur_num = int("".join(cur_num))

                if ops and ops[-1] == "*":
                    nums[-1] *= cur_num
                    ops.pop()
                elif ops and ops[-1] == "/":
                    nums[-1] = nums[-1]//cur_num
                    ops.pop()
                else:
                    nums.append(cur_num)

            else: ops.append(s[index])

            index += 1


        op_ind = 0
        num_ind = 0
        while op_ind < len(ops):
            if ops[op_ind] == "+":
                nums[num_ind+1] += nums[num_ind]
            else:
                nums[num_ind+1] = nums[num_ind] - nums[num_ind + 1]
            
            op_ind += 1
            num_ind += 1
        
        return nums[-1]



        