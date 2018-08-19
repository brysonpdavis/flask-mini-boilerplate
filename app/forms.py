from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    fst_handle = StringField('First Twitter Handle', validators =[DataRequired()])
    snd_handle = StringField('Second Twitter Handle', validators =[DataRequired()])
    submit = SubmitField('Analyze!')