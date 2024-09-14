# from flask import Flask , abort

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return '<h1>Python Operations with Flask Routing and Views</h1>'

# @app.route('/print/<string:parameter>')
# def print_string(parameter):
#     print(parameter) 
  
#     return f'<h2>The parameter you entered is: {parameter}</h2>'


# @app.route('/count/<int:parameter>')
# def count(parameter):
    
#     numbers = ''.join(f'{i}<br>' for i in range(parameter + 1))
#     return f'<h2>Counting from 0 to {parameter}</h2><p>{numbers}</p>'


# @app.route('/math/<int:num1>/<operation>/<int:num2>')
# def math(num1, operation, num2):
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == 'div':
#         if num2 == 0:
#             abort(400, description="Division by zero is not allowed.")
#         result = num1 / num2 
#     elif operation == '%':
#         if num2 == 0:
#             abort(400, description="Division by zero is not allowed.")
#         result = num1 % num2
#     else:
#         abort(400, description="Invalid operation.")
    
#     return str(result)


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<abdi>')
def print_string(abdi):
    print("hello")
    return abdi


@app.route('/count/<int:number>')
def count(number):
    if number < 1:
        abort(400, description="Number must be a positive integer.")
  
    numbers = "\n".join(str(i) for i in range(number))
    return f'{numbers}\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            abort(400, description="Division by zero is not allowed.")
        result = num1 / num2 
    elif operation == '%':
        if num2 == 0:
            abort(400, description="Division by zero is not allowed.")
        result = num1 % num2
    else:
        abort(400, description="Invalid operation.")
    
    return str(result)  



if __name__ == '_main_':
    app.run(port=5555, debug=True)