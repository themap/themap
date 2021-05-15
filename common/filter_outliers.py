import math

def filter_outliers(data,value_fn,threshold=1.5):
    data_length = len(data)
    if data_length <= 4:
        return data
    data = sorted(data, key=value_fn, reverse=False)
    q1 = 0
    q3 = 0
    if ((data_length / 4) % 1) == 0: 
        q1 = 1 / 2 * (value_fn(data[math.floor(data_length / 4)]) + value_fn(data[math.floor(data_length / 4) + 1]))
        q3 = 1 / 2 * (value_fn(data[math.floor(data_length * (3 / 4)) - 1]) + value_fn(data[math.floor(data_length * (3 / 4))]))
    else:
        q1 = value_fn(data[math.floor(data_length / 4 + 1)])
        q3 = value_fn(data[math.floor(data_length * (3 / 4) + 1)])
    iqr = q3 - q1
    max_value = q3 + iqr * threshold
    min_value = q1 - iqr * threshold
    filtered = filter(lambda x: (value_fn(x) >= min_value) and (value_fn(x) <= max_value),data)
    return list(filtered)