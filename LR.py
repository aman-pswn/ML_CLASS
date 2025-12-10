def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Enter a valid number.")

def main():
    print("Simple Linear Regression using Normal Formula\n")

    n = int(read_float("Enter number of training data points: "))
    if n < 2:
        print("Need at least 2 points.")
        return

    x_vals = []
    y_vals = []

    for i in range(n):
        print(f"\nData point #{i+1}:")
        x = read_float("  x = ")
        y = read_float("  y = ")
        x_vals.append(x)
        y_vals.append(y)

    # Convert to sums
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xy = sum(x_vals[i] * y_vals[i] for i in range(n))
    sum_x2 = sum(x_vals[i] * x_vals[i] for i in range(n))

    # Apply formulas
    B1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    B0 = (sum_y / n) - B1 * (sum_x / n)

    print("\nCalculated Coefficients:")
    print(f"  B0 (intercept) = {B0}")
    print(f"  B1 (slope)     = {B1}")

    q = int(read_float("\nHow many values of x to predict y for? "))

    for i in range(q):
        print(f"\nPrediction #{i+1}:")
        x_new = read_float("  x = ")
        y_pred = B0 + B1 * x_new
        print(f"  Predicted y = {y_pred}")

if _name_ == "_main_":
    main()