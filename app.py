from flask import request, Flask,flash, render_template, jsonify, url_for,current_app
import database as bd
from forms import form_crear_usuario, form_editar_usuario, form_crear_habitacion, form_editar_habitacion, form_crear_administrador
from settings.config import configuracion
import os
from werkzeug.utils import secure_filename
import pickle



app = Flask(__name__)
app.config.from_object(configuracion)
app.config['UPLOAD_FOLDER'] = './static/images'


#Vista de los superAdministradores
@app.route('/super_administrador')
def super_administrador():
    lista_Administradores= bd.sql_select_admins()
    flash=("Lista de administradores:")
    return render_template('superAdministrador.html',t_administradores=lista_Administradores,titulo= "Super administrador")


#Vista de los administradores
@app.route('/')
def api():
    return render_template("IniciarSesion.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    database=bd.sql_login_usuarios(name1)
    if int(len(database))!=1 or name1 != str(database[0][0]):
        return render_template('IniciarSesion.html',info='Usuario No existe')
    else:
        if str(database[0][1])!=pwd:
            return render_template('IniciarSesion.html',info='Contraseña Incorrecta')
        else:
	        return render_template('index.html',name=name1)


#@app.route('/')
#def api():
#    return render_template('index.html',titulo="Administrar")

@app.route('/index_user')
def index_user():
    lista_Usuarios = bd.sql_select_usuarios()
    flash("Lista de usuarios")
    return render_template('index_user.html',t_usuarios=lista_Usuarios,titulo="Usuarios")

@app.route('/agregar_user',methods=['GET', 'POST'])
def nuevo_user():
    if request.method == 'GET':
        form = form_crear_usuario()
        return render_template('agregar_user.html',form=form,titulo="Registrar nuevo usuario")
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_insert_usuarios(nombre,cedula,correo,telefono,ciudad)
        flash(f'Usuario {nombre} registrado con exito!')
        lista_Usuarios = bd.sql_select_usuarios()
        return render_template('index_user.html',t_usuarios=lista_Usuarios,titulo="Usuarios")

@app.route('/editar_user/<string:id>',methods=['GET', 'POST'])
def editar_user(id):
    if request.method == 'GET':
        form = form_editar_usuario()
        user = bd.sql_buscar_usuarios(id)
        return render_template('editar_user.html',datos=user,form=form,titulo="Editar usuario "+id)
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_update_usuarios(id,nombre,cedula,correo,telefono,ciudad)
        flash(f'Usuario {nombre} modificado con exito!')
        lista_Usuarios = bd.sql_select_usuarios()
        return render_template('index_user.html',t_usuarios=lista_Usuarios,titulo="Usuarios")

@app.route('/eliminar_user/<string:id>',methods=['GET'])
def eliminar_user(id):
    bd.sql_delete_usuarios(id)
    flash(f'el usuario {id} fue eliminado con exito!')
    lista_Usuarios = bd.sql_select_usuarios()
    return render_template('index_user.html',t_usuarios=lista_Usuarios,titulo="Usuarios")

@app.route('/index_habitacion')
def index_habitacion():
    lista_Habitaciones = bd.sql_select_habitaciones()
    flash("Lista de Habitaciones")
    return render_template('index_habitacion.html',t_habitaciones=lista_Habitaciones,titulo="Habitaciones")

@app.route('/agregar_hab',methods=['GET', 'POST'])
def nueva_hab():
    if request.method == 'GET':
        form = form_crear_habitacion()
        return render_template('agregar.html',form=form,titulo="Crear nueva habitacion")
    if request.method == 'POST':
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        capacidad= request.form["capacidad"]
        precio= request.form["precio"]
        f = request.files["foto"]
        filename = secure_filename(f.filename)
        foto=filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        bd.sql_insert_habitacion(nombre,descripcion,capacidad,precio,foto)
        flash(f'Habitacion {nombre} creada con exito!')
        lista_Habitaciones = bd.sql_select_habitaciones()
        return render_template('index_habitacion.html',t_habitaciones=lista_Habitaciones,titulo="Habitaciones")

@app.route('/editar_hab/<string:id>',methods=['GET', 'POST'])
def editar_hab(id):
    if request.method == 'GET':
        form = form_editar_habitacion()
        hab = bd.sql_buscar_habitacion(id)
        return render_template('editar.html',datos=hab,form=form,titulo="Editar Habitacion "+id)
    if request.method == 'POST':
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        capacidad= request.form["capacidad"]
        precio= request.form["precio"]
        bd.sql_update_habitacion(id,nombre,descripcion,capacidad,precio)
        flash(f'Habitacion {nombre} modificada con exito!')
        lista_Habitaciones = bd.sql_select_habitaciones()
        return render_template('index_habitacion.html',t_habitaciones=lista_Habitaciones,titulo="Habitaciones")

@app.route('/eliminar_hab/<string:id>',methods=['GET'])
def eliminar_habitacion(id):
    bd.sql_delete_habitacion(id)
    flash(f'la habitacion {id} fue eliminada con exito!')
    lista_Habitaciones = bd.sql_select_habitaciones()
    return render_template('index_habitacion.html',t_habitaciones=lista_Habitaciones,titulo="Habitaciones")
    
app.run(debug=True)