from flask import Flask,jsonify,request,render_template
import sqlite3
import pickle

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        pregnancies=int(request.form['pregnancies'])
        glucose=int(request.form['glucose'])
        bloodPressure=int(request.form['bloodPressure'])
        skinThickness=int(request.form['skinThickness'])
        insulin=int(request.form['insulin'])
        bmi=float(request.form['bmi'])
        diabetesPedigreeFunction=float(request.form['diabetesPedigreeFunction'])
        age=int(request.form['age'])
        data=[pregnancies,glucose,bloodPressure,skinThickness,insulin,bmi,diabetesPedigreeFunction,age]
        print(data)
        with open('model.pickle','rb') as file:
            model=pickle.load(file)
        result=model.predict([data])
        print(result)
        if result[0]==0:
            outcome='No Diabetic'
        else:
            outcome='Diabetic Patient'
        print("Data has been inserted successful")
        return jsonify({'message':outcome})
    else:
        return render_template('predict.html')

@app.route('/patient',methods=['GET','POST'])
def showpatient():
    conn=sqlite3.connect('patient1.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM PATIENTSINFO")
    data=[]
    for i in cur.fetchall():
        patient={}
        patient['name']=i[0]
        patient['result']=i[1]
        data.append(patient)
    return render_template('showpatient.html',data=data)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=False,port=5500)