from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

MODEL_PATH = "f1_trained_model.pkl"

if not os.path.exists(MODEL_PATH):
    from model_training import main
    print("Model not found. Training model...")
    main()

model = joblib.load(MODEL_PATH)

FEATURE_COLUMNS = [
    "grid",
    "quali_position",
    "prev_finish",
    "rolling_finish_5",
    "constructor_avg_finish",
    "constructor_avg_points",
    "driver_races",
    "driver_avg_points",
    "grid_quali_diff"
]


@app.route("/")
def home():
    return jsonify({"message": "F1 Prediction API is running."})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if data is None:
            return jsonify({"error": "Invalid JSON input"}), 400

        missing_features = [col for col in FEATURE_COLUMNS if col not in data]
        if missing_features:
            return jsonify({
                "error": f"Missing features: {missing_features}"
            }), 400

        input_data = pd.DataFrame([[data[col] for col in FEATURE_COLUMNS]],
                                  columns=FEATURE_COLUMNS)

        prediction = model.predict(input_data)[0]

        predicted_position = int(round(prediction))
        predicted_position = max(1, min(20, predicted_position))

        return jsonify({
            "predicted_finish_position": predicted_position
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
from chatbot import process_query
from llm import get_llm

llm = get_llm()

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        question = data.get("question")

        response = process_query(question, llm)

        return jsonify({"answer": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
