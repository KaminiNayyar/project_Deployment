from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd


# App definition
app = Flask(__name__)

# importing models
with open('df_pipeline.pkl', 'rb') as f:
   df_pipeline= pickle.load (f)

with open('model_columns.pkl', 'rb') as f:
   model_columns = pickle.load (f)

  #webpage

@app.route('/')
def test():
    return "welcome!"

@app.route('/predict', methods=['POST'])
def predict():

    if flask.request.method == 'POST':
       try:
           json_ = request.json # '_' since 'json' is a special word
           print(json_)
           #query_ = pd.get_dummies(pd.DataFrame(json_))
           query_ = pd.DataFrame(json_)
           query = query_.reindex(columns = model_columns, fill_value= 0)
           prediction = list(df_pipeline.predict(query))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })

if __name__ == "__main__":
    app.run()
  

 