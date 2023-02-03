def even_odd_filter(**kwargs):
    filtered_values = {}

    for key, values in kwargs.items():
        filtered_values[key] = []

        if key == 'odd':
            check = 1
        else:
            check = 0

        for num in values:
            if num % 2 == check:
                filtered_values[key].append(num)

    filtered_values = dict(sorted(filtered_values.items(), key=lambda x: -len(x[1])))
    return filtered_values
