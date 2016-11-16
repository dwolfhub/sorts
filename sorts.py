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


def shell_sort(sort_me: list):
    sm_len = len(sort_me)

    # determine optimal gaps
    max_gap = sm_len // 2
    k = 1
    l = 2
    gaps = []
    while k < max_gap:
        gaps.append(k)
        k = pow(l, 2) - 1
        l += 1

    for gap in gaps:
        for i in range(gap):
            subset = []
            j = i
            while j < sm_len:
                subset.append(sort_me[j])
                j += gap
            insertion_sort(subset)
            while i < sm_len:
                sort_me.pop(i)
                sort_me.insert(i, subset.pop(0))
                i += gap


def merge_sort(sort_me):
    pass


def quick_sort(sort_me):
    pass
