'''
122. Best Time to Buy and Sell Stock II



    Input: prices = [7,1,5,3,6,4]
    Output: 7

    Input: prices = [1,2,3,4,5]
    Output: 4

    Input: prices = [7,6,4,3,1]
    Output: 0

    Input: prices = [1,2,3,4,5]
    Output: 4
'''

def solution(prices) -> int:
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i-1]
    return profit

print(solution([7,1,5,3,6,4]))  # 7
print(solution([1,2,3,4,5]))    # 4
print(solution([7,6,4,3,1]))    # 0
print(solution([1,2,3,4,5]))    # 4