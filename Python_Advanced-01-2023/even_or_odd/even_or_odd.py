def even_odd(*args):
    numbers = []

    if args[-1] == 'even':
        check = 0
    else:
        check = 1

    for n in args[:-1]:
        if n % 2 == check:
            numbers.append(n)

    return numbers
