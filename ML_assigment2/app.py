from flask import Flask,render_template

app = Flask(__name__)

@app.route("/", methods =['GET','POST'])

def home_page():

    return render_template('index.html')

@app.route("/predict",methods = ['POST'])
def affair():
    if (request.method == 'POST'):
        num1 = int(request.form['num1'])
        # print(prd[num1])
        result = num1
        return render_template('results.html', num1=num1, result=result)




if __name__ =="__main__":

    app.run()
