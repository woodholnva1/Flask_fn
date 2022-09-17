
from unittest import result
from flask import Flask,render_template,abort,request,flash,redirect,session
from classes import database
from utils import is_valid_email

app = Flask(__name__)
app.secret_key = "super secret key"

#--------------------------------
#Definir objetos de Clase:
Objeto_bd = database()


#---------------------------------------
#vistas de la web
@app.route('/')
def Principal():
    return render_template('index.html')


#------------------------------------------------------------
#Vista del formulario de Cuestionario
#------------------------------------------------------------

@app.route('/formulario',methods=['GET','POST'])
def Formulario():

    #Obtener Variables del Formulario
    if request.method == 'POST':

        req = request.form

        Datos_form = {
        "email":req.get('email'),
        "edad": req.get('edad'),
        "redFavorita": req.get('redFavorita'),
        "tmpFacebook": req.get('tmpFacebook'),
        "tmpWhatsApp": req.get('tmpWhatsApp'),
        "tmpTwitter": req.get('tmpTwitter'),
        "tmpInstagram": req.get('tmpInstagram'),
        "tmpTiktok": req.get('tmpTiktok'),
        "sexo": req.get('value_sex')
    }


        # Control de excepcionas al Registrar Formulario
        try:
            if is_valid_email(Datos_form["email"]):
                resultado = Objeto_bd.insert_form(Datos_form)
                print(resultado)
                return render_template('succes.html',data=Datos_form)
            else:
             flash("El Correo es Invalido")
             return redirect(request.url)

        #En caso de Error por constrain indicar mensaje
        except:
            flash("El Correo ya se encuentra Registrado")
            return redirect(request.url)

    #Variables Para los combo del formulario
    Data_dict = {
    "horas": [1,2,3,4,5,8,10],
    "redes": ["Facebook","Whatsapp","Twitter","Instagram","Tiktok"],
    "sexo": ["Masculino","Femenino","Otros"]
    }

    return render_template('formulario.html',data=Data_dict)



#Vista de Estadisticas
@app.route('/estadisticas')
def estadisticas():

    resultado = Objeto_bd.Consulta_sql()
    resultado_2 = Objeto_bd.Consulta_sql_2()

    lista = []

    for i in resultado.keys():
        lista.append(i)

    return render_template('estadisticas.html',chart1=resultado,lista=lista,chart2=resultado_2)


@app.route('/error')
def error():
    abort(401)


#Main
if __name__=='__main__':
	app.run(debug=True)