from flask import Flask,render_template,redirect,request
import pickle
pipe =pickle.load(open('pipepredict.pkl', 'rb'))
piperesult =pickle.load(open('piperesult.pkl','rb'))
import numpy as np
import pandas as pd
import mysql.connector
app = Flask(__name__)
app.secret_key = 'secret'
con=mysql.connector.connect(host="localhost",user="root",password="",database="registration")
cursor = con.cursor()



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    cursor.execute("""SELECT * FROM `user` WHERE `email` LIKE  '{}' """.format(email))
    member = cursor.fetchall()
    if len(member)>0:
        return render_template('register.html', message="Email already exists")
    else:
        cursor.execute("""INSERT INTO `user` (`id`,`name`,`email`,`password`)VALUES
        (NULL,'{}','{}','{}')""".format(name,email,password))
        con.commit()
        return render_template('login.html',message="Registration Successful. Kindly login to proceed")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    cursor.execute("""SELECT * FROM `user` WHERE `email` LIKE  '{}' AND `password` LIKE  '{}' """
                   .format(email,password))
    users = cursor.fetchall()
    print(users)
    if len(users)>0:
        return redirect('/profile')
    else:
        return render_template('login.html',message='Incorrect Email/Password')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/scoreprediction')
def scoreprediction():
    return render_template('scoreprediction.html')


@app.route('/perform_predictons',methods=['post'])
def perform_predictions():
    batting = request.form.get('batting')
    bowling = request.form.get('bowling')
    score = int(request.form.get('score'))
    #overs = int(request.form.get('overs'))


    over = float(request.form.get('overs'))
    decimal_part = int(str(over).split('.')[1])
    overs = int(str(over).split('.')[0])


    wickets = int(request.form.get('wickets'))
    wickets_left = 10 -wickets
    balls_left = 120 -((overs * 6) + decimal_part)

    crr = score/(over+(decimal_part/6))
    lastfive = request.form.get('lastfive')



    print('Batting : ',batting)
    print('Bowling : ',bowling)
    print('Score : ',score)
    print('Wickets Left : ',wickets_left)
    print('Balls Left : ',balls_left)
    print('Current Run Rate : ',crr)
    print('OVERS : ',overs)


    features = np.array([[batting,bowling, score, wickets_left, balls_left, crr, lastfive]])
    features_df = pd.DataFrame(features, columns=['team_1', 'team_2', 'total_runs', 'wickets_left', 'balls_left', 'crr',
                                                  'last_five'])
    pred = str(pipe.predict(features_df)[0])
    pred = pred.split('.')[0]
    print(pred)
    return render_template('scoreprediction.html',pred=pred)



@app.route('/resultprediction')
def resultprediction():
    return render_template('resultprediction.html')


@app.route('/perform_result',methods=['post'])
def perform_result():
    batting = request.form.get('batting')
    bowling = request.form.get('bowling')
    score = int(request.form.get('score'))
    #overs = int(request.form.get('overs'))


    over = float(request.form.get('overs'))
    decimal_part = int(str(over).split('.')[1])
    overs = int(str(over).split('.')[0])


    wickets = int(request.form.get('wickets'))
    wickets_left = 10 -wickets
    balls_left = 120 -((overs * 6) + decimal_part)

    crr = score/(overs+(decimal_part/6))
    lastfive = request.form.get('lastfive')
    target = int(request.form.get('target'))

    score_left = target - score
    rem_overs = 21 - (overs + (decimal_part / 6))
    rrr = score/rem_overs


    print('Batting : ', batting)
    print('Bowling : ', bowling)
    print('Score : ', score)
    print('Wickets Left : ', wickets_left)
    print('Balls Left : ', balls_left)
    print('Current Run Rate : ', crr)
    print('OVERS : ', overs)
    print('target : ', target)
    print('Score Left : ',score_left)
    print('rrr : ',rrr)

    features = np.array([[batting, bowling, score_left, balls_left, wickets_left, target, crr, rrr, lastfive]])
    features_df = pd.DataFrame(features, columns=['team_1', 'team_2', 'runs_left', 'balls_left', 'wickets_left', 'Targets', 'crr', 'rrr', 'last_five'])
    pred = piperesult.predict_proba(features_df)
    predbatting = pred[0][1] * 100
    predbowling = pred[0][0] * 100
    print('Pred Batting',predbatting)
    print('Pred Bowling',predbowling)
    result = f"{batting} : {predbatting:.2f} || {bowling} : {predbowling:.2f}"

    return render_template('resultprediction.html', pred=result)


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')





app.run(debug=True)