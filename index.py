from flask import Flask,request,render_template,redirect

app = Flask(__name__);

data=[]

@app.route("/",methods=["GET"])
def home():
    return render_template('home.html',name=data)

@app.route("/",methods=["POST"])
def add():
    fdata = request.form
    data.append(fdata["name"])
    return redirect('/')

@app.route("/delete",methods=["post"])
def delete():
    fdata = request.form
    data.pop( int(fdata["index"]))
    return redirect('/')

@app.route("/update",methods=["post"])
def update():
    fdata = request.form
    data[int(fdata['index'])] = fdata["name"]
    return redirect('/')

app.run(port=5000,debug=True)