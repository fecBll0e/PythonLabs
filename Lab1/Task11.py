def frange(from_, to_, step_):
    while from_ < to_ - step_:
        from_ += step_
        print(round(from_, 1))
        
frange(1, 5, 0.1)