End-to-end MLOps pipeline that predicts if a customer is likely to leave a telecom company

Requirements (Core Libraries to install):

1.) scikit-learn
2.) xgboost
3.) mlflow
4.) fastapi
5.) uvicorn
6.) docker
7.) evidently
8.) pytest
9.) mysql-connector-python
10.) Python 3.11.9

> .github
    - For CI/CD pipelines

> api
    -  FastAPI app + Dockerfile 

> data
    - CSV file containing labeled data in format of: 
        -> CustomerID,gender,SeniorCitizen,Partner,Dependents,tenure,
        PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,
        DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,
        PaymentMethod,MonthlyCharges,TotalCharges,Churn
        
    - DB tha holds the tables containing the data

> monitoring
    - Drift detection, logging scripts

> notebooks
    - EDA and experiments

> src
    - Training, preprocessing, utilities

> tests
    - Unit and integration tests

For database:
> downloaded csv
> used import wizard in mysql to populate a table with data

