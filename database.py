import sqlite3 
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('baseDatos.db')
        return con
    except Error:
        print(Error)

def sql_select_usuarios():
    strsql="SELECT * FROM Usuarios;"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    usuarios = cursor_Obj.fetchall()
    con.close()
    return usuarios

def sql_login_usuarios(user):
    strsql="SELECT correo,contrasena FROM Usuarios WHERE correo='"+user+"'"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    usuarios = cursor_Obj.fetchall()
    con.close()
    return usuarios   

def sql_buscar_usuarios(id):
    strsql="SELECT * FROM Usuarios WHERE id="+id
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    usuarios = cursor_Obj.fetchall()
    con.close()
    return usuarios

def sql_insert_usuarios(nombre,cedula,correo,telefono,ciudad):
    strsql="INSERT INTO Usuarios (nombre,cedula,correo,telefono,ciudad,contrasena) VALUES('"+nombre+"', '"+cedula+"', '"+correo+"', '"+telefono+"', '"+ciudad+"', '"+cedula+"');"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_update_usuarios(id,nombre,cedula,correo,telefono,ciudad):
    strsql="UPDATE Usuarios SET nombre = '"+nombre+"', cedula = '"+cedula+"', correo = '"+correo+"', telefono = '"+telefono+"', ciudad = '"+ciudad+"' WHERE id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_usuarios(id):
    strsql="DELETE FROM Usuarios WHERE id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_select_habitaciones():
    strsql="SELECT * FROM Habitaciones;"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion

def sql_buscar_habitacion(id):
    strsql="SELECT * FROM Habitaciones WHERE id="+id
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion

def sql_insert_habitacion(nombre,descripcion,capacidad,precio,foto):
    strsql="INSERT INTO Habitaciones (nombre,descripcion,capacidad,precio,foto) VALUES('"+nombre+"', '"+descripcion+"', '"+capacidad+"', '"+precio+"', '"+foto+"');"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_update_habitacion(id,nombre,descripcion,capacidad,precio):
    strsql="UPDATE Habitaciones SET nombre = '"+nombre+"', descripcion = '"+descripcion+"', capacidad = '"+capacidad+"', precio = '"+precio+"' WHERE id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_habitacion(id):
    strsql="DELETE FROM Habitaciones WHERE id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

