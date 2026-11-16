class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = []
        letters_t = []

        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        if s_list == t_list:
            return True
        else:
            return False
        
