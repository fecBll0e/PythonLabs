def non_empty(def_):
    def wrapper():
        return list(filter(lambda x: not x == '' and x is not None, def_()))
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', None]
print(get_pages())