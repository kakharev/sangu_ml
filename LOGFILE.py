x = [1000, 1800, 1100, 1200, 2100, 1400, 2000, 1600, 1700, 1050, 1900, 1500, 1300]
y = [70, 110,  65,  75, 155,  90, 180, 115, 100,  40, 175,  78,  75]
def mean(data):
    return sum(data) / len(data)
def linear_regression(x, y):
    mean_x = mean(x)
    mean_y = mean(y)

    # სლოპი
    numerator = sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y))
    denominator = sum((x_i - mean_x)**2 for x_i in x)
    slope = numerator / denominator

    # ინტერცეპტი (b)
    intercept = mean_y - slope * mean_x

    return slope, intercept

def predict(x, slope, intercept):
    return slope * x + intercept



slope, intercept = linear_regression(x, y)
print("Slope:", slope)
print("Intercept:", intercept)

# Predict for a new value of x
new_x = 1600
predicted_y = predict(new_x, slope, intercept)
print("Predicted y for x =", new_x, ":", predicted_y)
