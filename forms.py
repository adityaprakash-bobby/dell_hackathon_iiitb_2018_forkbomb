from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class Searchform(FlaskForm):
    inches = SelectField('Inches', choices = [(11.6, '11.6'), (12.5, '12.5'), (13.3, '13.3'), (14, '14'), (15, '15'), (15.6, '15.6'), (17, '17')])
    resolution = SelectField('Resolution', choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    processor = SelectField('Processor', choices = [(1, '1'), (2, '2'), (3, '3')])
    clockspeed = SelectField('ClockSpeed', choices = [(2, '2'), (2.5, '2.5'), (3, '3')])
    gpu = SelectField('GPU', choices = [(1, '1'), (2, '2'), (3, '3')])
    weight = SelectField('Weight', choices = [(1.8, '1.8'), (2.3, '2.3'), (2.7, '2.7')])
    price = SelectField('Price', choices = [(500, '500'), (750, '750'), (1000, '1000')])
    submit = SubmitField('Find')
