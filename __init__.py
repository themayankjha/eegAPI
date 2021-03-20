from flask import Flask,jsonify, make_response,request,render_template
from functions import databaseentry,databaseinfogather

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "This is not a gateway, please send data to /input or request data from /output"


@app.route('/input', methods=['GET'])
def enter():
    try:
        username=request.args.get("username")
        attention=request.args.get("attention")
        meditation=request.args.get("meditation")
        output=databaseentry(username,attention,meditation)
        return make_response(jsonify(output), 200)
    except:
        params = dict()
        (params['code'])=("unsuccessful")
        return make_response(jsonify(params), 200)




@app.route('/output', methods=['GET'])
def heartandstrokedata():
        username=request.args.get("username")
        output=databaseinfogather(username)
        return make_response(jsonify(output), 200)

if __name__ == '__main__':
    app.debug = True
    app.run()
