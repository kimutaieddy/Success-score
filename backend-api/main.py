from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Enable CORS (Allows frontend to call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; restrict for security in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

class InputData(BaseModel):
    input_data: dict

AZURE_ML_ENDPOINT_URL = "https://wakadinali-model-mrazi.westus3.inference.ml.azure.com/score"
AZURE_ML_API_KEY = os.getenv("AZURE_ML_API_KEY")

if not AZURE_ML_API_KEY:
    raise ValueError("Azure ML API key is missing. Set AZURE_ML_API_KEY environment variable.")

@app.post("/inference")
def inference(input_data: InputData):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AZURE_ML_API_KEY}",
        }
        response = requests.post(AZURE_ML_ENDPOINT_URL, json=input_data.dict(), headers=headers)
        response.raise_for_status()
        
        # Ensure response is JSON
        result = response.json()
        
        # Check if result is a list
        if isinstance(result, list) and len(result) > 0:
            model_output = result[0]  # Extract first item
        elif isinstance(result, dict):
            model_output = result.get("prediction", None)
        else:
            raise ValueError("Unexpected response format from Azure ML API")

        # Convert model output to success/failure message
        if model_output == 1:
            return {"status": "success"}
        elif model_output == 0:
            return {"status": "failure"}
        else:
            raise ValueError(f"Unexpected model output: {model_output}")

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error calling Azure ML endpoint: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Invalid response from model: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
