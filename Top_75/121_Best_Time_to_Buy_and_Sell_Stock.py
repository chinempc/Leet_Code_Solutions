'''
    121. Best Time to Buy and Sell Stock

    Input: prices = [7,1,5,3,6,4]
    Output: 5

    Input: prices = [7,6,4,3,1]
    Output: 0

Gameplan
---------
    Two pointer method.
    Keep a left and right pointer as well as keep track of the max profit found,
    The left pointer is to find the lowest value and the right is to find the highest value between the lowest value and the end,

    left starts at index 0 and right at 1 and loop through the array as long as the right index is in the array's size.
    Check if the current right's value is greater than the current left's value
        True
            Check if the current pair is profitable by subtracting the evaluating prices[r] - prices[l]
        False
            Make left's index right's index, Right has the smallest value we found so far.
    We increment the right index either way.

'''

def solution(prices) -> int:
    l, r, maxProfit = 0, 1, 0

    while r < len(prices):
        # Check if right's value is bigger than left's
        if prices[r] > prices[l]:
            # Calculate profit and check if its bigger than the current max
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            # Right's value is the smallest number that we found so make left's value that.
            l = r
        # Increment right's index either way
        r += 1
    return maxProfit

print(solution([7,1,5,3,6,4]))  # 5
print(solution([7,6,4,3,1]))    # 0