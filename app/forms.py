from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField('Admin Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

class NewItem(FlaskForm):
    device = StringField('Device', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Item')

class NewComponent(FlaskForm):
    part = StringField('Part', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Item')