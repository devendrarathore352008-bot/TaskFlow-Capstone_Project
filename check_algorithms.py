from backend.app.algorithms.sorting import insertion_sort, insertion_sort_count
from backend.app.algorithms.searching import (
    linear_search,
    binary_search,
    linear_search_count,
    binary_search_count,
)


def check(case_name, result, expected):
    if result == expected:
        print(f"PASS: {case_name}")
    else:
        print(f"FAIL: {case_name} - expected {expected}, got {result}")


# 1. Empty list
records = []
insertion_sort(records, "title")
check("Insertion Sort - Empty List", records, [])

# 2. Single element
records = [{"title": "Task A"}]
insertion_sort(records, "title")
check("Insertion Sort - Single Element", records, [{"title": "Task A"}])

# 3. Binary search (first, middle, last)
records = [
    {"title": "A"},
    {"title": "B"},
    {"title": "C"},
]

check("Binary Search - First", binary_search(records, "A", "title"), 0)
check("Binary Search - Middle", binary_search(records, "B", "title"), 1)
check("Binary Search - Last", binary_search(records, "C", "title"), 2)

# 4. Binary search not found
check("Binary Search - Not Found", binary_search(records, "X", "title"), -1)

# 5. insertion_sort_count
records = [
    {"title": "C"},
    {"title": "A"},
    {"title": "B"},
]
count = insertion_sort_count(records, "title")
check("Insertion Sort Count Type", type(count), int)
check("Insertion Sort Count > 0", count > 0, True)

# 6. binary_search_count
result = binary_search_count(records, "B", "title")
check("Binary Search Count Index", result["index"], 1)
check("Binary Search Count > 0", result["comparison_count"] > 0, True)

# 7. linear_search_count
result = linear_search_count(records, "X", "title")
check("Linear Search Not Found", result["index"], -1)
check(
    "Linear Search Comparison Count",
    result["comparison_count"],
    len(records),
)