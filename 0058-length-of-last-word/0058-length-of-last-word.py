class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''Returns the length of the last word in a string.'''
        words = s.split()
        last_word = words[-1]
        return len(last_word)