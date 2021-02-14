def pre_process(a=0.97):
    def inner_wrapper(def_):
        def wrapper(list_):
            res = []
            for i in range(len(list_)):
                res.append(round(list_[i] - a * list_[i-1], 2))
            def_(res)
        return wrapper
    return inner_wrapper

s = [1, 3, 5, 7, 9]

@pre_process(a=0.93)
def plot_signal(s_):
    for sample in s_:
        print(sample)
plot_signal(s)