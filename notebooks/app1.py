{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "39e067bd-73a9-4d19-b40e-54bde003233c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import render_template, request, jsonify,Flask\n",
    "import flask\n",
    "import numpy as np\n",
    "import traceback #allows you to send error to user\n",
    "import pickle\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c8eaf43d-92c5-445e-b5e7-a6a6d769dd23",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# App definition\n",
    "app = Flask(__name__)\n",
    "\n",
    "# importing models\n",
    "with open('model.pkl', 'rb') as f:\n",
    "   model = pickle.load (f)\n",
    "\n",
    "with open('model_columns.pkl', 'rb') as f:\n",
    "   model_columns = pickle.load (f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1661f101-0004-42ab-b0ae-8cacbdfefcd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [20/Jan/2023 16:05:39] \"GET / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "#webpage\n",
    "\n",
    "@app.route('/')\n",
    "def welcome():\n",
    "    return \"Welcome! Use this Flask App for loan status prediction\"\n",
    "\n",
    "@app.route('/predict', methods=['POST','GET'])\n",
    "def predict():\n",
    "    if flask.request.method == 'GET':\n",
    "        return \"Prediction page. Try using post with params to get specific prediction.\"\n",
    "\n",
    "    if flask.request.method == 'POST':\n",
    "        try:\n",
    "            json_ = request.json # '_' since 'json' is a special word\n",
    "            print(json_)\n",
    "            query_ = pd.get_dummies(pd.DataFrame(json_))\n",
    "            query = query_.reindex(columns = model_columns, fill_value= 0)\n",
    "            prediction = list(regressor.predict(query))\n",
    "\n",
    "            return jsonify({\n",
    "               \"prediction\":str(prediction)\n",
    "           })\n",
    "\n",
    "        except:\n",
    "            return jsonify({\n",
    "               \"trace\": traceback.format_exc()\n",
    "               })\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6078bff-93c3-4377-b452-d96e4b976580",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
