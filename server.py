from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='supersecrets'
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter']=1
    elif 'counter' in session:
        session['counter']+=1
    if 'reset' not in session:
        session['reset']=0

    return render_template("index.html")
    
@app.route('/add2', methods=['POST'])
def add2():
    if request.form['add2']=='add2':
        session['counter']+=2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if request.form['reset']=='reset':
        session['counter']=0
    return redirect('/')


app.run(debug=True) # run our server
