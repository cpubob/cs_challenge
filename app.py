import requests
from flask import Flask, render_template,request,jsonify

app = Flask(__name__)
vars = {}
vars['response'] = None

challengeTests = 'for t in [[[1,1],2],[[2,2],4]]:\n  print g(t[0][0], t[0][1]) == t[1]'

@app.route('/')
def get_root():
    vars['solution'] = None
    vars['response'] = None

    return render_template("index.html", vars=vars)

@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print content['src']
    return jsonify({"uuid":uuid})

@app.route('/', methods=['POST'])
def post_data():
    userCode = request.form['Solution']
    testCode = userCode + "\n" + challengeTests

    r = requests.post('http://rh-codeservice-vmengine1.appspot.com/src', data={
        "src": testCode,
        "status": 0,
    })

    if r.status_code != 200:
        vars['response'] = "Responses Code %s\n%s" % (r.status_code, r.text)

    for i, v in enumerate(r.text.split()):
        if v != "True":
            vars['response'] = "Test %s failed" % i
            break
    else:
        vars['response'] = "Success!!!"

    vars['solution'] = request.form['Solution']
    return render_template("index.html", vars=vars)

if __name__ == "__main__":
    app.run(debug=True)
