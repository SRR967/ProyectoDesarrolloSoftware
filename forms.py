from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class form_crear_usuario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    cedula = StringField('Cedula', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    enviar = SubmitField('Crear Usuario')

class form_editar_usuario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    cedula = StringField('Cedula', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    enviar = SubmitField('Editar Usuario')

class form_crear_habitacion(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    capacidad = StringField('Capacidad', validators=[DataRequired()])
    precio = StringField('Precio', validators=[DataRequired()])
    foto = FileField('Foto', validators=[DataRequired()])
    enviar = SubmitField('Crear Habitacion')

class form_editar_habitacion(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    capacidad = StringField('Capacidad', validators=[DataRequired()])
    precio = StringField('Precio', validators=[DataRequired()])
    enviar = SubmitField('Editar Habitacion')