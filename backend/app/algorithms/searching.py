def linear_search(records, target_value, key):

    for index, record in enumerate(records):
        if record[key] == target_value:
            return index

    return -1


def binary_search(sorted_records, target_value, key):

    low = 0
    high = len(sorted_records) - 1

    while low <= high:

        mid = (low + high) // 2

        if sorted_records[mid][key] == target_value:
            return mid

        elif sorted_records[mid][key] < target_value:
            low = mid + 1

        else:
            high = mid - 1

    return -1

def linear_search_count(records, target_value, key):

    comparison_count = 0

    for index, record in enumerate(records):

        comparison_count += 1

        if record[key] == target_value:
            return {
                "index": index,
                "comparison_count": comparison_count
            }

    return {
        "index": -1,
        "comparison_count": comparison_count
    }


def binary_search_count(sorted_records, target_value, key):

    low = 0
    high = len(sorted_records) - 1

    comparison_count = 0

    while low <= high:

        comparison_count += 1

        mid = (low + high) // 2

        if sorted_records[mid][key] == target_value:
            return {
                "index": mid,
                "comparison_count": comparison_count
            }

        elif sorted_records[mid][key] < target_value:
            low = mid + 1

        else:
            high = mid - 1

    return {
        "index": -1,
        "comparison_count": comparison_count
    }