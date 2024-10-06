def loop_practice(height):
    length = height * 2 - 1
    stars = 1
    for i in range(1, height + 1):
        print(("*" * stars).center(length))
        stars += 2
    print("*".center(length))
loop_practice(5)