if __name__ == '__main__':
    n = int(input())
    allrooms = list(map(int, input().split()))
    unique = set()
    common = set()
    for room in allrooms:
        if room in unique:
            common.add(room)
        else:
            unique.add(room)
    print(sum(unique.difference(common)))