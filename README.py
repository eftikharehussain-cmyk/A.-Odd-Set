# A.-Odd-Set
for _ in range(int(input())):
    n = int(input())
    lst = [x for x in map(int, input().split())]
    cnt1 = 0
    cnt2 = 0
    for i in lst:
        if i % 2 == 0:
            cnt1 += 1
        else:
            cnt2 += 1
    print("YES" if cnt1 == cnt2 == n else "NO")

