import mysql.connector

class Componentes:

    
    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root", 
        passwd="Semeolvido1*", database="Lab_Inventario")

    #EQUIPOSSQL--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    def consulta_equipos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM registro_equipos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


    def buscar_equipos(self, Id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM registro_equipos WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()     
        return datos 
    
    def inserta_equipos(self,serialeq, nombreeq, marcaeq, caraceq, obseq,canteq):
        cur = self.conexion.cursor()
        sql='''INSERT INTO registro_equipos (serialeq, nombreeq, marcaeq, caraceq, obseq,canteq) 
        VALUES('{}', '{}','{}', '{}','{}','{}')'''.format(serialeq, nombreeq, marcaeq, caraceq, obseq,canteq)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    

    def elimina_equipos(self,Id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM registro_equipos WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return n  



    def modifica_equipos(self,Id,serialeq, nombreeq, marcaeq, caraceq, obseq,canteq):
        cur = self.conexion.cursor()
        sql ='''UPDATE registro_equipos SET  serialeq ='{}', nombreeq = '{}' , marcaeq = '{}', caraceq = '{}',  obseq='{}', canteq = '{}'WHERE Id = '{}' '''.format(serialeq, nombreeq, marcaeq, caraceq, obseq,canteq, Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  
    def Retornarserialeq(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_equipos where serialeq= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos

    def Retornarnombreeq(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_equipos where nombreeq= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos

    def Retornarmarcaeq(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_equipos where marcaeq= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos

    #SUSTANCIASSQL-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def consulta_reactivos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM registro_reactivos" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


    def buscar_reactivos(self, Id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM registro_reactivos WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()     
        return datos 
    
    def inserta_reactivos(self,codigoreac,nombrereac,ubireac,pelireac,pesoreac,u_medida,numcas,cantreac):
        cur = self.conexion.cursor()
        sql='''INSERT INTO registro_reactivos (codigoreac,nombrereac,ubireac,pelireac,pesoreac,u_medida,numcas,cantreac) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}')'''.format(codigoreac,nombrereac,ubireac,pelireac,pesoreac,u_medida,numcas,cantreac)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def elimina_reactivos(self,Id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM registro_reactivos WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return n  



    def modifica_reactivos(self,Id,codigoreac,nombrereac,ubireac,pelireac,pesoreac,u_medida,numcas,cantreac):
        cur = self.conexion.cursor()
        sql ='''UPDATE registro_reactivos SET  codigoreac ='{}', nombrereac = '{}' , ubireac = '{}', pelireac = '{}',  pesoreac='{}',u_medida='{}',numcas='{}', cantreac = '{}'WHERE Id = '{}' '''.format(codigoreac,nombrereac,ubireac,pelireac,pesoreac,u_medida,numcas,cantreac, Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  

    def Retornarcodreac(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_reactivos where codigoreac= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos

    def Retornarnombrereac(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_reactivos where nombrereac= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos

    def Retornarubireac(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_reactivos where ubireac= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos


    #MATERIALES-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def consulta_materiales(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM registro_materiales" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


    def buscar_materiales(self, Id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM registro_materiales WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()     
        return datos 
    
    def inserta_materiales(self,codigomat,nombremat,ubimat,material,obsmat,cantmat):
        cur = self.conexion.cursor()
        sql='''INSERT INTO registro_materiales (codigomat,nombremat,ubimat,material,obsmat,cantmat) 
        VALUES('{}', '{}','{}', '{}','{}','{}')'''.format(codigomat,nombremat,ubimat,material,obsmat,cantmat)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def elimina_materiales(self,Id):
        cur = self.conexion.cursor()
        sql='''DELETE FROM registro_materiales WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.conexion.commit()    
        cur.close()
        return n  



    def modifica_materiales(self,Id,codigomat,nombremat,ubimat,material,obsmat,cantmat):
        cur = self.conexion.cursor()
        sql ='''UPDATE registro_materiales SET  codigomat ='{}', nombremat = '{}' , ubimat = '{}', material = '{}', obsmat='{}', cantmat = '{}'WHERE Id = '{}' '''.format(codigomat,nombremat,ubimat,material,obsmat,cantmat, Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  

    def Retornarcodmat(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_materiales where codigomat= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos

    def Retornarnombremat(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_materiales where nombremat= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos

    def Retornarubimat(self,ref):
        cur=self.conexion.cursor()
        sql="select * from registro_materiales where ubimat= {}".format(ref)
        cur.execute(sql)
        datos=cur.fetchall()
        cur.close()
        return datos