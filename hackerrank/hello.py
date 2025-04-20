import time

def slice_delete(s, i):
    return s[:i] + s[i+1:]

def pointer_delete(s, i):
    # Simulate skipping one character
    result = []
    for idx, c in enumerate(s):
        if idx != i:
            result.append(c)
    return ''.join(result)

sizes = [10, 100, 1000, 10000, 100000]  # different string sizes
delete_index = 5  # arbitrary position to delete

print(f"{'Size':>10} | {'Slice Time (s)':>15} | {'Pointer Time (s)':>17}")
print("-" * 50)

for size in sizes:
    s = "a" * size
    
    # Time slicing
    start = time.perf_counter()
    _ = slice_delete(s, delete_index)
    slice_time = time.perf_counter() - start
    
    # Time pointer method
    start = time.perf_counter()
    _ = pointer_delete(s, delete_index)
    pointer_time = time.perf_counter() - start

    print(f"{size:10} | {slice_time:15.8f} | {pointer_time:17.8f}")
