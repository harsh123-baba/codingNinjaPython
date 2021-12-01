def towerofBramha(n, a, b, c):
    if n==1:
        print("Move 1st disk from ", a, " to ", c)
        return

    towerofBramha(n-1, a, c, b)
    print("Move ", n, "th disk from ", a , " to ", c)
    towerofBramha(n-1, b, a, c)

towerofBramha(3, "s", "h", "d")