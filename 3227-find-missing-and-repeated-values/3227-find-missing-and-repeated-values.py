class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid) 
        lst = [num for row in grid for num in row]
        sum_n = n**2 * (n**2 + 1) // 2
        sum_squares = n**2 * (n**2 + 1) * (2 * n**2 + 1) // 6
        grid_sum = sum(lst)
        grid_sum_squares = sum(num * num for num in lst)
        diff_sum = grid_sum - sum_n  
        diff_sum_squares = grid_sum_squares - sum_squares
        sum_ab = diff_sum_squares // diff_sum  
        a = (diff_sum + sum_ab) // 2
        b = (sum_ab - diff_sum) // 2
        return [a, b]