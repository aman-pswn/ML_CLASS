import numpy as np
def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number — please enter a numeric value.")
def main():
    print("Multiple Linear Regression (y = B0 + B1*x1 + B2*x2)\n")
    n=int(read_float("Enter number of training data points (n): "))
    if n<2:
        print("For regression you should provide at least 2 data points. Exiting.")
        return
    X_list=[]
    y_list=[]
    print("\nEnter each training example's x1, x2 and y (press Enter after each value).")
    for i in range(n):
        print(f"\nData point #{i+1}:")
        x1=read_float("  x1 = ")
        x2=read_float("  x2 = ")
        y=read_float("  y  = ")
        X_list.append([1.0,x1,x2])
        y_list.append(y)
    X=np.array(X_list)
    y=np.array(y_list)
    beta=np.linalg.pinv(X)@y
    B0,B1,B2=beta
    print("\nFitted coefficients:")
    print(f"  B0 = {B0}")
    print(f"  B1 = {B1}")
    print(f"  B2 = {B2}")
    y_pred_train=X@beta
    residuals=y-y_pred_train
    rss=np.sum(residuals**2)
    print(f"\nRSS: {rss:.6f}")
    q=int(read_float("\nHow many unknown (x1,x2) pairs would you like to predict? "))
    if q<=0:
        print("No predictions requested. Done.")
        return
    print("\nEnter unknown pairs to predict y:")
    for j in range(q):
        print(f"\nUnknown #{j+1}:")
        ux1=read_float("  x1 = ")
        ux2=read_float("  x2 = ")
        ux=np.array([1.0,ux1,ux2])
        uy=ux@beta
        print(f"  Predicted y = {uy}")
if _name=="main_":
    main()