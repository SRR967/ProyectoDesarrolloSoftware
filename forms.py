from flask_wtf import FlaskForm
from wtforms import DateField,StringField, FileField, SubmitField, EmailField, PasswordField
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

class form_crear_administrador(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    cedula= StringField('Cedula', validators=[DataRequired()])
    correo= EmailField('Correo', validators=[DataRequired()])
    telefono= StringField('Telefono', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    enviar= SubmitField('Crear administrador')

class form_editar_admin(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    cedula = StringField('Cedula', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    enviar = SubmitField('Editar administrador')

class form_crear_superAdmin(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    cedula= StringField('Cedula', validators=[DataRequired()])
    correo= EmailField('Correo', validators=[DataRequired()])
    telefono= StringField('Telefono', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    enviar= SubmitField('Crear super administrador')

class form_editar_superAdmin(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    cedula = StringField('Cedula', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    ciudad = StringField('Ciudad', validators=[DataRequired()])
    enviar = SubmitField('Editar super administrador')

class form_reservacion(FlaskForm):
    fecha_entrada = DateField('Fecha entrada', validators=[DataRequired()])
    fecha_salida = DateField('Fecha salida', validators=[DataRequired()])
    comentarios = StringField('comentarios', validators=[DataRequired()])
    enviar = SubmitField('Realizar Reserva')