# Machine Learning Basics Example: Iris Classification

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
iris = load_iris()
X = iris.data          # features (flower measurements)
y = iris.target        # labels (flower species)

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Choose a model
model = DecisionTreeClassifier()

# 4. Train the model
model.fit(X_train, y_train)

# 5. Make predictions
predictions = model.predict(X_test)

# 6. Evaluate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Predictions:", predictions)
print("Actual:     ", y_test)
print("Accuracy:", accuracy)
