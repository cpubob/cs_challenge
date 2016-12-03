from flask import Flask, render_template,request

app = Flask(__name__)
vars = {}

@app.route('/')
def get_root():
    return render_template("index.html", vars=vars)


@app.route('/', methods=['POST'])
def post_data():
    vars['solution'] = request.form['Solution']
    return render_template("index.html", vars=vars)

if __name__ == "__main__":
    app.run(debug=True)
