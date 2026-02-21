def fibbonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibbonacci_series(n - 1)
        series.append(series[-1] + series[-2])
        return series
print(fibbonacci_series(11))    
