from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'age' : '39'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'age' : '47'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age' : '38'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'age' : '42'},
        {'first_name' : 'Chris','last_name' : 'Lugo', 'age' : '31'}
    ]
    return render_template("index.html",users=users)

if __name__=="__main__":
    app.run(debug=True)