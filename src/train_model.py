import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
import os

from preprocessing import load_and_preprocess_data

def train_and_evaluate(X_train, X_test, y_train, y_test, preprocessor, model_type='logistic'):
    print(f"Training {model_type} model...")
    
    if model_type == 'logistic':
        classifier = LogisticRegression(random_state=42)
    elif model_type == 'random_forest':
        classifier = RandomForestClassifier(random_state=42, n_estimators=100)
    else:
        raise ValueError("Unsupported model type")
        
    # Create full pipeline
    clf_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                   ('classifier', classifier)])
    
    # Train model
    clf_pipeline.fit(X_train, y_train)
    
    # Predict
    y_pred = clf_pipeline.predict(X_test)
    y_pred_proba = clf_pipeline.predict_proba(X_test)[:, 1]
    
    # Evaluate
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred_proba)
    }
    
    print("\n--- Evaluation Metrics ---")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")
        
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return clf_pipeline, metrics

if __name__ == '__main__':
    data_path = '../data/ip_filings_synthetic_data.csv'
    
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}. Please run generate_data.py first.")
        exit(1)
        
    X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data(data_path)
    
    # Train Logistic Regression
    lr_model, lr_metrics = train_and_evaluate(X_train, X_test, y_train, y_test, preprocessor, 'logistic')
    
    # Train Random Forest
    rf_model, rf_metrics = train_and_evaluate(X_train, X_test, y_train, y_test, preprocessor, 'random_forest')
    
    # Save the report
    os.makedirs('../docs', exist_ok=True)
    report_path = '../docs/metrics_report.txt'
    with open(report_path, 'w') as f:
        f.write("Baseline ML Model Evaluation\n")
        f.write("="*30 + "\n\n")
        f.write("Logistic Regression Metrics:\n")
        for k, v in lr_metrics.items():
            f.write(f"{k}: {v:.4f}\n")
        f.write("\nRandom Forest Metrics:\n")
        for k, v in rf_metrics.items():
            f.write(f"{k}: {v:.4f}\n")
    print(f"\nMetrics saved to {report_path}")
