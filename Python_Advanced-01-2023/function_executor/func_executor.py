def func_executor(*args):
    output = []

    for func, data in args:
        output.append(f"{func.__name__} - {func(*data)}")

    return '\n'.join(output)
