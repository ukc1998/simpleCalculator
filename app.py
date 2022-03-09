from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/simpleCalculator', methods=['POST'])
def math_Operations():
    if (request.method=='POST'):
        operation = request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='Addition'):
            r=num1+num2
            result = 'The sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'Subtraction'):
            r = num1 - num2
            result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'Multiplication'):
            r = num1 * num2
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'Division'):
            r = num1 / num2
            result = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)

        return render_template('results.html',result=result)



if __name__ == '__main__':
    app.run()
