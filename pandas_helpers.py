def filter(data, column, value):
    return data.loc[data[column] == value]