from flask import render_template, url_for, flash, request, g
from flask import Flask, redirect
from forms import Searchform, CountryForm
from ratingF import *
from revenueServices import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('home.html')

@app.route('/')
@app.route('/forecasting', methods=['GET', 'POST'])
def forecasting():
    return render_template('forecasting.html', title='Forecasting')

@app.route('/new_prod', methods=['GET', 'POST'])
def new_prod():
    form = Searchform()

    if request.method == 'GET' and request.args.get('submit') == 'Find':
        inches = request.args.get('inches')
        gpu = request.args.get('gpu')
        resolution = request.args.get('resolution')
        processor = request.args.get('processor')
        weight = request.args.get('weight')
        price = request.args.get('price')
        clockspeed = request.args.get('clockspeed')
        copy = [ inches, gpu, processor, resolution, weight, clockspeed, price]
        val = rating(copy)
        return render_template('new_prod.html', title = 'New Product', val = val, form=form, req = request.args)
    return render_template('new_prod.html', title='New Product', form = form)

@app.route('/revenue', methods=['GET', 'POST'])
def revenue():
    form = CountryForm()
    if request.method == 'GET' and request.args.get('submit') == 'Choose':
        country = request.args.get('country')
        data = get(country)
        return render_template('revenue.html', title='Revenue', data = data, form = form, country=country)
    return render_template('revenue.html', title='Revenue', form = form)

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0')
