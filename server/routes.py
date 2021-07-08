from server import app

from flask import request


@app.route('/', methods =['POST', 'GET'])
def defult_route():
    if(request.method == 'POST'):
        return(f"{request.form['time']=},{request.form['message']=}")
    request_adress = request.remote_addr
    print(f"Worked, {request_adress=}")
    return "FAIL"