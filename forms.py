from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CafeForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    precio = StringField('Precio',validators=[DataRequired()])
    ingredientes = StringField('Ingredientes',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar',render_kw={'class': 'submit-button'})