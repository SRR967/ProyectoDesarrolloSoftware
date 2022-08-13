from flask import request, Flask,flash, render_template, jsonify, url_for,current_app
import database as bd
from forms import form_crear_usuario, form_editar_usuario, form_crear_habitacion, form_editar_habitacion,form_crear_administrador, form_editar_admin,form_crear_superAdmin,form_editar_superAdmin, form_reservacion
from settings.config import configuracion
import os
from werkzeug.utils import secure_filename
import pickle



app = Flask(__name__)
app.config.from_object(configuracion)
app.config['UPLOAD_FOLDER'] = './static/images'


#Vista de los superAdministradores
@app.route('/super_administrador/<string:id>')
def super_administrador(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    return render_template('SuperAdministrador.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,titulo= "Super administrador")

@app.route('/index_superAdmin/<string:id>')
def index_superAdmin(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    lista_superAdministradores= bd.sql_select_superAdmin()
    flash=("Lista de Super Administradores")
    return render_template('index_superAdmin.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_superAdmin= lista_superAdministradores)

@app.route('/agregar_superAdmin',methods=['GET', 'POST'])
def agregar_superAdmin():
    if request.method == 'GET':
        form = form_crear_superAdmin()
        return render_template('agregar_superAdmin.html',form=form,titulo="Registrar nuevo  super administrador")
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_insert_superAdmin(nombre,cedula,correo,telefono,ciudad)
        flash(f'Super Administrardor {nombre} registrado con exito!')
        lista_superAdmin = bd.sql_select_superAdmin()
        return render_template('index_superAdmin.html',t_superAdmin=lista_superAdmin,titulo="Registro super Administradores")


@app.route('/editar_superAdmin/<string:id>',methods=['GET', 'POST'])
def editar_superAdmin(id):
    if request.method == 'GET':
        form = form_editar_superAdmin()
        admin = bd.sql_buscar_superAdmin(id)
        return render_template('editar_superAdmin.html',datos=admin,form=form,titulo="Editar super administrador "+id)
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_update_superAdmin(id,nombre,cedula,correo,telefono,ciudad)
        flash(f'Super Administrador {nombre} modificado con exito!')
        lista_Admin = bd.sql_select_superAdmin()
        return render_template('index_superAdmin.html',t_superAdmin=lista_Admin,titulo="Super Administradores")

@app.route('/eliminar_superAdmin/<string:id>',methods=['GET'])
def eliminar_superAdmin(id):
    bd.sql_delete_superAdmin(id)
    flash(f'el super Administrador {id} fue eliminado con exito!')
    lista_admins = bd.sql_select_superAdmin()
    return render_template('index_superAdmin.html',t_superAdmin=lista_admins,titulo="Super Administradores")


#----------------------------------------------------------------
@app.route('/index_admin/<string:id>')
def index_admin(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    lista_Administradores= bd.sql_select_admins()
    flash=("Lista de administradores:")
    return render_template('index_admin.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user, t_administradores= lista_Administradores)

@app.route('/editar_admin/<string:id>',methods=['GET', 'POST'])
def editar_admin(id):
    if request.method == 'GET':
        form = form_editar_admin()
        admin = bd.sql_buscar_admin(id)
        return render_template('editar_admin.html',datos=admin,form=form,titulo="Editar administrador "+id)
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_update_admin(id,nombre,cedula,correo,telefono,ciudad)
        flash(f'Administrador {nombre} modificado con exito!')
        lista_Admin = bd.sql_select_admins()
        return render_template('index_admin.html',t_administradores=lista_Admin,titulo="Administradores")

@app.route('/agregar_admin',methods=['GET', 'POST'])
def agregar_admin():
    if request.method == 'GET':
        form = form_crear_administrador()
        return render_template('agregar_admin.html',form=form,titulo="Registrar nuevo administrador")
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_insert_admin(nombre,cedula,correo,telefono,ciudad)
        flash(f'Administrardor {nombre} registrado con exito!')
        lista_Admin = bd.sql_select_admins()
        return render_template('index_admin.html',t_administradores=lista_Admin,titulo="Registro administradores")

@app.route('/eliminar_admin/<string:id>',methods=['GET'])
def eliminar_admin(id):
    bd.sql_delete_admin(id)
    flash(f'el Administrador {id} fue eliminado con exito!')
    lista_admins = bd.sql_select_usuarios()
    return render_template('index_admin.html',t_administradores=lista_admins,titulo="Administradores")


#----------------------------------------------------------------

@app.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')


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
        if pwd != str(database[0][1]):
            return render_template('IniciarSesion.html',info='Contraseña Incorrecta')
        else:
            if str(database[0][2])=='super':
                id_user=str(database[0][3])
                nombre_user=str(database[0][4])
                perfil=str(database[0][2])
                return render_template('superAdministrador.html',perfil=perfil,nombre=nombre_user,correo=name1,id_user=id_user,titulo="Hotel JW Marriott Marquis Dubai")
            elif str(database[0][2])=='admin':
                id_user=str(database[0][3])
                nombre_user=str(database[0][4])
                perfil=str(database[0][2])
                return render_template('index.html',perfil=perfil,nombre=nombre_user,correo=name1,id_user=id_user,titulo="Hotel JW Marriott Marquis Dubai")
            else:
                id_user=str(database[0][3])
                nombre_user=str(database[0][4])
                perfil=str(database[0][2])
                return render_template('Usuarios.html',perfil=perfil,nombre=nombre_user,correo=name1,id_user=id_user,titulo="Hotel JW Marriott Marquis Dubai")


@app.route('/index/<string:id>')
def index1(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    return render_template('index.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/index_user/<string:id>')
def index_user(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    lista_Usuarios = bd.sql_select_usuarios()
    flash("Lista de usuarios")
    return render_template('index_user.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_usuarios=lista_Usuarios,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/agregar_user/<string:id>',methods=['GET', 'POST'])
def nuevo_user(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    if request.method == 'GET':
        form = form_crear_usuario()
        return render_template('agregar_user.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,form=form,titulo="Hotel JW Marriott Marquis Dubai")
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_insert_usuarios(nombre,cedula,correo,telefono,ciudad)
        flash(f'Usuario {nombre} registrado con exito!')
        lista_Usuarios = bd.sql_select_usuarios()
        return render_template('index_user.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_usuarios=lista_Usuarios,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/editar_user/<string:id_u>/<string:id>',methods=['GET', 'POST'])
def editar_user(id_u,id):
    database=bd.sql_buscar_usuarios(id_u)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    if request.method == 'GET':
        form = form_editar_usuario()
        user = bd.sql_buscar_usuarios(id)
        return render_template('editar_user.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,datos=user,form=form,titulo="Editar usuario "+id)
    if request.method == 'POST':
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        correo= request.form["correo"]
        telefono= request.form["telefono"]
        ciudad= request.form["ciudad"]
        bd.sql_update_usuarios(id,nombre,cedula,correo,telefono,ciudad)
        flash(f'Usuario {nombre} modificado con exito!')
        lista_Usuarios = bd.sql_select_usuarios()
        return render_template('index_user.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_usuarios=lista_Usuarios,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/eliminar_user/<string:id_u>/<string:id>',methods=['GET'])
def eliminar_user(id_u,id):
    database=bd.sql_buscar_usuarios(id_u)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    bd.sql_delete_usuarios(id)
    flash(f'el usuario {id} fue eliminado con exito!')
    lista_Usuarios = bd.sql_select_usuarios()
    return render_template('index_user.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_usuarios=lista_Usuarios,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/index_habitacion/<string:id>')
def index_habitacion(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    lista_Habitaciones = bd.sql_select_habitaciones()
    flash("Lista de Habitaciones")
    return render_template('index_habitacion.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_habitaciones=lista_Habitaciones,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/agregar_hab/<string:id>',methods=['GET', 'POST'])
def nueva_hab(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    if request.method == 'GET':
        form = form_crear_habitacion()
        return render_template('agregar.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,form=form,titulo="Crear nueva habitacion")
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
        return render_template('index_habitacion.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_habitaciones=lista_Habitaciones,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/editar_hab/<string:id_u>/<string:id>',methods=['GET', 'POST'])
def editar_hab(id_u,id):
    database=bd.sql_buscar_usuarios(id_u)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    if request.method == 'GET':
        form = form_editar_habitacion()
        hab = bd.sql_buscar_habitacion(id)
        return render_template('editar.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,datos=hab,form=form,titulo="Editar Habitacion "+id)
    if request.method == 'POST':
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        capacidad= request.form["capacidad"]
        precio= request.form["precio"]
        bd.sql_update_habitacion(id,nombre,descripcion,capacidad,precio)
        flash(f'Habitacion {nombre} modificada con exito!')
        lista_Habitaciones = bd.sql_select_habitaciones()
        return render_template('index_habitacion.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_habitaciones=lista_Habitaciones,titulo="Hotel JW Marriott Marquis Dubai")

@app.route('/eliminar_hab/<string:id_u>/<string:id>',methods=['GET'])
def eliminar_habitacion(id_u,id):
    database=bd.sql_buscar_usuarios(id_u)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])
    perfil=str(database[0][7])
    bd.sql_delete_habitacion(id)
    flash(f'la habitacion {id} fue eliminada con exito!')
    lista_Habitaciones = bd.sql_select_habitaciones()
    return render_template('index_habitacion.html',perfil=perfil,nombre=nombre_user,correo=correo,id_user=id_user,t_habitaciones=lista_Habitaciones,titulo="Hotel JW Marriott Marquis Dubai")

#----------------------------------------------------------------
# Vista del usuario
@app.route('/inicio/<string:id>')
def inicio(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3])   
    return render_template('Usuarios.html',nombre=nombre_user,correo=correo,id_user=id_user,titulo="Inicio")

@app.route('/habitaciones/<string:id>')
def habitaciones(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3]) 
    lista_Habitaciones = bd.sql_select_habitaciones()
    flash("Lista de Habitaciones")
    return render_template('habitaciones.html',nombre=nombre_user,correo=correo,t_habitaciones=lista_Habitaciones,id_user=id,titulo="Habitaciones")

@app.route('/reservacion/<string:id>')
def reservacion(id):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3]) 
    lista_Habitaciones = bd.sql_buscar_reservas(id)
    return render_template('reservacion.html',nombre=nombre_user,correo=correo,id_user=id_user,t_reservacion=lista_Habitaciones,titulo="Reservaciones")

@app.route('/realizar_reserva/<string:id>/<string:id_hab>',methods=['GET', 'POST'])
def realizar_reserva(id,id_hab):
    database=bd.sql_buscar_usuarios(id)
    id_user=str(database[0][0])
    nombre_user=str(database[0][1])
    correo=str(database[0][3]) 
    if request.method == 'GET':
        form=form_reservacion()
        titulo="Reserva"
        return render_template('reserva.html',nombre=nombre_user,correo=correo,id_user=id,form=form,id_hab=id_hab,titulo=titulo)
    if request.method == 'POST':
        fecha_entrada = request.form["fecha_entrada"]
        fecha_salida = request.form["fecha_salida"]
        comentarios= request.form["comentarios"]
        bd.sql_reserva(id,id_hab,fecha_entrada,fecha_salida,comentarios)
        flash(f'la Habitacion {id_hab} fue reservada con exito')
        lista_Habitaciones = bd.sql_buscar_reservas(id)
        return render_template('reservacion.html',nombre=nombre_user,correo=correo,id_user=id_user,t_reservacion=lista_Habitaciones,titulo="Reservaciones")


app.run(debug=True)