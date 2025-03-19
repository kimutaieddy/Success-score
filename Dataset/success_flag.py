from azureml.train.automl import AutoMLConfig

automl_config = AutoMLConfig(
    task="classification",
    training_data=df,
    label_column_name="success_flag",
    primary_metric="accuracy",
    enable_onnx_compatible_models=True,
    featurization="auto",
    blocked_models=["XGBoostClassifier"],  # Simplify for faster training
    experiment_timeout_hours=1  # Hackathon-friendly
)