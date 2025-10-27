def seq_num(num):
    for elem in range(num):
        yield elem

gen = seq_num(10)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
