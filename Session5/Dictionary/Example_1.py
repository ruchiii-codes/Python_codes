test_dict = {
    "Ruchi": [5, 7, 9, 4, 0],
    "is": [6, 7, 4, 3, 3],
    "Best": [9, 9, 6, 5, 5]
}

max_key = ""
max_count = 0

for key, value in test_dict.items():
    unique_count = len(set(value))   # count unique values
    
    if unique_count > max_count:
        max_count = unique_count
        max_key = key

print(max_key)