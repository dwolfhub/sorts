def bubble_sort(sort_me):
    for x in range(len(sort_me), 1, -1):
        for y in range(x - 1):
            if sort_me[y] > sort_me[y + 1]:
                sort_me[y], sort_me[y + 1] = sort_me[y + 1], sort_me[y]


def selection_sort(sort_me):
    for x in range(len(sort_me), 1, -1):
        i = 0
        high = sort_me[i]
        for y in range(1, x):
            if sort_me[y] > high:
                i = y
                high = sort_me[i]

        sort_me[y], sort_me[i] = sort_me[i], sort_me[y]


def insertion_sort(sort_me):
    for x in range(1, len(sort_me)):
        z = sort_me.pop(x)
        inserted = False
        for y in range(x):
            if sort_me[y] > z:
                sort_me.insert(y, z)
                inserted = True
                break
        if not inserted:
            sort_me.insert(x, z)


def shell_sort(sort_me: list):
    list_len = len(sort_me)

    # determine optimal gaps (uses 2 ^ k - 1 formula)
    max_gap = list_len // 2
    gap = 1
    k = 2
    gaps = []
    while gap < max_gap:
        gaps.append(gap)
        gap = pow(2, k) - 1
        k += 1

    for gap in reversed(gaps):
        # using each gap..
        for start_of_subset in range(gap):
            # insertion sort each subset
            current_sort_item_index = start_of_subset + gap
            while current_sort_item_index < list_len:
                current_sort_item_value = sort_me[current_sort_item_index]
                working_index = start_of_subset
                while working_index < current_sort_item_index:
                    if current_sort_item_value < sort_me[working_index]:
                        current_sort_item_value, sort_me[working_index] = \
                            sort_me[working_index], current_sort_item_value
                    working_index += gap

                sort_me[working_index] = current_sort_item_value
                current_sort_item_index += gap


def merge_sort(sort_me):
    pass


def quick_sort(sort_me):
    pass
