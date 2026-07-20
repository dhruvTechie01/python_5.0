         # algorithms
       
# Socho tumhare paas 8 cards hain:
# [38, 27, 43, 3, 9, 82, 10, 19]
# Merge Sort ka rule:
# Array ko baar-baar 2 parts mein divide karo.
# Jab ek-ek element bach jaye, divide karna band karo.
# Phir sorted order mein merge karte jao.
# Step 1: Divide
# [38, 27, 43, 3, 9, 82, 10, 19]

#           ↓

# [38, 27, 43, 3]      [9, 82, 10, 19]

#           ↓

# [38, 27] [43, 3]     [9, 82] [10, 19]

#           ↓

# [38] [27] [43] [3] [9] [82] [10] [19]
# Ab sab single elements hain.
# Step 2: Merge (Sort karte hue)
# Merge 38 and 27
# [38] [27]

# ↓

# [27, 38]
# Merge 43 and 3
# [43] [3]

# ↓

# [3, 43]
# Merge 9 and 82
# [9] [82]

# ↓

# [9, 82]
# Merge 10 and 19
# [10] [19]

# ↓

# [10, 19]
# Step 3: Merge Bigger Arrays
# [27, 38] + [3, 43]

# ↓

# [3, 27, 38, 43]
# [9, 82] + [10, 19]

# ↓

# [9, 10, 19, 82]
# Step 4: Final Merge
# [3, 27, 38, 43]
# [9, 10, 19, 82]

# ↓

# [3, 9, 10, 19, 27, 38, 43, 82]
# # 

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10, 19]

merge_sort(arr)

print(arr)