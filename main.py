def letterPos(w, y):
    y == 0
    for i in range(0, len(w)):
        if w[i] == y:
            y == (y + 1)
    return y
    return False
print (letterPos("rat", "r"))