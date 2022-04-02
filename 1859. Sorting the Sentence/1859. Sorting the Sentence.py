class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        for j in range(len(words)):
            for i in range(len(words)):
                smallest = int(words[i][-1])-1
                words[i], words[smallest] = words[smallest], words[i]

        original_sentence = ""
        for i in range(len(words)):
            words[i] = words[i].strip(words[i][-1])
            if i == len(words) - 1:
                original_sentence += words[i]
            else:
                original_sentence += words[i] + " "

        return original_sentence

    