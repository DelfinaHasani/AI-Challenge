from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load saved model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Label mapping
label_map = {1: "World", 2: "Sports", 3: "Business", 4: "Sci/Tech"}

# Create FastAPI app
app = FastAPI(title="AG News Text Classification API")

# Define request body
class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict_category(input: InputText):
    clean = input.text.lower()
    vec = vectorizer.transform([clean])
    pred = model.predict(vec)[0]
    return {"prediction": label_map[int(pred)]}
