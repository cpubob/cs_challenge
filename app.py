import requests
from flask import Flask, render_template,request,jsonify
import challenges
import ast

challenge = [{
    'test':'for t in [[1.05,1],[1.25,1.25],[-1.26,-1.25],[.38,.5]]:\n  print g(t[0]) == t[1]',
    'description': 'Given a numbers, a, return its value to the nearest quarter.',
    'baseSolution': 'def g(a):\n  #TODO Your solution here\n',
    }]



app = Flask(__name__)
vars = {}
vars['challengeNum'] = challenges.ChallengeOne().name
vars['challenge'] =  challenges.ChallengeOne().description
vars['tests'] = ast.literal_eval(challenges.ChallengeOne().tests)
vars['response'] = None



@app.route('/')
def get_root():
    vars['solution'] = challenges.ChallengeOne().base
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
    testCode = userCode + "\n" + challenges.ChallengeOne().testing

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
        vars['response'] = "Success!!!" + "\n"

    vars['solution'] = request.form['Solution']
    return render_template("index.html", vars=vars)

if __name__ == "__main__":
    app.run(debug=True)
