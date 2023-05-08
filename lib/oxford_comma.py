def oxford_comma(items):
    while items:
        if len(items) == 2:
            return " and ".join(items)
        else:
            return ", ".join(items[:-2] + [", and ".join(items[-2:])])
