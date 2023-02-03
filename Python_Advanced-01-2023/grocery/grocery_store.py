def grocery_store(**kwargs):
    shopping_list = sorted(kwargs.items(), key=lambda x: x[0])
    shopping_list = sorted(shopping_list, key=lambda x: -len(x[0]))
    shopping_list = sorted(shopping_list, key=lambda x: -x[1])
    output = [f"{x}: {y}" for x, y in shopping_list]
    return '\n'.join(output)
