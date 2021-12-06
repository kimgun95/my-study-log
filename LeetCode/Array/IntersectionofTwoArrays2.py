from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        # intersection(교차점/교집합)을 묻는 질문
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    answer.append(nums1[i])
                    nums2[j] = -1
                    break
        return answer


s = Solution()
print(s.intersect([4,9,5], [9,4,9,8,4]))