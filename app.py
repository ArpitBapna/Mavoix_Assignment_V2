#!/usr/bin/env python
# coding: utf-8

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('/home/arpitbapna/mysite/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    ug = request.form.get('ug')
    ugyear = request.form.get('ugyear')
    pg = request.form.get('pg')
    pgyear = request.form.get('pgyear')
    python = request.form.get('python')
    r = request.form.get('r')
    ds = request.form.get('ds')
    ml = request.form.get('ml')
    dl = request.form.get('dl')
    nlp = request.form.get('nlp')
    sm = request.form.get('sm')
    aws = request.form.get('aws')
    sql = request.form.get('sql')
    nosql = request.form.get('nosql')
    excel = request.form.get('excel')

    if ug:
        deg_type_UG = 1
    else:
        deg_type_UG = 0
    if pg:
        deg_type_PG = 1
        year = int(pgyear)
    else:
        deg_type_PG = 0
        year = int(ugyear)
    if year == 2020 or year == 2021 or year == 2022 or year == 2023:
        year_enc = 3
    elif year == 2019:
        year_enc = 2
    else:
        year_enc = 1


    print(python,r,ds,ml,dl,nlp,sm,aws,sql,nosql,year_enc,deg_type_PG, deg_type_UG,excel)

    features = [int(python),int(r),int(ds), deg_type_PG, deg_type_UG,int(ml),int(dl),int(nlp),int(sm),int(aws),int(sql),int(nosql),int(excel),year_enc]
    final_features = [np.array(features)]

    prediction = model.predict(final_features)
    if prediction[0] == 1:
        output = "Congratulations! You are shortlisted for Data Scientist "
    elif prediction[0] == 0:
        output = "Sorry! You did not qualify for Data Scientist"
    return render_template('index.html', Result = '{}'.format(output))


if __name__ == "__main__":
    app.run()



