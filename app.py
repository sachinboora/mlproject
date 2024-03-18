import sys
from pathlib import Path
sys.path.append(str(Path('src').parent.parent)) 
import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException

application = Flask( __name__)

app = application

# route for homepage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=str(request.form.get('gender')),
            race_ethnicity=str(request.form.get('ethnicity')),
            parental_level_of_education=str(request.form.get('parental_level_of_education')),
            lunch=str(request.form.get('lunch')),
            test_preparation_course=str(request.form.get('test_preparation_course')),
            reading_score=int(request.form.get('reading_score')), # type: ignore
            writing_score=int(request.form.get('writing_score')), # type: ignore
        )

        preds_df = data.get_data_as_data_frame()
        print(preds_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(preds_df)
        return render_template('home.html', results=results[0])
    
if  __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)

