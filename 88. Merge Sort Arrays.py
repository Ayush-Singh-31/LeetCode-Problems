'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)

'''
List are passed by reference, so we can modify the list in place. We start from the end of the list and compare the elements of the two lists. We start from the end because we are sure that the end of the list is empty. We compare the last element of the two lists and put the greater element at the end of the list. We decrement the index of the list from which we took the element. We repeat the process until we have compared all the elements of the two lists. If there are elements left in the second list, we put them at the beginning of the first list. The time complexity of the solution is O(n + m) where n is the length of the first list and m is the length of the second list. The space complexity of the solution is O(1) because we are modifying the input list in place. The solution is optimal because we are using the input list to store the result and we are not using any extra space. The solution is also optimal in terms of time complexity because we are comparing the elements of the two lists only once and putting the elements in the correct position in the first list.
'''