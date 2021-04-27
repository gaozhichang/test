'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

执行用时: 32 ms
内存消耗: 13.1 MB
提交时间：4 分钟前
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nums.sort()
        dt = {}
        for i in range(len(nums)):
            if dt.has_key(nums[i]):
                if nums[i]*2==target:
                    return [dt[nums[i]],i]
            else:
                dt[nums[i]] = i
            
        for i in nums:
            find = target-i
            if dt.has_key(find) and dt[find]!=dt[i]:
                return dt[i],dt[find]
