from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def get_root():
    vars = {}
    vars['price'] = 75.23
    vars['frameworks'] = ['flask', 'django', 'rails']
    return render_template("index.html", vars=vars)


@app.route('/search')
def get_data():
    query  = request. args.get('q')
    return 'You just searched for %s' % query

@app.route('/search', methods=['POST'])
def post_data():
    username = request.headers.get('Username')
    password = request.headers.get('Password')

    print username

    return '<p>You have successfully logged in as %s' % username

if __name__ == "__main__":
    app.run(debug=True)
