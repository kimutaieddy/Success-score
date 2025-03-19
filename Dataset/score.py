import json
import mlflow
import pandas as pd
from typing import Dict, Any

def init():
    """
    Load the model during startup.
    """
    global model
    model_path = "azureml://locations/eastus/workspaces/fec3e1a4-3b34-4972-923f-ab1a440d8086/models/da/versions/1"
    model = mlflow.pyfunc.load_model(model_path)

def run(raw_data: str) -> Dict[str, Any]:
    """
    Process incoming data and return predictions.
    """
    try:
        # Parse input data
        data = json.loads(raw_data)["data"]
        input_df = pd.DataFrame(data)

        # Get predictions
        predictions = model.predict(input_df)

        # Return results
        return {
            "status": "success",
            "predictions": predictions.tolist()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Optional: Add logging for debugging
if __name__ == "__main__":
    init()
    test_data = json.dumps({"data": [[1.2, 3.4, 5.6]]})  # Example input
    print(run(test_data))