from flask import Flask, request, make_response,redirect,abort
from flask_script import Manager

app=Flask(__name__)
manager=Manager(app)
@app.route('/')
def index():
    # user_agent=request.headers.get('User-Agent')
    # return '<p>Your browser is {0}</p>'.format(user_agent)
    # response=make_response('<h1>take a cookie</h1>')
    # response.set_cookie('answer','42')
    # return response
    return redirect('http://www.baidu.com')
@app.route('/ss/<name>')
def user(name):
    if not name:
        abort(405)
    return '<h1>Hello {0}</h1>'.format(name)
@app.route('/404')
def FOF():
    return '<h2>Bad Request</h2>',404
if __name__=='__main__':
    # app.run(debug=True)
    manager.run()