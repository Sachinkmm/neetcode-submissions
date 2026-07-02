class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n2 < n1:
            return self.findMedianSortedArrays(nums2, nums1)

        total = n1 + n2
        half = (total + 1) // 2
        
        l = 0
        r = n1
        while l <= r:
            mid1 = (l + r) // 2
            mid2 = half - mid1
            l1 = nums1[mid1-1] if mid1-1 >= 0 else float("-infinity")
            r1 = nums1[mid1] if mid1 < n1 else float("infinity")
            l2 = nums2[mid2-1] if mid2-1 >= 0 else float("-infinity")
            r2 = nums2[mid2] if mid2 < n2 else float("infinity")

            if l1 <= r2 and l2 <= r1:
                if total % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1
        return 0