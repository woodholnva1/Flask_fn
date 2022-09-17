import sqlite3
from unittest import result


class database():

    def __init__(self):
        
        #Conexion a la BD
        self.__conn = sqlite3.connect('formularios.db',check_same_thread=False)
        self.__cursor = self.__conn.cursor()       

    #Recibir diccionario desde POST en Insertar en BD
    def insert_form(self,param):

        dictionario = param  
        
        self.__cursor.execute('''insert into registro_form(email,edad,redPreferida,tmpFacebook,
        TmpWhasap,tmpTwitter,tmpInsta,tmpTiktok,sexo) 
        VALUES (:email,
        :edad,
        :redFavorita,
        :tmpFacebook,
        :tmpWhatsApp,
        :tmpTwitter,
        :tmpInstagram,
        :tmpTiktok,
        :sexo)''',dictionario)

        self.__conn.commit()
        return "Datos Insertados"
    
    #Realizar consultas a la BD para las Estaditicas   
    def Consulta_sql(self):
        self.__cursor.execute('''SELECT redPreferida,COUNT(*) AS CONTEO FROM 
        registro_form GROUP BY redPreferida 
        ORDER BY redPreferida''')
        results = self.__cursor.fetchall()
        return dict(results)


    #Realizar consultas al BD / Armar Diccionario para la Grafica
    def Consulta_sql_2(self):
        self.__cursor.execute('''SELECT redPreferida,COUNT(*) AS CONTEO FROM 
                                registro_form where edad = '18-25' GROUP BY EDAD,redPreferida 
                                ORDER BY REDPREFERIDA''')
        Edad_1 = self.__cursor.fetchall()


        self.__cursor.execute('''SELECT redPreferida,COUNT(*) AS CONTEO FROM 
                                registro_form where edad = '26-33' GROUP BY EDAD,redPreferida 
                                ORDER BY REDPREFERIDA''')
        Edad_2 = self.__cursor.fetchall()


        self.__cursor.execute('''SELECT redPreferida,COUNT(*) AS CONTEO FROM 
                                registro_form where edad = '34-40' GROUP BY EDAD,redPreferida 
                                ORDER BY REDPREFERIDA''')
        Edad_3 = self.__cursor.fetchall()
    
        self.__cursor.execute('''SELECT redPreferida,COUNT(*) AS CONTEO FROM 
                                registro_form where edad = '40+' GROUP BY EDAD,redPreferida 
                                ORDER BY REDPREFERIDA''')
        Edad_4 = self.__cursor.fetchall()

        results = {
            "Edad_1":dict(Edad_1),
            "Edad_2":dict(Edad_2),
            "Edad_3":dict(Edad_3),
            "Edad_4":dict(Edad_4)
        }
        
        return results
    


