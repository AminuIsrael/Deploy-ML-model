import json
import pickle
import numpy as np
from flask import Flask, request
# 

flask_app = Flask(__name__)

#ML model path
model_path = "ML_Model/model.pkl"


@flask_app.route('/', methods=['GET'])
def index_page():
    return_data = {
        "error" : "0",
        "message" : "Successful"
    }
    return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json')

@flask_app.route('/predict',methods=['GET'])
def model_deploy():
    try:
        age = request.form.get('age')
        bs_fast = request.form.get('BS_Fast')
        bs_pp = request.form.get('BS_pp')
        plasma_r = request.form.get('Plasma_R')
        plasma_f = request.form.get('Plasma_F')
        HbA1c = request.form.get('HbA1c')
        fields = [age,bs_fast,bs_pp,plasma_r,plasma_f,HbA1c]
        if not None in fields:
            #Datapreprocessing Convert the values to float
            age = float(age)
            bs_fast = float(bs_fast)
            bs_pp = float(bs_pp)
            plasma_r = float(plasma_r)
            plasma_f = float(plasma_f)
            hbA1c = float(HbA1c)
            result = [age,bs_fast,bs_pp,plasma_r,plasma_f,HbA1c]
            #Passing data to model & loading the model from disk
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])[0]
            conf_score =  np.max(classifier.predict_proba([result]))*100
            return_data = {
                "error" : '0',
                "message" : 'Successfull',
                "prediction": prediction,
                "confidence_score" : conf_score.round(2)
            }
        else:
            return_data = {
                "error" : '1',
                "message": "Invalid Parameters"             
            }
    except Exception as e:
        return_data = {
            'error' : '2',
            "message": str(e)
            }
    return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json')


if __name__ == "__main__":
    flask_app.run(host ='0.0.0.0',port=5432, debug=False)
    
    
