from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def examForm():
    return render_template('examForm.html')

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form['name']
    roll=request.form['roll']
    registrationNumber=request.form['registrationNumber']
    registratedCourse=request.form['registratedCourse']
    examDate=request.form['examDate']
    examEnd=request.form['examEnd']
    return render_template('/success.html', 
                           name=name,
                           roll=roll,
                           registratedCourse=registratedCourse,
                           registrationNumber=registrationNumber,
                           examEnd=examEnd,
                           examDate=examDate
                           )

if __name__=="__main__":
    app.run(debug=True)