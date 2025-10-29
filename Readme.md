```
Markovate Assignment
│
├── Core ML (Classification or Regression)/
│   ├── Artifacts
│   ├── Data
│   ├── Plots
│   ├── Titanic_ML_pipeline.ipynb
│
├── Edge_Detection_(ComputerVision)_Optimization&Monitoring│/
│   ├── Data        
│   ├── Test Image
│   ├── Drift_monitoring_plan.md
│   ├── Edge_Detection_(Computer_Vision)_and_Monitoring.ipynb
│   ├── Export_OnnX.md
│   ├── Model_optimization.md
│ 
├── Experimentation, Reproducibility & Deployment Pipeline/
│   ├── app                 
│   ├── Baseline
│   ├── config                     
│   └── Data_Ingestion
│   └── Model_Artifacts_registry 
│   └── Model_training         
│   └── Monitoring 
├── Quick Reasoning
│   ├── readme.md

```


## 1. Core ML (Classification) – Markovate ML Engineer Assessment
This module demonstrates a complete end-to-end ML workflow for a simple classification problem using scikit-learn, covering:

1. Data exploration (EDA)
2. Basic feature engineering
3. Model training and evaluation
4. Feature correlation visualization
5. Model persistence for deployment readiness

## Dataset
1. Dataset Used: Titanic Dataset
2. Target Classes: 1
3. This dataset is lightweight, interpretable, and ideal for demonstrating classification workflows.

## Exploratory Data Analysis (EDA)
1. Loaded and inspected the Titanic dataset using Pandas.
2. Checked for missing values and data distribution.
3. Created a feature correlation heatmap to identify relationships among input variables.


### Feature Engineering
1. imputation transformer
2. one hot encoding
3. Scaling
4. Feature selection

### Sklearn Pipeline
1. train the model
2. Create Pipeline
3. Fit pipeline with the data
4. Evaluate Model pipe
4. Save model pipe artifacts


## 2. Edge_Detection_(ComputerVision) Optimization & Monitoring│
1. Basic CNN model Building on BIPEDV2 DataSet
2. Custom Sobel and Canny code
3. Comparison between **CNN** **|** **Sobel** **|** **Canny**

    ### 4.Optimization and Monitoring
    1. Exporting to Onnx 
    2. Calcuting CPU latency

    ### Monitoring Plans
    [Edge_Detection_(ComputerVision)_Optimization&Monitoring](Edge_Detection_(ComputerVision)_Optimization&Monitoring/Drift_monitoring_plan.md)

## 3. Experimentation, Reproducibility & Deployment Pipeline
[Experimentation, Reproducibility & Deployment Pipeline](<Experimentation, Reproducibility & Deployment Pipeline/Readme.md>)

## Quick Reasoning
[Quick Reasoning](<Quick Reasoning/readme.md>)