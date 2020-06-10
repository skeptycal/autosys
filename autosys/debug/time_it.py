def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        dt = (te - ts) * 1000

        time_list.append({method.__name__: f"{dt:4.4}"})
        dbprint(time_list[-1])
        return (result, dt)

    return timed
