# Backend API

This is the FastAPI backend for the Success-score ROI Calculator.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Azure ML credentials:
```
AZURE_ML_ENDPOINT_URL=your_endpoint_url_here
AZURE_ML_API_KEY=your_api_key_here
```

## Running the API

Start the server:
```bash
python main.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Welcome message
- `POST /inference` - Submit data for ROI calculation and prediction

## Environment Variables

- `AZURE_ML_ENDPOINT_URL` - Azure Machine Learning endpoint URL
- `AZURE_ML_API_KEY` - Azure Machine Learning API key
