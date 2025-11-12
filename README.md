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
11.) pymysql sqlalchemy

>src

    - CSV file containing labeled data in format of: 
        -> CustomerID,gender,SeniorCitizen,Partner,Dependents,tenure,
        PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,
        DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,
        PaymentMethod,MonthlyCharges,TotalCharges,Churn
        
    - Training, preprocessing, utilities