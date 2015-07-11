def make_order_list(list_in):
    order_list = []
    for item in list_in:
        if item not in order_list:
            order_list.append(item)
    return order_list


def group_ordered(list_in):
    if list_in is None:
        return None
    order_list = make_order_list(list_in)
    current = 0
    for item in order_list:
        search = current + 1
        while True:
            try:
                if list_in[search] != item:
                    search += 1
                else:
                    current += 1
                    list_in[current], list_in[search] = list_in[search], list_in[current]
                    search += 1
            except IndexError:
                break
    return list_in


def group_ordered2(list_in):
    from collections import OrderedDict
    result = OrderedDict()
    for value in list_in:
        result.setdefault(value, []).append(value)
    return result
