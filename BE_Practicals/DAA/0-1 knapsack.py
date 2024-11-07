# 4. Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.

# 1. DP solution
# Function to solve 0-1 Knapsack problem using Dynamic Programming
def knapsack_dp(weights, values, capacity):
    n = len(values)
    # Create a DP table with size (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Either include the item or exclude it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    # Return the maximum value for the given capacity
    return dp[n][capacity]

# Driver code
if __name__ == "__main__":
    # Take inputs from the user
    n = int(input("Enter the number of items: "))
    values = list(map(int, input("Enter the values of the items separated by spaces: ").split()))
    weights = list(map(int, input("Enter the weights of the items separated by spaces: ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Calculate the maximum value
    max_value = knapsack_dp(weights, values, capacity)
    print(f"Maximum value in knapsack = {max_value}")
