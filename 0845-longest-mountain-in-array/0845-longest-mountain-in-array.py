class Solution(object):
    def longestMountain(self, arr):
        n=len(arr)
        max_len=0
        for i in range (1,len(arr)-1):
            if arr[i-1]< arr[i]> arr[i+1]:
                left=i
                right=i
                while left>0 and arr[left-1]< arr[left]:
                   left -=1
                while right< len(arr)-1 and  arr[right]> arr[right+1]:
                   right +=1
                max_len=max(max_len,right-left+1)
        return max_len

        