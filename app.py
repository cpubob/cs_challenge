from flask import Flask, render_template,request

app = Flask(__name__)
vars = {}


@app.route('/')
def get_root():
    vars['solution'] = None
    vars['response'] = None

    return render_template("index.html", vars=vars)


@app.route('/', methods=['POST'])
def post_data():
    vars['solution'] = request.form['Solution']
    vars['response'] = 'Success'
    return render_template("index.html", vars=vars)

if __name__ == "__main__":
    app.run(debug=True)
