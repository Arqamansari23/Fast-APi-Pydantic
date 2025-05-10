from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target

    # Initialize model
    model = RandomForestClassifier()

    # Train model
    model.fit(X, y)

    # Save the model
    joblib.dump(model, 'model/iris_model.pkl')


if __name__ == "__main__":
    train_model()
    print("Model trained and saved as iris_model.pkl")