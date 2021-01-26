def count_down(number):
    print(number)
    if number > 0:
        count_down(number - 1)


count_down(60)