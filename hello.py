

from flask import Flask, render_template 

app = Flask(__name__)   
@app.route('/')
def parameter():
    return render_template('index.html',num1=8, num2=8)

 
@app.route('/<num>')
def parameter_one(num):
    return render_template('index.html',num1=int(num), num2=8 )

@app.route('/<number1>/<number2>')
def parameter_two(num1,num2):
    return render_template('index.html',num1=int(num1), num2=int(num2))
    




    
    


if __name__=="__main__":   
 app.run(debug=True)  