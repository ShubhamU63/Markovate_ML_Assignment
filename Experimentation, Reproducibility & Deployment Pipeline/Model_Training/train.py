
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
from sklearn.metrics import accuracy_score, classification_report
from Data_Ingestion.data_ingestion import get_logger,read_params



ARTIFACT_DIR = "Model_Artifacts_Registry"
MODEL_DIR = os.path.join(ARTIFACT_DIR, "models")
REPORT_DIR = os.path.join(ARTIFACT_DIR, "reports")
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

training_logger = get_logger("training_logger", "training.log")

def train_model(df: pd.DataFrame, target: str,params_path='config/params.yaml'):

    params = read_params(params_path)
    seed = params.get('seed', 42)
    test_size = params.get('test_size', 0.2)
    
    df.drop(columns=['PassengerId','Name','Ticket','Cabin'],inplace=True)

    X = df.drop(columns=[target])
    y = df[target]

    trf1 = ColumnTransformer([
    ('impute_age',SimpleImputer(),[2]),
    ('impute_embarked',SimpleImputer(strategy='most_frequent'),[6])],remainder='passthrough')
    
    trf2 = ColumnTransformer([
    ('ohe_sex_embarked',OneHotEncoder(sparse_output=False,handle_unknown='ignore'),[1,6])],remainder='passthrough')
    
    trf3 = ColumnTransformer([
    ('scale',MinMaxScaler(),slice(0,10))])

    trf4 = SelectKBest(score_func=chi2,k=8)

    trf5 = DecisionTreeClassifier()

    pipe = Pipeline([
    ('trf1',trf1),
    ('trf2',trf2),
    ('trf3',trf3),
    ('trf4',trf4),
    ('trf5',trf5)])

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=test_size,random_state=seed)

    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)

    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)

    # Step 5: Save model & report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_path = os.path.join(MODEL_DIR, f"pipeline_model_{timestamp}.joblib")
    report_path = os.path.join(REPORT_DIR, f"report_{timestamp}.txt")

    joblib.dump(pipe, model_path)
    with open(report_path, "w") as f:
        f.write(f"Accuracy: {acc}\n\n{report}")

    training_logger.info(f"Pipeline model saved at {model_path} with accuracy {acc}")
    return {"model_path": model_path, "report_path": report_path, "accuracy": acc}