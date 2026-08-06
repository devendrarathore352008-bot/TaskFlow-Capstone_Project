def insertion_sort(records, key):

    for i in range(1, len(records)):

        current = records[i]

        j = i - 1

        while j >= 0 and records[j][key] > current[key]:
            records[j + 1] = records[j]
            j -= 1

        records[j + 1] = current

def insertion_sort_count(records, key):

    comparison_count = 0

    for i in range(1, len(records)):

        current = records[i]

        j = i - 1

        while j >= 0:

            comparison_count += 1

            if records[j][key] > current[key]:
                records[j + 1] = records[j]
                j -= 1
            else:
                break

        records[j + 1] = current

    return comparison_count