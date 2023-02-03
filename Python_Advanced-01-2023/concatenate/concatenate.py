def concatenate(*args, **kwargs):
    string = ''.join(args)
    for k, v in kwargs.items():
        string = string.replace(k, v)
    return string
