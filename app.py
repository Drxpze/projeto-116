from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    
    name = "Arthur"
    idade = "15"
    
    return render_template('index.html',name=name,idade=idade)

@app.route("/2")
def pai():
    name = "João"
    idade = "45"
    
    return(render_template("index.html",name=name,idade=idade))

@app.route("/3")
def mae():
    name = "katia"
    idade = "42"
    
    return(render_template("index.html",name=name,idade=idade))

@app.route("/2")
def amigo():
    name = "Pedro"
    idade = "16"
    
    return(render_template("index.html",name=name,idade=idade))

app.run()
