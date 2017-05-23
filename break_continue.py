def app():
    #0: affiche 0, 1, 2, 3
    for i in range(0, 10):
        if (i == 4):
            break

        print(i)

    """
    #1: 1, 2 et 3 sont équivalents
    print('\n')
    for i in range(0, 10):
        if (i == 4):
            continue

        j = process(i)
        if (j == 0):
            continue

        print(j)

    #2: 1, 2 et 3 sont équivalents
    print('\n')
    for i in range(0, 10):
        if (i == 4):
            pass
        else:
            j = process(i)
            if (j == 0):
                pass
            else:
                print(j)

    #3: 1, 2 et 3 sont équivalents
    print('\n')
    for i in range(0, 10):
        if (i != 4):
            j = process(i)
            if (j != 0):
                print(j)
    """

    #4: affiche 0, 1, 2, 3, 5, 6, 7, 8, 9
    print('\n')
    for i in range(0, 10):
        if (i == 4):
            continue

        print(i)

    #5: affiche 0, 1, 2, 3 mais pas "c'est la fin"
    print('\n')
    for i in range(0, 10):
        if (i == 4):
            return

        print(i)
    print("c'est la fin")

if __name__ == "__main__":
    app()
