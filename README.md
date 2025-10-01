📰 AG News Text Classification

This project implements a text classification pipeline using the AG News dataset
.
The model is trained to classify news articles into 4 categories:

🌍 World

⚽ Sports

💼 Business

💻 Sci/Tech


⚙️ Installation & Setup

Clone the repo and install dependencies:

git clone https://github.com/DelfinaHasani/AI-Challenge

pip install -r requirements.txt

🚀 Run the API

Start the FastAPI server with:

uvicorn app:app --reload


Then open Swagger UI in your browser:
👉 http://127.0.0.1:8000/docs

📌 Example Request

POST /predict

{
  "text": "Cristiano Ronaldo signs new contract with F.C. Barcelona"
}

✅ Example Response
{
  "prediction": "Sports"
}

📊 Model Performance

Logistic Regression achieved 91% accuracy

Naive Bayes achieved 89% accuracy

📈 Confusion matrix & classification reports are included in the notebook.

📚 Tech Stack

Python 3.13

FastAPI – API framework

scikit-learn – ML training & evaluation

NLTK – text preprocessing

Pandas / NumPy – data handling

✨ Future Improvements

Deploy to cloud (Heroku / Render / Docker)

Add a simple frontend (React or HTML form)

Support for more datasets / multi-label classification