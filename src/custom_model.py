from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any, List
import uvicorn
import transformers
import torch

# Example model class (replace with your actual model)
class EvilLlama:
    def predict(self, data):
        print("Data", data)
        query = data
        model_id = "cognitivecomputations/dolphin-2.9.4-llama3.1-8b"

        pipeline = transformers.pipeline(   
            "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto",
            max_length = 2048
        )

        return {"prediction": pipeline(query)[0]['generated_text']}

app = FastAPI()
model = EvilLlama()

class Parameters(BaseModel):
    stream: bool
    stop: List[str]
    details: bool
    return_full_text: bool

class PredictionRequest(BaseModel):
    inputs: str
    parameters: Parameters


# Define a route for the prediction endpoint
@app.post("/predict")
def predict(request: PredictionRequest):
    # Use the model to make predictions based on input_data
    print("Request", request)
    prediction = model.predict(request.inputs)
    return prediction

if __name__ == "__main__":
    # Use Uvicorn to run the app, accessible from outside the server
    uvicorn.run(app, host="0.0.0.0", port=8000)
