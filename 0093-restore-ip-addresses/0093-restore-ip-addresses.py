class Solution:
  def helper(self, cur, index, s):
    if index == len(s) and len(cur) == 4:
      self.answer.append(".".join(cur.copy()))
    
    if len(cur) >= 4:
      return
    
    num  = ""
    for i in range(index, index+3):
      if i >= len(s):
        break
      
      num += s[i]

      if (len(num) > 1 and num[0] == '0') or int(num) > 255:
        break

      cur.append(num)
      self.helper(cur, i + 1, s)
      cur.pop()


  def restoreIpAddresses(self, s: str) -> List[str]:
    self.answer = []
    self.helper([], 0, s)
    return self.answer