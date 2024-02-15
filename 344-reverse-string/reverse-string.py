class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(self,i,j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

        l,r = 0, len(s)-1
        while l <=r:
            swap(s,l,r)
            l += 1
            r -= 1
        return s
        
        