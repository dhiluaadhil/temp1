import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import os
from preprocessing import load_and_preprocess_data

def train_dl_model():
    print("--- Phase 2: Deep Learning Pipeline ---")
    data_path = '../data/ip_filings_synthetic_data.csv'
    
    if not os.path.exists(data_path):
        print("Data not found.")
        return
        
    X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data(data_path)
    
    # Using Multi-Layer Perceptron (Neural Network) for DL Baseline
    print("Training Multi-Layer Perceptron (Deep Learning Neural Network)...")
    dl_classifier = MLPClassifier(hidden_layer_sizes=(128, 64, 32), max_iter=500, random_state=42)
    
    dl_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('classifier', dl_classifier)])
    
    dl_pipeline.fit(X_train, y_train)
    y_pred = dl_pipeline.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"DL Model Accuracy: {acc:.4f}")
    print("DL Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == '__main__':
    train_dl_model()
