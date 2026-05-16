
spy_ids = list(range(1, 21))  # IDs 1, 2, 3, ..., 20

# Add a duplicate to test detection
spy_ids.append(10)  # duplicate ID 10
print("Generated Spy IDs:", spy_ids, "\n")

# Method 1: Brute-Force Duplicate Detection
def brute_force_duplicate(ids):
    n = len(ids)
    for i in range(n):
        for j in range(i + 1, n):
            if ids[i] == ids[j]:
                return True
    return False

# Method 2: Optimized Duplicate Detection Using Sets
def set_duplicate(ids):
    seen = set()
    for id_ in ids:
        if id_ in seen:
            return True
        seen.add(id_)
    return False


print(brute_force_duplicate(spy_ids))
print(set_duplicate(spy_ids))