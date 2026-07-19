from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained ML model
model = joblib.load("model.pkl")


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    return render_template('predict.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'GET':
        return render_template('predict.html')

    attendance = int(request.form['attendance'])
    marks = int(request.form['marks'])
    engagement = int(request.form['engagement'])

    # Since your model expects 4 inputs,
    # we temporarily use a default StudyHours value.
    study_hours = 3

    prediction = model.predict([[attendance, marks, study_hours, engagement]])[0]

    if prediction == 1:
        risk = "High Risk of Dropout"
        recommendation = "Counseling Required Immediately"
        risk_class = "high"
        icon = "🔴"
    else:
        risk = "Low Risk of Dropout"
        recommendation = "Continue Monitoring — Student is Doing Well"
        risk_class = "low"
        icon = "🟢"

    return render_template(
        'result.html',
        attendance=attendance,
        marks=marks,
        engagement=engagement,
        risk=risk,
        recommendation=recommendation,
        risk_class=risk_class,
        icon=icon
    )


if __name__ == "__main__":
    app.run(debug=True)
    