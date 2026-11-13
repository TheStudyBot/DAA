import random

# Quick Sort
def quick_sort(a, low, high, randomized, count):

    if low < high:

        # Randomized pivot
        if randomized:
            p = random.randint(low, high)
            a[p], a[high] = a[high], a[p]

        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            count[0] += 1

            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i+1], a[high] = a[high], a[i+1]
        p = i + 1

        quick_sort(a, low, p-1, randomized, count)
        quick_sort(a, p+1, high, randomized, count)


# Same input for both
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = a1.copy()

c1 = [0]
c2 = [0]

# Deterministic Quick Sort
quick_sort(a1, 0, len(a1)-1, False, c1)

# Randomized Quick Sort
random.seed(1)
quick_sort(a2, 0, len(a2)-1, True, c2)

print("Deterministic Quick Sort:")
print(a1)
print("Comparisons:", c1[0])

print("\nRandomized Quick Sort:")
print(a2)
print("Comparisons:", c2[0])