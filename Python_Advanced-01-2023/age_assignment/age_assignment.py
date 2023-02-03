def age_assignment(*args, **kwargs):
    names = sorted(args)
    output = [f"{name} is {kwargs[name[0]]} years old." for name in names]
    return '\n'.join(output)
