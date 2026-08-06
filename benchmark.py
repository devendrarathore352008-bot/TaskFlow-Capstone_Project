from backend.app.algorithms.sorting import insertion_sort_count
from backend.app.algorithms.searching import (
    linear_search_count,
    binary_search_count,
)

def generate_records(size):
    records = []

    for i in range(size):
        records.append({
            "title": f"Task {i:04d}",
            "priority": "medium",
            "due_date": "tomorrow"
        })

    return records


sizes = [10, 500, 3000]

for size in sizes:

    records = generate_records(size)

    sort_records = [record.copy() for record in records]

    sort_count = insertion_sort_count(sort_records, "title")

    linear_result = linear_search_count(records, f"Task {size-1:04d}", "title")

    binary_result = binary_search_count(sort_records, f"Task {size-1:04d}", "title")

    print(f"\nData Size: {size}")
    print(f"Insertion Sort Comparisons: {sort_count}")
    print(f"Linear Search Comparisons: {linear_result['comparison_count']}")
    print(f"Binary Search Comparisons: {binary_result['comparison_count']}")