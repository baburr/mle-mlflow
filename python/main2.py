import os
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor

EXPERIMENT_NAME = 'Default' # ваш код здесь (напишите своё уникальное имя эксперимента)
RUN_NAME = "model_0_registry"
REGISTRY_MODEL_NAME = "churn_model_bburxodjaev"


os.environ["MLFLOW_S3_ENDPOINT_URL"] = 'https://storage.yandexcloud.net' # ваш код здесь
os.environ["AWS_ACCESS_KEY_ID"] = 'YCAJE3Nlz8iDILW5VTYM1ihQB'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'YCPjvS7uwhvJpUj3bKm8X-IX4QAwBIVsvX61IL44'

# ваш код здесь
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = CatBoostRegressor()
model.fit(X_train, y_train)

# Подготовка данных для логирования
predictions = model.predict(X_test)

pip_requirements = '../requirements.txt'
signature = mlflow.models.infer_signature(X_test, predictions)
input_example = X_test[:10]
metadata = {'model_type': 'monthly'}


experiment_id = mlflow.get_experiment_by_name(EXPERIMENT_NAME).experiment_id

with mlflow.start_run(run_name=RUN_NAME, experiment_id=experiment_id) as run:
    run_id = run.info.run_id
    # ваш код здесь
    model_info = mlflow.catboost.log_model(
        await_registration_for=60,
        cb_model=model,
        artifact_path='models',
        input_example=input_example,
        signature=signature,
        metadata=metadata,
        pip_requirements=pip_requirements,
        registered_model_name=REGISTRY_MODEL_NAME
    )