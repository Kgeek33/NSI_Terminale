def renverser(lst: list | None) -> list | None:
    if lst == None:
        return None

    nvLst = []
    for i in range(len(lst) - 1, -1, -1):
        nvLst.append(lst[i])

    return nvLst


assert renverser(None) == None
assert renverser([30]) == [30]
assert renverser([3, 6, 9, 100]) == [100, 9, 6, 3]
