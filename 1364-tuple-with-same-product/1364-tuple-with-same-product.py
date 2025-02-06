class Solution:
    def tupleSameProduct(self, nums):
        product_count = defaultdict(int)
        n = len(nums)

        # Step 1: Count the frequency of each product of pairs
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Step 2: Calculate the number of valid tuples
        result = 0
        for count in product_count.values():
            if count > 1:
                result += count * (count - 1) * 4  # Each pair contributes 8 tuples

        return result