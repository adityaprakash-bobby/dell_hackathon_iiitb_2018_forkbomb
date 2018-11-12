from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class Searchform(FlaskForm):
    inches = SelectField('Inches', choices = [(11.6, '11.6inch'), (12.5, '12.5inch'), (13.3, '13.3inch'), (14, '14inch'), (15, '15inch'), (15.6, '15.6inch'), (17, '17inch')])
    resolution = SelectField('Resolution', choices = [(1, 'Full HD'), (2, 'HD'), (3, 'IPS Panel'), (4, 'IPS Panel Full HD'), (5, '4K HD')])
    processor = SelectField('Processor', choices = [(1, 'i3'), (2, 'i5'), (3, 'i7')])
    clockspeed = SelectField('ClockSpeed', choices = [(2, '2.0GHz'), (2.5, '2.5GHz'), (3, '3.0GHz')])
    gpu = SelectField('GPU', choices = [(1, 'AMD'), (2, 'Intel'), (3, 'Nvidia')])
    weight = SelectField('Weight', choices = [(1.8, '1.8kg'), (2.3, '2.3kg'), (2.7, '2.7kg')])
    price = SelectField('Price', choices = [(300, '$300'),(460, '$460'),(350, '$350'),(500, '$500'), (750, '$750'), (1000, '$1000')])
    submit = SubmitField('Find')

class CountryForm(FlaskForm):
    country = SelectField('Country', choices = [('uk', 'United Kingdom'), ('india','India'), ('japan','Japan'), ('us', 'United States')])
    submit = SubmitField('Choose')
