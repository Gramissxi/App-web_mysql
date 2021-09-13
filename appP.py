from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_mysqldb import MySQL 

appP=Flask(__name__)

#mysqlconnexion

appP.config[ "MYSQL_HOST"]='localhost'
appP.config[ "MYSQL_USER"]='root'
appP.config[ "MYSQL_PASSWORD"]='43319717'
appP.config[ "MYSQL_DB"]='patio_de_los_lecheros'

mysql=MySQL(appP)

#SETTINGS
appP.secret_key=" mysecretkey"

@appP.route('/') 
def Index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT *FROM fichero ")
    data= cur.fetchall()
    print(data)
    return render_template("index.html", contactos= data)


@appP.route('/add_contact', methods= ["POST"])
def add_contact():
    if request.method== "POST":
      nombre= request.form["Nombre"]
      apellido= request.form["Apellido"]
      telefono= request.form["Teléfono"]
      email= request.form["Email"]
      direccion= request.form["Dirección"]
      areadetrabajo= request.form["Área"]
      cur= mysql.connection.cursor()
      cur.execute("INSERT INTO fichero (Nombre, Apellido, Teléfono, Email, Dirección, Área ) VALUES (%s, %s, %s, %s, %s, %s)",
      (nombre,apellido,telefono,email,direccion,areadetrabajo))
      mysql.connection.commit()
      flash("Empleado agregado correctamente")
      return redirect(url_for("Index"))

@appP.route('/edit/<id>')
def get_contact(id):
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM fichero WHERE id = %s", (id))
    data= cur.fetchall()
    return render_template("editar-contactos.html", contact= data[0])
   
@appP.route("/update/<id>", methods= ["POST"])
def update_contact(id):
    if request.method == "POST":
       nombre = request.form ["Nombre"]
       apellido = request.form ["Apellido"]
       telefono = request.form ["Teléfono"]
       email = request.form ["Email"]
       direccion = request.form ["Dirección"]
       areadetrabajo = request.form["Área"]
       cur = mysql.connection.cursor()
       cur.execute("""
         UPDATE fichero
         SET  Nombre = %s,
              Apellido = %s,
              Teléfono= %s 
              Dirección= %s
              Email= %s
              areadetrabajo= %s            
         WHERE id = %s
       """, (nombre, apellido, telefono, direccion, email,areadetrabajo, id))
       mysql.connection.commit()
       flash("Empleado actualizado")
       return  redirect (url_for("Index"))

@appP.route('/delete/<string:id>')
def delete_contact(id):
    cur= mysql.connection.cursor()
    cur.execute("DELETE FROM fichero WHERE id= {0}" .format(id))
    mysql.connection.commit()
    flash("Contacto borrado sactifactoriamente")
    return redirect (url_for("Index"))

    

@appP.route
def buscar():
  pass

if __name__=='__main__':
  appP.run(port=3000, debug= True) #parametros