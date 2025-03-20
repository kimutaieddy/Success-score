from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input data model
class InputData(BaseModel):
    input_data: dict

# Azure ML endpoint configuration
AZURE_ML_ENDPOINT_URL = os.getenv("AZURE_ML_ENDPOINT_URL")
AZURE_ML_API_KEY = os.getenv("AZURE_ML_API_KEY")

if not AZURE_ML_API_KEY:
    raise ValueError("Azure ML API key is missing. Set AZURE_ML_API_KEY in .env file.")

# ROI calculation function
def calculate_roi_metrics(input_values, success_status):
    try:
        budget = float(input_values["budget"])
        employees = int(input_values["employees_impacted"])
        duration = int(input_values["duration_months"])
        comm_score = float(input_values["communication_score"])
        avg_salary = float(input_values["_avg_salary"])
        productivity_gain = float(input_values["_productivity_gain"])

        HOURS_PER_MONTH = 160
        MONTHS_PER_YEAR = 12

        hourly_wage = avg_salary / (HOURS_PER_MONTH * MONTHS_PER_YEAR)
        engagement_rate = (comm_score / 5) * 100  

        ips = employees * hourly_wage * HOURS_PER_MONTH * duration * productivity_gain

        if success_status == "success":
            eb = ips + 0.1 * budget
            ec = budget  
        else:
            disengagement_cost = employees * hourly_wage * HOURS_PER_MONTH * duration * (1 - engagement_rate / 100)
            cf = 1.5 * budget + disengagement_cost
            eb = 0
            ec = budget + cf

        net_savings = eb - ec
        roi = (net_savings / budget) * 100 if budget != 0 else 0

        return {
            "status": success_status,
            "roi": round(roi, 1),
            "net_savings": round(net_savings, 2),
            "productivity_savings": round(ips, 2),
            "total_costs": round(ec, 2),
        }
    except Exception as e:
        logging.error(f"Error in ROI calculation: {e}")
        raise ValueError("Invalid input data for ROI calculation.")

# Inference endpoint
@app.post("/inference")
async def inference(input_data: InputData):
    try:
        logging.debug(f"Received input data: {input_data.dict()}")

        headers = {
            "Authorization": f"Bearer {AZURE_ML_API_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.post(AZURE_ML_ENDPOINT_URL, json=input_data.dict(), headers=headers)
        
        if response.status_code == 401:
            logging.error("Unauthorized: Invalid API key!")
            raise HTTPException(status_code=401, detail="Unauthorized: Check your API key!")

        response.raise_for_status()
        response_json = response.json()
        
        # Handling different response formats
        if isinstance(response_json, list):
            model_output = response_json[0]
        elif isinstance(response_json, dict) and "prediction" in response_json:
            model_output = response_json["prediction"]
        else:
            logging.error(f"Unexpected response format: {response_json}")
            raise HTTPException(status_code=500, detail="Invalid response format from Azure ML.")

        success_status = "success" if model_output == 1 else "failure"

        columns = input_data.input_data["columns"]
        values = input_data.input_data["data"][0]
        input_values = dict(zip(columns, values))

        metrics = calculate_roi_metrics(input_values, success_status)

        logging.debug(f"Calculated ROI metrics: {metrics}")
        return metrics

    except requests.exceptions.RequestException as e:
        logging.error(f"Azure ML request failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to connect to Azure ML service.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, reload=True)
