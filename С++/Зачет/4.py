import statistics

def covariance(x, y):
    return statistics.covariance(x, y)

x = [1, 2, 4, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 1,6, 3, 1, 2, 3]
print(f"Ковариация двух списков: {covariance(x, y)}")


