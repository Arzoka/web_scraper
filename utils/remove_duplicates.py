def remove_duplicates(lst):
    if isinstance(lst, list):
        return list(set(lst))
    elif isinstance(lst, dict):
        return {k: v for k, v in lst.items() if v is not None}
    else:
        raise TypeError('remove_duplicates() only accepts lists and dicts.')
