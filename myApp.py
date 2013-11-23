from bottle import route, run, get, post, request


@route('/login')
def Login():
    return """ <form method="post">
        enter your name : <input type="text" name="username"/><br>
        enter your password : <input type="password" name="password"/><br>
        <input type="submit" name="submit"/>
        </form>"""

@post('/login') 
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    if username==password :
        return True
    else:
        return False
run(host='localhost', port=8080,
    debug=True, reloader=True)