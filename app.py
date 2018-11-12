from flask import render_template, url_for, flash, request, g
from flask import Flask, redirect
from forms import Searchform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/forecasting', methods=['GET', 'POST'])
def forecasting():
    return render_template('forecasting.html', title='Forecasting')

@app.route('/new_prod', methods=['GET', 'POST'])
def new_prod():
    form = Searchform()
    if request.method == 'POST' and form.validate():
        return 'hello'
    return render_template('new_prod.html', title='New Product', form = form)

@app.route('/revenue', methods=['GET', 'POST'])
def revenue():
    return render_template('revenue.html', title='Revenue')

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0')
