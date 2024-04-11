class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_height = 0
        max_index = 0

        for i in range(1, len(arr)-1):
            if (arr[i-1] < arr[i] > arr[i+1]) and arr[i] > max_height:
                max_height = arr[i]
                max_index = i


        return max_index