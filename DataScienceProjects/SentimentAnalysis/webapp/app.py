from flask import Flask, request, jsonify
import torch
import numpy as np
from transformers import RobertaForSequenceClassification, RobertaTokenizer
import onnxruntime

app = Flask(__name__)
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
session = onnxruntime.InferenceSession("roberta-sequence-classification-9.onnx")

app.route("/")
def home():
    print("I am here")
    return "<h3> This is Roberta Sentiment Analysis Prediction container </h3>"


app.route("/predict", methods=["POST"])
def predict():
    """
    Input Sample:
        ["you smell really well"]
    Output sample:
        {"positive_sentiment":True}
    """
    input_ids = torch.tensor(tokenizer.encode(request.json[0], add_special_tokens=True)).unsqueeze(0)

    if input_ids.requires_grad:
        numpy_arr = input_ids.detach().cpu().numpy()
    else:
        numpy_arr = input_ids.cpu().numpy()

    inputs = {session.get_inputs()[0].name: numpy_arr}
    out = session.run(None, inputs)

    results = np.argmax(out)

    return jsonify({"positive_sentiment": bool(results)})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)