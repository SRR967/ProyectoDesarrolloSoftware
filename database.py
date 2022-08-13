import sqlite3 
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('baseDatos.db')
        return con
    except Error:
        print(Error)

def sql_select_admins():
    #strsql= ('INSERT INTO producto (id, nombre, precio, existencia) VALUES (?,?,?,?)',(id,nombre, precio, cantidad))
    strsql= ('SELECT * FROM Usuarios WHERE perfil="admin"')
    con= sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    administradores = cursor_Obj.fetchall()
    con.close()
    return administradores

def sql_buscar_admin(id):
    strsql="SELECT * FROM Usuarios WHERE perfil='admin' and id="+id
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    administradores = cursor_Obj.fetchall()
    con.close()
    return administradores

def sql_insert_admin(nombre,cedula,correo,telefono,ciudad):
    strsql="INSERT INTO Usuarios (nombre,cedula,correo,telefono,ciudad,contrasena,perfil) VALUES('"+nombre+"', '"+cedula+"', '"+correo+"', '"+telefono+"', '"+ciudad+"', '"+cedula+"','admin');"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_update_admin(id,nombre,cedula,correo,telefono,ciudad):
    strsql="UPDATE Usuarios SET nombre = '"+nombre+"', cedula = '"+cedula+"', correo = '"+correo+"', telefono = '"+telefono+"', ciudad = '"+ciudad+"' WHERE  perfil='admin' and id = "+id+";"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_admin(id):
    strsql="DELETE FROM Usuarios WHERE  perfil='admin' and id = "+id+";"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

#----------------------------------------------------------------

def sql_select_superAdmin():
    strsql= ('SELECT * FROM Usuarios WHERE perfil="super"')
    con= sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    administradores = cursor_Obj.fetchall()
    con.close()
    return administradores

def sql_insert_superAdmin(nombre,cedula,correo,telefono,ciudad):
    strsql="INSERT INTO Usuarios (nombre,cedula,correo,telefono,ciudad,contrasena,perfil) VALUES('"+nombre+"', '"+cedula+"', '"+correo+"', '"+telefono+"', '"+ciudad+"', '"+cedula+"','super');"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_buscar_superAdmin(id):
    strsql="SELECT * FROM Usuarios WHERE perfil='super' and id="+id
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    superAdministradores = cursor_Obj.fetchall()
    con.close()
    return superAdministradores

def sql_update_superAdmin(id,nombre,cedula,correo,telefono,ciudad):
    strsql="UPDATE Usuarios SET nombre = '"+nombre+"', cedula = '"+cedula+"', correo = '"+correo+"', telefono = '"+telefono+"', ciudad = '"+ciudad+"'  WHERE perfil='super' and id = "+id+";"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_delete_superAdmin(id):
    strsql="DELETE FROM Usuarios WHERE perfil='super' and  = "+id+";"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

#----------------------------------------------------------------

def sql_select_usuarios():
    strsql="SELECT * FROM Usuarios WHERE perfil='usuario';"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    usuarios = cursor_Obj.fetchall()
    con.close()
    return usuarios

def sql_login_usuarios(user):
    strsql="SELECT correo,contrasena,perfil,id,nombre FROM Usuarios WHERE correo='"+user+"'"
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
    strsql="INSERT INTO Usuarios (nombre,cedula,correo,telefono,ciudad,contrasena,perfil) VALUES('"+nombre+"', '"+cedula+"', '"+correo+"', '"+telefono+"', '"+ciudad+"', '"+cedula+"','usuario');"
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

#----------------------------------------------------------------

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

def sql_select_reservaciones():
    strsql="SELECT * FROM Reservaciones;"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    reservacion = cursor_Obj.fetchall()
    con.close()
    return reservacion

def sql_reserva(id,id_hab,fecha_entrada,fecha_salida,comentarios):
    strsql="INSERT INTO Reservas (id_user,id_habitacion,fecha_entrada,fecha_salida,comentarios) VALUES('"+id+"', '"+id_hab+"', '"+fecha_entrada+"', '"+fecha_salida+"', '"+comentarios+"');"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()

def sql_buscar_reservas(id):
    strsql="SELECT * FROM Reservas WHERE id_user="+id
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion