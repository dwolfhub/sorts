def bubble_sort(sort_me):
    for x in range(len(sort_me), 1, -1):
        for y in range(x - 1):
            if sort_me[y] > sort_me[y + 1]:
                sort_me[y], sort_me[y + 1] = sort_me[y + 1], sort_me[y]


def selection_sort(sort_me):
    for x in range(len(sort_me), 1, -1):
        i = 0
        h = sort_me[i]
        for y in range(1, x):
            if sort_me[y] > h:
                i = y
                h = sort_me[i]

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


def shell_sort(sort_me):
    pass


def merge_sort(sort_me):
    pass


def quick_sort(sort_me):
    pass
