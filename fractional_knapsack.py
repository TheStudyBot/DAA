# Hardcoded weights and values
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

# Calculate value/weight ratio
ratio = [values[i] / weights[i] for i in range(3)]

# Sort items by ratio (descending)
for i in range(3):
    for j in range(i + 1, 3):
        if ratio[i] < ratio[j]:
            ratio[i], ratio[j] = ratio[j], ratio[i]
            weights[i], weights[j] = weights[j], weights[i]
            values[i], values[j] = values[j], values[i]

profit = 0

# Fill the knapsack
for i in range(3):
    if weights[i] <= capacity:
        profit += values[i]
        capacity -= weights[i]
    else:
        profit += ratio[i] * capacity
        break

print("Maximum Profit:", profit)