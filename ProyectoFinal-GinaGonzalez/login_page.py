from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from Componentes import *

class login_page:
    comp=Componentes()
    def __init__(self, root):
        self.window = root
        self.window.title("LABIN")
        self.window.geometry("800x500")
        self.window.config(bg = "white")

        self.frame1 = Frame(self.window, bg='#F67000')
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= "LAB ", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=95,y=200
        )
        label2 = Label(self.frame1, text= "IN", font=("times new roman", 40, "bold"), bg="yellow", fg="RoyalBlue1").place(x=120,y=270)

        self.frame2 = Frame(self.window, bg = "#5F88AB")
        self.frame2.place(x=300,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=50,y=100,width=400,height=350)

        self.username1 = Label(self.frame3,text="Usuario", font=("helvetica",20, "bold"),bg="white", fg="gray").place(x=50,y=40)
        self.usernameentry = Entry(self.frame3,font=("arial",15),bg="white",fg="gray")
        self.usernameentry.place(x=50, y=80, width=300)

        self.password1 = Label(self.frame3,text="Contraseña", font=("helvetica",20,"bold"),bg="white", fg="gray").place(x=50,y=120)
        self.passwordentry = Entry(self.frame3,bg="white",fg="gray",show="*")
        self.passwordentry.place(x=50, y=160, width=300)

        self.loginbutton = Button(self.frame3,text="Iniciar sesión",command=self.funcionlogin,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="green",fg="white").place(x=50,y=200,width=300)
        self.Invitado = Button(self.frame3,text="Ver Inventario como invitado",font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="green",fg="white",command=self.inventario_inv).place(x=50,y=250,width=300)

    def IniSesi(self):
        self.window=tk.Toplevel()
        self.window.title("LABIN")
        self.window.geometry("800x500")
        self.window.config(bg = "white")

        self.frame1 = Frame(self.window, bg='#F67000')
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= "LAB ", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=95,y=200
        )
        label2 = Label(self.frame1, text= "IN", font=("times new roman", 40, "bold"), bg="yellow", fg="RoyalBlue1").place(x=120,y=270)

        self.frame2 = Frame(self.window, bg = "#5F88AB")
        self.frame2.place(x=300,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=50,y=100,width=400,height=350)

        self.username1 = Label(self.frame3,text="Usuario", font=("helvetica",20, "bold"),bg="white", fg="gray").place(x=50,y=40)
        self.usernameentry = Entry(self.frame3,font=("arial",15),bg="white",fg="gray")
        self.usernameentry.place(x=50, y=80, width=300)

        self.password1 = Label(self.frame3,text="Contraseña", font=("helvetica",20,"bold"),bg="white", fg="gray").place(x=50,y=120)
        self.passwordentry = Entry(self.frame3,bg="white",fg="gray",show="*")
        self.passwordentry.place(x=50, y=160, width=300)

        self.loginbutton = Button(self.frame3,text="Iniciar sesión",command=self.funcionlogin,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="green",fg="white").place(x=50,y=200,width=300)
        self.Invitado = Button(self.frame3,text="Ver Inventario como invitado",font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="green",fg="white",command=self.inventario_inv).place(x=50,y=250,width=300)


    def funcionlogin(self):
        if self.usernameentry.get()=="" or self.passwordentry.get()=="":
            messagebox.showerror("Error","Debes llenar todos los campos",parent=self.window)
        else:
            try:
                self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="Semeolvido1*", database="Lab_Inventario")
                cur = self.conexion.cursor()
                cur.execute("select * from registro_Autorizados where usuario=%s and password=%s",(self.usernameentry.get(),self.passwordentry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Usuario y contraseña son inválidos",parent=self.window)
                else:
                    messagebox.showinfo("Succes","Bienvenido a LABIN",parent=self.window)
                    self.borrarlogin()
                    self.conexion.close()
                    obj.inventario_admin()                    
                    
            except Exception as e:
                messagebox.showerror("Error",f"Error {str(e)}",parent=self.window)

    def borrarlogin(self):
        self.usernameentry.delete(0,END)
        self.passwordentry.delete(0,END)
    
    #FUNCIONES PARA EQUIPOS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Guardar(self): 
        if self.id ==-1:       
            self.comp.inserta_equipos(self.serialeq.get(),self.nombreeq.get(),self.marcaeq.get(),self.caraceq.get(),self.obseq.get(),self.canteq.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.comp.modifica_equipos(self.id,self.serialeq.get(),self.nombreeq.get(),self.marcaeq.get(),self.caraceq.get(),self.obseq.get(),self.canteq.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiatabla()
        self.insertardatos() 
        self.limpiartexto() 

    def Buscarserial(self):
        cod_serial = self.serialeq.get()
        cod_serial = str("'" + cod_serial + "'")
        cod_serial = self.comp.Retornarserialeq(cod_serial)
        self.grid.delete(*self.grid.get_children())
        i = -1
        for dato in cod_serial:
            i= i+1                       
            self.grid.insert('',i, text = cod_serial[i][0:1], values=cod_serial[i][1:7])

    def Buscarnombre(self):
        cod_nombre = self.nombreeq.get()
        cod_nombre = str("'" + cod_nombre + "'")
        cod_nombre = self.comp.Retornarnombreeq(cod_nombre)
        self.grid.delete(*self.grid.get_children())
        i = -1
        for dato in cod_nombre:
            i= i+1                       
            self.grid.insert('',i, text = cod_nombre[i][0:1], values=cod_nombre[i][1:7])
            
    def Buscarmarca(self):
        cod_marca = self.marcaeq.get()
        cod_marca = str("'" + cod_marca + "'")
        cod_marca = self.comp.Retornarmarcaeq(cod_marca)
        self.grid.delete(*self.grid.get_children())
        i = -1
        for dato in cod_marca:
            i= i+1                       
            self.grid.insert('',i, text = cod_marca[i][0:1], values=cod_marca[i][1:7])

    
    def limpiartexto(self):
        self.serialeq.delete(0,END)
        self.nombreeq.delete(0,END)
        self.marcaeq.delete(0,END)
        self.caraceq.delete(0,END)
        self.obseq.delete(0,END)
        self.canteq.delete(0,END)


    def limpiatabla(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def insertardatos(self):
        datos = self.comp.consulta_equipos()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] ) 

    def mostrar_datos(self):
        self.grid.delete(*self.grid.get_children())
        registro = self.comp.consulta_equipos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.grid.insert('',i, text = registro[i][0:1], values=registro[i][1:7])

    def Nuevo(self):         
        self.limpiartexto()        
        self.serialeq.focus()

    def Modificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave                         
            valores = self.grid.item(selected,'values')
            self.limpiartexto()            
            self.serialeq.insert(0,valores[0])
            self.nombreeq.insert(0,valores[1])
            self.marcaeq.insert(0,valores[2])
            self.caraceq.insert(0,valores[3])   
            self.obseq.insert(0,valores[4]) 
            self.canteq.insert(0,valores[5]) 
            self.serialeq.focus()
                                        
    def Eliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            seguro = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if seguro == messagebox.YES:
                n = self.comp.elimina_equipos(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiatabla()
                    self.insertardatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def Cancelar(self):
        seguro = messagebox.askquestion("Cancelar", "Esta seguro de cancelar")
        if seguro == messagebox.YES:
            self.limpiartexto() 


    #FUNCIONES PARA REACTIVOS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Guardarreac(self): 
        if self.id ==-1:       
            self.comp.inserta_reactivos(self.codigoreac.get(),self.nombrereac.get(),self.ubireac.get(),self.pelireac.get(),self.pesoreac.get(),self.u_medida.get(),self.numcas.get(),self.cantreac.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.comp.modifica_reactivos(self.id,self.codigoreac.get(),self.nombrereac.get(),self.ubireac.get(),self.pelireac.get(),self.pesoreac.get(),self.u_medida.get(),self.numcas.get(),self.cantreac.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiatablareac()
        self.insertardatosreac() 
        self.limpiartextoreac() 

    def Buscarcodreac(self):
        cod_reac = self.codigoreac.get()
        cod_reac = str("'" + cod_reac + "'")
        cod_reac = self.comp.Retornarcodreac(cod_reac)
        self.grid1.delete(*self.grid1.get_children())
        i = -1
        for dato in cod_reac:
            i= i+1                       
            self.grid1.insert('',i, text = cod_reac[i][0:1], values=cod_reac[i][1:9])

    def Buscarnombrereac(self):
        reac_nombre = self.nombrereac.get()
        reac_nombre = str("'" + reac_nombre + "'")
        reac_nombre = self.comp.Retornarnombrereac(reac_nombre)
        self.grid1.delete(*self.grid1.get_children())
        i = -1
        for dato in reac_nombre:
            i= i+1                       
            self.grid1.insert('',i, text = reac_nombre[i][0:1], values=reac_nombre[i][1:9])
            
    def Buscarubireac(self):
        ubi_reac = self.ubireac.get()
        ubi_reac = str("'" + ubi_reac + "'")
        ubi_reac = self.comp.Retornarubireac(ubi_reac)
        self.grid1.delete(*self.grid1.get_children())
        i = -1
        for dato in ubi_reac:
            i= i+1                       
            self.grid1.insert('',i, text = ubi_reac[i][0:1], values=ubi_reac[i][1:9])

    
    def limpiartextoreac(self):
        self.codigoreac.delete(0,END)
        self.nombrereac.delete(0,END)
        self.ubireac.delete(0,END)
        self.pelireac.delete(0,END)
        self.pesoreac.delete(0,END)
        self.u_medida.delete(0,END)
        self.numcas.delete(0,END)
        self.cantreac.delete(0,END)


    def limpiatablareac(self):
        for item in self.grid1.get_children():
            self.grid1.delete(item)
                
    def insertardatosreac(self):
        datos = self.comp.consulta_reactivos()        
        for row in datos:            
            self.grid1.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],row[7],row[8],))
        
        if len(self.grid1.get_children()) > 0:
            self.grid1.selection_set( self.grid1.get_children()[0] ) 

    def mostrar_datosreac(self):
        self.grid1.delete(*self.grid1.get_children())
        registro = self.comp.consulta_reactivos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.grid1.insert('',i, text = registro[i][0:1], values=registro[i][1:9])

    def Nuevoreac(self):         
        self.limpiartextoreac()        
        self.codigoreac.focus()

    def Modificarreac(self):        
        selected = self.grid1.focus()                               
        clave = self.grid1.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave                         
            valores = self.grid1.item(selected,'values')
            self.limpiartextoreac()            
            self.codigoreac.insert(0,valores[0])
            self.nombrereac.insert(0,valores[1])
            self.ubireac.insert(0,valores[2])
            self.pelireac.insert(0,valores[3])   
            self.pesoreac.insert(0,valores[4]) 
            self.u_medida.insert(0,valores[5]) 
            self.numcas.insert(0,valores[6]) 
            self.cantreac.insert(0,valores[7]) 
            self.codigoreac.focus()
                                        
    def Eliminarreac(self):
        selected = self.grid1.focus()                               
        clave = self.grid1.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid1.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            seguro = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if seguro == messagebox.YES:
                n = self.comp.elimina_reactivos(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiatablareac()
                    self.insertardatosreac()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def Cancelarreac(self):
        seguro = messagebox.askquestion("Cancelar", "Esta seguro de cancelar")
        if seguro == messagebox.YES:
            self.limpiartextoreac() 


    #FUNCIONES PARA MATERIALES -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Guardarmat(self): 
        if self.id ==-1:       
            self.comp.inserta_materiales(self.codigomat.get(),self.nombremat.get(),self.ubimat.get(),self.material.get(),self.obsmat.get(),self.cantmat.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.comp.modifica_materiales(self.id,self.codigomat.get(),self.nombremat.get(),self.ubimat.get(),self.material.get(),self.obsmat.get(),self.cantmat.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiatablamat()
        self.insertardatosmat() 
        self.limpiartextomat() 

    def Buscarcodmat(self):
        cod_mat = self.codigomat.get()
        cod_mat = str("'" + cod_mat + "'")
        cod_mat = self.comp.Retornarcodmat(cod_mat)
        self.grid2.delete(*self.grid2.get_children())
        i = -1
        for dato in cod_mat:
            i= i+1                       
            self.grid2.insert('',i, text = cod_mat[i][0:1], values=cod_mat[i][1:9])

    def Buscarnombremat(self):
        mat_nombre = self.nombremat.get()
        mat_nombre = str("'" + mat_nombre + "'")
        mat_nombre = self.comp.Retornarnombremat(mat_nombre)
        self.grid2.delete(*self.grid2.get_children())
        i = -1
        for dato in mat_nombre:
            i= i+1                       
            self.grid2.insert('',i, text = mat_nombre[i][0:1], values=mat_nombre[i][1:9])
            
    def Buscarubimat(self):
        ubi_mat = self.ubimat.get()
        ubi_mat = str("'" + ubi_mat + "'")
        ubi_mat = self.comp.Retornarubimat(ubi_mat)
        self.grid2.delete(*self.grid2.get_children())
        i = -1
        for dato in ubi_mat:
            i= i+1                       
            self.grid2.insert('',i, text = ubi_mat[i][0:1], values=ubi_mat[i][1:9])

    
    def limpiartextomat(self):
        self.codigomat.delete(0,END)
        self.nombremat.delete(0,END)
        self.ubimat.delete(0,END)
        self.material.delete(0,END)
        self.obsmat.delete(0,END)
        self.cantmat.delete(0,END)


    def limpiatablamat(self):
        for item in self.grid2.get_children():
            self.grid2.delete(item)
                
    def insertardatosmat(self):
        datos = self.comp.consulta_materiales()        
        for row in datos:            
            self.grid2.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5],row[6],))
        
        if len(self.grid2.get_children()) > 0:
            self.grid2.selection_set( self.grid2.get_children()[0] ) 

    def mostrar_datosmat(self):
        self.grid2.delete(*self.grid2.get_children())
        registro = self.comp.consulta_materiales()
        i = -1
        for dato in registro:
            i= i+1                       
            self.grid2.insert('',i, text = registro[i][0:1], values=registro[i][1:9])

    def Nuevomat(self):         
        self.limpiartextomat()        
        self.codigomat.focus()

    def Modificarmat(self):        
        selected = self.grid2.focus()                               
        clave = self.grid2.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave                         
            valores = self.grid2.item(selected,'values')
            self.limpiartextomat()            
            self.codigomat.insert(0,valores[0])
            self.nombremat.insert(0,valores[1])
            self.ubimat.insert(0,valores[2])
            self.material.insert(0,valores[3])   
            self.obsmat.insert(0,valores[4]) 
            self.cantmat.insert(0,valores[5]) 
            self.codigomat.focus()
                                        
    def Eliminarmat(self):
        selected = self.grid2.focus()                               
        clave = self.grid2.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid2.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            seguro = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if seguro == messagebox.YES:
                n = self.comp.elimina_materiales(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiatablamat()
                    self.insertardatosmat()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def Cancelarmat(self):
        seguro = messagebox.askquestion("Cancelar", "Esta seguro de cancelar")
        if seguro == messagebox.YES:
            self.limpiartextoreac() 
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Aqui va la configuracion del menu
    def inventario_admin(self):
        self.window.withdraw()
        self.inventarioadmin=tk.Toplevel()
        self.inventarioadmin.geometry('1350x700')
        self.inventarioadmin.config(bd=20,bg='DarkCyan')
        self.inventarioadmin.title("Lab IN")
        self.menu = True
        self.color = True
        self.frame_inicio = Frame(self.inventarioadmin, bg='black', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
        self.frame_menu = Frame(self.inventarioadmin, bg='black', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        self.frame_top = Frame(self.inventarioadmin, bg='black', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        self.frame_principal = Frame(self.inventarioadmin, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.inventarioadmin.columnconfigure(1, weight=1)
        self.inventarioadmin.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.widgets()

    def inventario_inv(self):
        self.window.withdraw()
        self.inventarioinv=tk.Toplevel()
        self.inventarioinv.geometry('1350x700')
        self.inventarioinv.config(bd=20,bg='OrangeRed')
        self.inventarioinv.title("Lab IN")
        self.menu = True
        self.color = True
        self.frame_inicio = Frame(self.inventarioinv, bg='black', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
        self.frame_menu = Frame(self.inventarioinv, bg='black', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        self.frame_top = Frame(self.inventarioinv, bg='black', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        self.frame_principal = Frame(self.inventarioinv, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.inventarioinv.columnconfigure(1, weight=1)
        self.inventarioinv.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.widgetsinv()
    
    def buscar_admin(self):
        self.inventarioadmin.withdraw()
        self.inventarioadminB=tk.Toplevel()
        self.inventarioadminB.geometry('1350x700')
        self.inventarioadminB.config(bd=20,bg='OrangeRed')
        self.inventarioadminB.title("Lab IN")
        self.menu = True
        self.color = True
        self.frame_inicio = Frame(self.inventarioadminB, bg='black', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
        self.frame_menu = Frame(self.inventarioadminB, bg='black', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        self.frame_top = Frame(self.inventarioadminB, bg='black', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        self.frame_principal = Frame(self.inventarioadminB, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.inventarioadminB.columnconfigure(1, weight=1)
        self.inventarioadminB.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.widgetsBuscadmin()

    def Lab_Inicio(self):
        self.pestanas.select([self.frame_uno])

    def Lab_equipos(self):
        self.pestanas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.columnconfigure(1, weight=1)
        self.frame_dos.rowconfigure(2, weight=1)
       

    def Lab_reactivos(self):
        self.pestanas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.columnconfigure(1, weight=1)

    def Lab_materiales(self):
        self.pestanas.select([self.frame_cuatro])
        self.frame_cuatro.columnconfigure(0, weight=1)
        self.frame_cuatro.columnconfigure(1, weight=1)

    def pantalla_ajustes(self):
        self.pestanas.select([self.frame_cinco])
        
    def menu_lateral(self):
        if self.menu is True:
            for i in range(50,170,10):
                self.frame_menu.config(width= i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.boton_close.grid_forget()
                if clik_inicio is None:
                    self.boton_inicio.grid(column=0, row=0, padx =10, pady=10)
                    self.boton_inicio.grid_propagate(0)
                    self.boton_inicio.config(width=i)
                    self.Lab_Inicio()
                    self.menu = False
        else:
            for i in range(170,50,-10):
                self.frame_menu.config(width=  i)
                self.frame_inicio.config(width= i)
                self.frame_menu.update()
                clik_inicio = self.boton_inicio.grid_forget()
                if clik_inicio is   None:
                    self.frame_menu.grid_propagate(0)
                    self.boton_close.grid(column=0, row=0, padx =10, pady=10)
                    self.boton_close.grid_propagate(0)
                    self.boton_close.config(width=i)
                    self.Lab_Inicio()
            self.menu = True

    def Volver(self):
        self.inventarioadminB.withdraw()
        self.inventario_admin()
    def Volverinv(self):
        self.inventarioinv.withdraw()
        self.IniSesi()
  
            
    def widgets(self):
        self.imagen_inicio = PhotoImage(file ='imagesproy\inicio.png')
        self.imagen_menu = PhotoImage(file ='imagesproy\menu.png')
        self.imagen_equipos = PhotoImage(file ='imagesproy\equipos.png')
        self.imagen_sustancias = PhotoImage(file ='imagesproy\sustancias.png')
        self.imagen_materiales = PhotoImage(file ='imagesproy\materiales.png')
        self.imagen_buscar=PhotoImage(file='imagesproy\\buscar.png')
        self.imagen_autor = PhotoImage(file ='imagesproy\\autor.png')
        self.logo = PhotoImage(file ='imagesproy\labimg.png')
        self.thanks=PhotoImage(file='imagesproy\\thanks.png')
        self.boton_inicio= Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
        self.boton_inicio.grid(column=0, row=0, padx=12, pady=10)
        self.boton_close = Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black',bd=0, command = self.menu_lateral)
        self.boton_close.grid(column=0, row=0, padx=5, pady=10)	
        
        Button(self.frame_menu, image= self.imagen_equipos, bg='black', activebackground='black', bd=0, command = self.Lab_equipos).grid(column=0, row=1, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_sustancias, bg='black',activebackground='black', bd=0, command =self.Lab_reactivos ).grid(column=0, row=2, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_materiales, bg= 'black',activebackground='black', bd=0, command = self.Lab_materiales).grid(column=0, row=3, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_buscar, bg= 'black',activebackground='black', bd=0, command = self.buscar_admin).grid(column=0, row=4, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_autor, bg= 'black',activebackground='black', bd=0, command = self.pantalla_ajustes).grid(column=0, row=5, pady=20,padx=10)
        Label(self.frame_menu, text= 'Equipos', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text= 'Reactivos', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text= ' Materiales', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text= 'Buscar', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)
        Label(self.frame_menu, text= 'Autor', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)
        
        
        est_pestanas = ttk.Style()
        est_pestanas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
        est_pestanas.theme_use('default')
        est_pestanas.configure("TNotebook", background='black', borderwidth=0)
        est_pestanas.configure("TNotebook.Tab", background="black", borderwidth=0)
        est_pestanas.map("TNotebook", background=[("selected", 'black')])
        est_pestanas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);
        
        self.pestanas = ttk.Notebook(self.frame_principal , style= 'TNotebook') 
        self.pestanas.grid(column=0,row=0, sticky='nsew')
        self.frame_uno = Frame(self.pestanas, bg='CadetBlue')
        self.frame_dos = Frame(self.pestanas, bg='CadetBlue')
        self.frame_tres = Frame(self.pestanas, bg='CadetBlue')
        self.frame_cuatro = Frame(self.pestanas, bg='CadetBlue')
        self.frame_cinco = Frame(self.pestanas, bg='white')
        self.frame_seis = Frame(self.pestanas, bg='CadetBlue')
        self.pestanas.add(self.frame_uno)
        self.pestanas.add(self.frame_dos)
        self.pestanas.add(self.frame_tres)
        self.pestanas.add(self.frame_cuatro)
        self.pestanas.add(self.frame_cinco)
        self.pestanas.add(self.frame_seis)
        self.id=-1
        self.titulo = Label(self.frame_top,text= 'INVENTARIO DE LABORATORIO', bg='black', fg= 'CadetBlue', font= ('Imprint MT Shadow', 15, 'bold'))
        self.titulo.pack(expand=1)
        Label(self.frame_uno, text= 'LAB IN',bg='CadetBlue', fg= 'white', font= ('Brush Script MT', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno ,image= self.logo, bg='CadetBlue').pack(expand=1)

        #EQUIPOS-------------------------------------------------------------------------------------------


        Label(self.frame_dos, text= 'EQUIPOS', bd=20, bg='CadetBlue', fg= 'White', font= ('Comic Sans MS', 20, 'bold')).place(x=150,y=20,width=150, height=80)
        
        
        acciones=LabelFrame(self.frame_dos, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones.place(x=400,y=20,width=550, height=80)

        self.btnNuevo=Button(acciones,text="Insertar",command=self.Nuevo, bg="#F09909", fg="white")
        self.btnNuevo.place(x=30,y=10,width=80, height=30 ) 
        self.btnNuevo=Button(acciones,text="Modificar",command=self.Modificar,bg="#F09909", fg="white")
        self.btnNuevo.place(x=150,y=10,width=80, height=30 ) 
        self.btnNuevo=Button(acciones,text="Eliminar",command=self.Eliminar, bg="#F09909", fg="white")
        self.btnNuevo.place(x=270,y=10,width=80, height=30 ) 
        self.btnmostar=Button(acciones,text="Mostrar Tabla",command=self.mostrar_datos, bg="#F09909", fg="white")
        self.btnmostar.place(x=380,y=10,width=100, height=30 ) 
       
        datosinv=LabelFrame(self.frame_dos, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv.place(x=40,y=115,width=1200, height=200)

        label1=Label(datosinv, text="Serial del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label1.place(x=10,y=20,width=200, height=30)
        self.serialeq=Entry(datosinv)
        self.serialeq.place(x=250,y=20,width=150,height=30)
        
        label2=Label(datosinv, text="Nombre del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label2.place(x=10,y=70,width=200, height=30)
        self.nombreeq=Entry(datosinv)
        self.nombreeq.place(x=250,y=70, width=150,height=30 )

        
        label3=Label(datosinv, text="Marca del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label3.place(x=10,y=120,width=200, height=30)
        self.marcaeq=Entry(datosinv)
        self.marcaeq.place(x=250,y=120, width=150,height=30)

        
        label4=Label(datosinv, text="Características", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label4.place(x=450,y=20,width=200, height=30)
        
        self.caraceq=Entry(datosinv)
        self.caraceq.place(x=690,y=20, width=150,height=30)
        
        label5=Label(datosinv, text="Observaciones", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label5.place(x=450,y=70,width=200, height=30)
        self.obseq=Entry(datosinv)
        self.obseq.place(x=690,y=70, width=150,height=30)

        label6=Label(datosinv, text="Cantidad", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label6.place(x=450,y=120,width=200, height=30)
        self.canteq=Entry(datosinv)
        self.canteq.place(x=690,y=120, width=150,height=30)
        
        self.boton1=Button(datosinv, text="Guardar",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Guardar)
        self.boton1.place(x=930,y=40, width=150,height=30)
        self.boton2=Button(datosinv, text="Cancelar",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Cancelar)
        self.boton2.place(x=930,y=110,width=150, height=30)
        
        
        showdb = Frame(self.frame_dos, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb.place(x=40, y=325, width=1200, height=300)
        Label(showdb, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid = ttk.Treeview(showdb,columns=("col1","col2","col3","col4","col5","col6"))        
        self.grid.column("#0",width=70)
        self.grid.column("col1",width=100, anchor=CENTER)
        self.grid.column("col2",width=100, anchor=CENTER)
        self.grid.column("col3",width=100, anchor=CENTER)
        self.grid.column("col4",width=200, anchor=CENTER)  
        self.grid.column("col5",width=200, anchor=CENTER)       
        self.grid.column("col6",width=70, anchor=CENTER)         
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Serial de equipo", anchor=CENTER)
        self.grid.heading("col2", text="Nombre Equipo", anchor=CENTER)
        self.grid.heading("col3", text="Marca del equipo", anchor=CENTER)
        self.grid.heading("col4", text="Características", anchor=CENTER)      
        self.grid.heading("col5", text="Observaciones", anchor=CENTER)       
        self.grid.heading("col6", text="Cantidad", anchor=CENTER)                          
        self.grid.pack(side=TOP,fill = Y)        
        scroll = Scrollbar(showdb, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=scroll.set)
        scroll.config(command=self.grid.yview)
        self.grid['selectmode']='browse'

        #REACTIVOS------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Label(self.frame_tres, text= 'REACTIVOS', bd=20, bg='CadetBlue', fg= 'White', font= ('Comic Sans MS', 20, 'bold')).place(x=100,y=20,width=200, height=80)
        
        
        acciones2=LabelFrame(self.frame_tres, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones2.place(x=400,y=20,width=550, height=80)

        self.btnNuevo2=Button(acciones2,text="Insertar",command=self.Nuevoreac, bg="#F09909", fg="white")
        self.btnNuevo2.place(x=30,y=10,width=80, height=30 ) 
        self.btnNuevo2=Button(acciones2,text="Modificar",command=self.Modificarreac,bg="#F09909", fg="white")
        self.btnNuevo2.place(x=150,y=10,width=80, height=30 ) 
        self.btnNuevo2=Button(acciones2,text="Eliminar",command=self.Eliminarreac, bg="#F09909", fg="white")
        self.btnNuevo2.place(x=270,y=10,width=80, height=30 ) 
        self.btnmostar2=Button(acciones2,text="Mostrar Tabla",command=self.mostrar_datosreac, bg="#F09909", fg="white")
        self.btnmostar2.place(x=380,y=10,width=100, height=30 ) 
       
        datosinv2=LabelFrame(self.frame_tres, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv2.place(x=40,y=115,width=1200, height=250)

        label7=Label(datosinv2, text="Codigo Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label7.place(x=10,y=20,width=200, height=30)
        self.codigoreac=Entry(datosinv2)
        self.codigoreac.place(x=250,y=20,width=150,height=30)
        
        label8=Label(datosinv2, text="Nombre del Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label8.place(x=10,y=70,width=200, height=30)
        self.nombrereac=Entry(datosinv2)
        self.nombrereac.place(x=250,y=70, width=150,height=30 )

        
        label9=Label(datosinv2, text="Ubicación Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label9.place(x=10,y=120,width=200, height=30)
        self.ubireac=Entry(datosinv2)
        self.ubireac.place(x=250,y=120, width=150,height=30)

        
        label10=Label(datosinv2, text="Peligrosidad", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label10.place(x=10,y=170,width=200, height=30)
        self.pelireac=Entry(datosinv2)
        self.pelireac.place(x=250,y=170, width=150,height=30)
        
        label11=Label(datosinv2, text="Peso Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label11.place(x=450,y=20,width=200, height=30)
        self.pesoreac=Entry(datosinv2)
        self.pesoreac.place(x=690,y=20, width=150,height=30)

        label12=Label(datosinv2, text="Unidad medida", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label12.place(x=450,y=70,width=200, height=30)
        self.u_medida=Entry(datosinv2)
        self.u_medida.place(x=690,y=70, width=150,height=30)

        label13=Label(datosinv2, text="Número CAS", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label13.place(x=450,y=120,width=200, height=30)
        self.numcas=Entry(datosinv2)
        self.numcas.place(x=690,y=120, width=150,height=30)

        label14=Label(datosinv2, text="Cantidad", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label14.place(x=450,y=170,width=200, height=30)
        self.cantreac=Entry(datosinv2)
        self.cantreac.place(x=690,y=170, width=150,height=30)
        
        self.boton3=Button(datosinv2, text="Guardar",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Guardarreac)
        self.boton3.place(x=930,y=40, width=150,height=30)
        self.boton4=Button(datosinv2, text="Cancelar",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Cancelarreac)
        self.boton4.place(x=930,y=110,width=150, height=30)
        
        
        showdb2 = Frame(self.frame_tres, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb2.place(x=40, y=350, width=1200, height=300)
        Label(showdb2, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid1 = ttk.Treeview(showdb2,columns=("col1","col2","col3","col4","col5","col6","col7","col8"))        
        self.grid1.column("#0",width=50)
        self.grid1.column("col1",width=100, anchor=CENTER)
        self.grid1.column("col2",width=200, anchor=CENTER)
        self.grid1.column("col3",width=100, anchor=CENTER)
        self.grid1.column("col4",width=100, anchor=CENTER)  
        self.grid1.column("col5",width=150, anchor=CENTER) 
        self.grid1.column("col6",width=100, anchor=CENTER) 
        self.grid1.column("col7",width=100, anchor=CENTER)       
        self.grid1.column("col8",width=70, anchor=CENTER)         
        self.grid1.heading("#0", text="Id", anchor=CENTER)
        self.grid1.heading("col1", text="Codigo Reactivo", anchor=CENTER)
        self.grid1.heading("col2", text="Nombre Reactivo", anchor=CENTER)
        self.grid1.heading("col3", text="Ubicación", anchor=CENTER)
        self.grid1.heading("col4", text="Peligrosidad", anchor=CENTER) 
        self.grid1.heading("col5", text="Peso Reactivo", anchor=CENTER) 
        self.grid1.heading("col6", text="Unidad de Medida", anchor=CENTER) 
        self.grid1.heading("col7", text="Número CAS", anchor=CENTER)       
        self.grid1.heading("col8", text="Cantidad", anchor=CENTER)                          
        self.grid1.pack(side=TOP,fill = Y)        
        scroll2 = Scrollbar(showdb2, orient=VERTICAL)
        scroll2.pack(side=RIGHT, fill = Y)
        self.grid1.config(yscrollcommand=scroll2.set)
        scroll2.config(command=self.grid1.yview)
        self.grid1['selectmode']='browse'


        #METERIALES------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Label(self.frame_cuatro, text= 'MATERIALES', bd=20, bg='CadetBlue', fg= 'White', font= ('Comic Sans MS', 20, 'bold')).place(x=130,y=20,width=200, height=80)
        
        
        acciones3=LabelFrame(self.frame_cuatro, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones3.place(x=400,y=20,width=550, height=80)

        self.btnNuevo3=Button(acciones3,text="Insertar",command=self.Nuevomat, bg="#F09909", fg="white")
        self.btnNuevo3.place(x=30,y=10,width=80, height=30 ) 
        self.btnNuevo3=Button(acciones3,text="Modificar",command=self.Modificarmat,bg="#F09909", fg="white")
        self.btnNuevo3.place(x=150,y=10,width=80, height=30 ) 
        self.btnNuevo3=Button(acciones3,text="Eliminar",command=self.Eliminarmat, bg="#F09909", fg="white")
        self.btnNuevo3.place(x=270,y=10,width=80, height=30 ) 
        self.btnmostar3=Button(acciones3,text="Mostrar Tabla",command=self.mostrar_datosmat, bg="#F09909", fg="white")
        self.btnmostar3.place(x=380,y=10,width=100, height=30 ) 
       
        datosinv3=LabelFrame(self.frame_cuatro, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv3.place(x=40,y=115,width=1200, height=200)

        label15=Label(datosinv3, text="Código Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label15.place(x=10,y=20,width=200, height=30)
        self.codigomat=Entry(datosinv3)
        self.codigomat.place(x=250,y=20,width=150,height=30)
        
        label16=Label(datosinv3, text="Nombre del Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label16.place(x=10,y=70,width=200, height=30)
        self.nombremat=Entry(datosinv3)
        self.nombremat.place(x=250,y=70, width=150,height=30 )

        
        label17=Label(datosinv3, text="Ubicación Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label17.place(x=10,y=120,width=200, height=30)
        self.ubimat=Entry(datosinv3)
        self.ubimat.place(x=250,y=120, width=150,height=30)

        
        label18=Label(datosinv3, text="Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label18.place(x=450,y=20,width=200, height=30)
        self.material=Entry(datosinv3)
        self.material.place(x=690,y=20, width=150,height=30)
        
        label19=Label(datosinv3, text="Observaciones", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label19.place(x=450,y=70,width=200, height=30)
        self.obsmat=Entry(datosinv3)
        self.obsmat.place(x=690,y=70, width=150,height=30)

        label20=Label(datosinv3, text="Cantidad", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label20.place(x=450,y=120,width=200, height=30)
        self.cantmat=Entry(datosinv3)
        self.cantmat.place(x=690,y=120, width=150,height=30)
        
        self.boton5=Button(datosinv3, text="Guardar",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Guardarmat)
        self.boton5.place(x=930,y=40, width=150,height=30)
        self.boton6=Button(datosinv3, text="Cancelar",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Cancelar)
        self.boton6.place(x=930,y=110,width=150, height=30)
        
        
        showdb3 = Frame(self.frame_cuatro, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb3.place(x=40, y=325, width=1200, height=300)
        Label(showdb3, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid2 = ttk.Treeview(showdb3,columns=("col1","col2","col3","col4","col5","col6"))        
        self.grid2.column("#0",width=50)
        self.grid2.column("col1",width=100, anchor=CENTER)
        self.grid2.column("col2",width=150, anchor=CENTER)
        self.grid2.column("col3",width=120, anchor=CENTER)
        self.grid2.column("col4",width=100, anchor=CENTER)  
        self.grid2.column("col5",width=250, anchor=CENTER)       
        self.grid2.column("col6",width=70, anchor=CENTER)         
        self.grid2.heading("#0", text="Id", anchor=CENTER)
        self.grid2.heading("col1", text="Código Material", anchor=CENTER)
        self.grid2.heading("col2", text="Nombre Material", anchor=CENTER)
        self.grid2.heading("col3", text="Ubicación Material", anchor=CENTER)
        self.grid2.heading("col4", text="Material", anchor=CENTER)      
        self.grid2.heading("col5", text="Observaciones", anchor=CENTER)       
        self.grid2.heading("col6", text="Cantidad", anchor=CENTER)                          
        self.grid2.pack(side=TOP,fill = Y)        
        scroll3 = Scrollbar(showdb3, orient=VERTICAL)
        scroll3.pack(side=RIGHT, fill = Y)
        self.grid2.config(yscrollcommand=scroll3.set)
        scroll3.config(command=self.grid2.yview)
        self.grid2['selectmode']='browse'

        #PRESENTADO POR------------------------------------------------------------------------------------------

        self.autorproy = Label(self.frame_cinco, text = 'PROYECTO BASE DE DATOS',fg='CadetBlue', bg ='white', font=('Kaufmann BT',40,'bold'))
        self.autorproy.pack(expand=1)
        Label(self.frame_cinco ,image= self.thanks, bg='white').pack(expand=1)
        self.texto1 = Label(self.frame_cinco, text = 'Presentado Por: Gina Stephanie Gonzalez \n Python y MySQL',fg='CadetBlue', bg ='white', font=('Kaufmann BT',25))
        self.texto1.pack(expand=1)   

    def widgetsinv(self):
        self.imagen_inicio = PhotoImage(file ='imagesproy\inicio.png')
        self.imagen_menu = PhotoImage(file ='imagesproy\menu.png')
        self.imagen_buscar1 = PhotoImage(file ='imagesproy\\buscar1.png')
        self.imagen_buscar2 = PhotoImage(file ='imagesproy\\buscar2.png')
        self.imagen_buscar3 = PhotoImage(file ='imagesproy\\buscar3.png')
        self.imagen_autor = PhotoImage(file ='imagesproy\\autor.png')
        self.logo = PhotoImage(file ='imagesproy\labimg.png')
        self.thanks=PhotoImage(file='imagesproy\\thanks.png')
        self.boton_inicio= Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
        self.boton_inicio.grid(column=0, row=0, padx=12, pady=10)
        self.boton_close = Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black',bd=0, command = self.menu_lateral)
        self.boton_close.grid(column=0, row=0, padx=5, pady=10)	
        
        Button(self.frame_menu, image= self.imagen_buscar1, bg='black', activebackground='black', bd=0, command = self.Lab_equipos).grid(column=0, row=1, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_buscar2, bg='black', activebackground='black', bd=0, command = self.Lab_reactivos).grid(column=0, row=2, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_buscar3, bg='black', activebackground='black', bd=0, command = self.Lab_materiales).grid(column=0, row=3, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_autor, bg= 'black',activebackground='black', bd=0, command = self.pantalla_ajustes).grid(column=0, row=4, pady=20,padx=10)
        Label(self.frame_menu, text= 'Equipos', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text= 'Reactivos', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text= 'Materiales', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text= 'Autor', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)
        
        
        est_pestanas = ttk.Style()
        est_pestanas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
        est_pestanas.theme_use('default')
        est_pestanas.configure("TNotebook", background='black', borderwidth=0)
        est_pestanas.configure("TNotebook.Tab", background="black", borderwidth=0)
        est_pestanas.map("TNotebook", background=[("selected", 'black')])
        est_pestanas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);
        
        self.pestanas = ttk.Notebook(self.frame_principal , style= 'TNotebook') 
        self.pestanas.grid(column=0,row=0, sticky='nsew')
        self.frame_uno = Frame(self.pestanas, bg='Coral')
        self.frame_dos = Frame(self.pestanas, bg='Coral')
        self.frame_tres = Frame(self.pestanas, bg='Coral')
        self.frame_cuatro = Frame(self.pestanas, bg='Coral')
        self.frame_cinco = Frame(self.pestanas, bg='white')
        self.pestanas.add(self.frame_uno)
        self.pestanas.add(self.frame_dos)
        self.pestanas.add(self.frame_tres)
        self.pestanas.add(self.frame_cuatro)
        self.pestanas.add(self.frame_cinco)
        self.id=-1
        self.titulo = Label(self.frame_top,text= 'INVENTARIO DE LABORATORIO', bg='black', fg= 'Coral', font= ('Imprint MT Shadow', 15, 'bold'))
        self.titulo.pack(expand=1)
        Label(self.frame_uno, text= 'LAB IN',bg='Coral', fg= 'white', font= ('Brush Script MT', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno ,image= self.logo, bg='Coral').pack(expand=1)

        #BUSCAR EQUIPOS -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        Label(self.frame_dos, text= 'BUSCAR EQUIPOS', bd=20, bg='Coral', fg= 'White', font= ('Comic Sans MS', 15, 'bold')).place(x=150,y=20,width=200, height=80)
        
        
        acciones=LabelFrame(self.frame_dos, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones.place(x=400,y=20,width=400, height=80)

        self.btnmostar=Button(acciones,text="Mostrar Tabla",command=self.mostrar_datos, bg="#F09909", fg="white")
        self.btnmostar.place(x=80,y=10,width=100, height=30) 
        self.btnvolver=Button(acciones,text="Iniciar Sesión",command=self.Volverinv, bg="#F09909", fg="white")
        self.btnvolver.place(x=200,y=10,width=100, height=30)


        #datos equipos
       
        datosinv=LabelFrame(self.frame_dos, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv.place(x=40,y=115,width=1200, height=200)

        label1=Label(datosinv, text="Serial del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label1.place(x=240,y=20,width=200, height=30)
        self.serialeq=Entry(datosinv)
        self.serialeq.place(x=490,y=20,width=150,height=30)
        
        label2=Label(datosinv, text="Nombre del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label2.place(x=240,y=70,width=200, height=30)
        self.nombreeq=Entry(datosinv)
        self.nombreeq.place(x=490,y=70, width=150,height=30 )
        
        label3=Label(datosinv, text="Marca del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label3.place(x=240,y=120,width=200, height=30)
        self.marcaeq=Entry(datosinv)
        self.marcaeq.place(x=490,y=120, width=150,height=30)

        self.boton1=Button(datosinv, text="Buscar Serial",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarserial)
        self.boton1.place(x=690,y=20, width=200,height=30)
       
        self.boton2=Button(datosinv, text="Buscar Nombre",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarnombre)
        self.boton2.place(x=690,y=70, width=200,height=30)
        
        self.boton3=Button(datosinv, text="Buscar Marca",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarmarca)
        self.boton3.place(x=690,y=120, width=200,height=30)
        
        
        showdb = Frame(self.frame_dos, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb.place(x=40, y=325, width=1200, height=300)
        Label(showdb, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid = ttk.Treeview(showdb,columns=("col1","col2","col3","col4","col5","col6"))        
        self.grid.column("#0",width=70)
        self.grid.column("col1",width=100, anchor=CENTER)
        self.grid.column("col2",width=100, anchor=CENTER)
        self.grid.column("col3",width=100, anchor=CENTER)
        self.grid.column("col4",width=200, anchor=CENTER)  
        self.grid.column("col5",width=200, anchor=CENTER)       
        self.grid.column("col6",width=70, anchor=CENTER)         
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Serial de equipo", anchor=CENTER)
        self.grid.heading("col2", text="Nombre Equipo", anchor=CENTER)
        self.grid.heading("col3", text="Marca del equipo", anchor=CENTER)
        self.grid.heading("col4", text="Características", anchor=CENTER)      
        self.grid.heading("col5", text="Observaciones", anchor=CENTER)       
        self.grid.heading("col6", text="Cantidad", anchor=CENTER)                          
        self.grid.pack(side=TOP,fill = Y)        
        scroll = Scrollbar(showdb, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=scroll.set)
        scroll.config(command=self.grid.yview)
        self.grid['selectmode']='browse'

        #BUSCAR REACTIVOS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Label(self.frame_tres, text= 'BUSCAR REACTIVOS', bd=20, bg='Coral', fg= 'White', font= ('Comic Sans MS', 15, 'bold')).place(x=150,y=20,width=220, height=80)
        
        
        acciones2=LabelFrame(self.frame_tres, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones2.place(x=400,y=20,width=400, height=80)

        self.btnmostar2=Button(acciones2,text="Mostrar Tabla",command=self.mostrar_datosreac, bg="#F09909", fg="white")
        self.btnmostar2.place(x=80,y=10,width=100, height=30) 
        self.btnvolver2=Button(acciones2,text="Iniciar Sesión",command=self.Volverinv, bg="#F09909", fg="white")
        self.btnvolver2.place(x=200,y=10,width=100, height=30)


        #datos equipos
       
        datosinv2=LabelFrame(self.frame_tres, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv2.place(x=40,y=115,width=1200, height=200)

        label4=Label(datosinv2, text="Código del Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label4.place(x=240,y=20,width=200, height=30)
        self.codigoreac=Entry(datosinv2)
        self.codigoreac.place(x=490,y=20,width=150,height=30)
        
        label5=Label(datosinv2, text="Nombre del Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label5.place(x=240,y=70,width=200, height=30)
        self.nombrereac=Entry(datosinv2)
        self.nombrereac.place(x=490,y=70, width=150,height=30 )
        
        label6=Label(datosinv2, text="Ubicación del Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label6.place(x=240,y=120,width=200, height=30)
        self.ubireac=Entry(datosinv2)
        self.ubireac.place(x=490,y=120, width=150,height=30)

        self.boton4=Button(datosinv2, text="Buscar Código",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarcodreac)
        self.boton4.place(x=690,y=20, width=200,height=30)
       
        self.boton5=Button(datosinv2, text="Buscar Nombre",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarnombrereac)
        self.boton5.place(x=690,y=70, width=200,height=30)
        
        self.boton6=Button(datosinv2, text="Buscar Ubicación",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarubireac)
        self.boton6.place(x=690,y=120, width=200,height=30)
        
        
        showdb2 = Frame(self.frame_tres, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb2.place(x=40, y=325, width=1200, height=300)
        Label(showdb2, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid1 = ttk.Treeview(showdb2,columns=("col1","col2","col3","col4","col5","col6","col7","col8"))        
        self.grid1.column("#0",width=50)
        self.grid1.column("col1",width=100, anchor=CENTER)
        self.grid1.column("col2",width=200, anchor=CENTER)
        self.grid1.column("col3",width=100, anchor=CENTER)
        self.grid1.column("col4",width=100, anchor=CENTER)  
        self.grid1.column("col5",width=150, anchor=CENTER) 
        self.grid1.column("col6",width=100, anchor=CENTER) 
        self.grid1.column("col7",width=100, anchor=CENTER)       
        self.grid1.column("col8",width=70, anchor=CENTER)         
        self.grid1.heading("#0", text="Id", anchor=CENTER)
        self.grid1.heading("col1", text="Codigo Reactivo", anchor=CENTER)
        self.grid1.heading("col2", text="Nombre Reactivo", anchor=CENTER)
        self.grid1.heading("col3", text="Ubicación", anchor=CENTER)
        self.grid1.heading("col4", text="Peligrosidad", anchor=CENTER) 
        self.grid1.heading("col5", text="Peso Reactivo", anchor=CENTER) 
        self.grid1.heading("col6", text="Unidad de Medida", anchor=CENTER) 
        self.grid1.heading("col7", text="Número CAS", anchor=CENTER)       
        self.grid1.heading("col8", text="Cantidad", anchor=CENTER)                         
        self.grid1.pack(side=TOP,fill = Y)        
        scroll2 = Scrollbar(showdb2, orient=VERTICAL)
        scroll2.pack(side=RIGHT, fill = Y)
        self.grid1.config(yscrollcommand=scroll2.set)
        scroll2.config(command=self.grid1.yview)
        self.grid1['selectmode']='browse'


        #BUSCAR MATERIALES--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Label(self.frame_cuatro, text= 'BUSCAR MATERIALES', bd=20, bg='Coral', fg= 'White', font= ('Comic Sans MS', 15, 'bold')).place(x=150,y=20,width=220, height=80)
        
        
        acciones3=LabelFrame(self.frame_cuatro, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones3.place(x=400,y=20,width=400, height=80)

        self.btnmostar3=Button(acciones3,text="Mostrar Tabla",command=self.mostrar_datosmat, bg="#F09909", fg="white")
        self.btnmostar3.place(x=80,y=10,width=100, height=30) 
        self.btnvolver3=Button(acciones3,text="Iniciar Sesión",command=self.Volverinv, bg="#F09909", fg="white")
        self.btnvolver3.place(x=200,y=10,width=100, height=30)


        #datos equipos
       
        datosinv3=LabelFrame(self.frame_cuatro, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv3.place(x=40,y=115,width=1200, height=200)

        label7=Label(datosinv3, text="Código Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label7.place(x=240,y=20,width=200, height=30)
        self.codigomat=Entry(datosinv3)
        self.codigomat.place(x=490,y=20,width=150,height=30)
        
        label8=Label(datosinv3, text="Nombre del Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label8.place(x=240,y=70,width=200, height=30)
        self.nombremat=Entry(datosinv3)
        self.nombremat.place(x=490,y=70, width=150,height=30 )
        
        label9=Label(datosinv3, text="Ubicación del Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label9.place(x=240,y=120,width=200, height=30)
        self.ubimat=Entry(datosinv3)
        self.ubimat.place(x=490,y=120, width=150,height=30)

        self.boton7=Button(datosinv3, text="Buscar Código",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarcodmat)
        self.boton7.place(x=690,y=20, width=200,height=30)
       
        self.boton8=Button(datosinv3, text="Buscar Nombre",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarnombremat)
        self.boton8.place(x=690,y=70, width=200,height=30)
        
        self.boton9=Button(datosinv3, text="Buscar Ubicación",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarubimat)
        self.boton9.place(x=690,y=120, width=200,height=30)
        
        
        showdb3 = Frame(self.frame_cuatro, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb3.place(x=40, y=325, width=1200, height=300)
        Label(showdb3, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid2 = ttk.Treeview(showdb3,columns=("col1","col2","col3","col4","col5","col6"))        
        self.grid2.column("#0",width=50)
        self.grid2.column("col1",width=100, anchor=CENTER)
        self.grid2.column("col2",width=150, anchor=CENTER)
        self.grid2.column("col3",width=120, anchor=CENTER)
        self.grid2.column("col4",width=100, anchor=CENTER)  
        self.grid2.column("col5",width=250, anchor=CENTER)       
        self.grid2.column("col6",width=70, anchor=CENTER)         
        self.grid2.heading("#0", text="Id", anchor=CENTER)
        self.grid2.heading("col1", text="Código Material", anchor=CENTER)
        self.grid2.heading("col2", text="Nombre Material", anchor=CENTER)
        self.grid2.heading("col3", text="Ubicación Material", anchor=CENTER)
        self.grid2.heading("col4", text="Material", anchor=CENTER)      
        self.grid2.heading("col5", text="Observaciones", anchor=CENTER)       
        self.grid2.heading("col6", text="Cantidad", anchor=CENTER)                          
        self.grid2.pack(side=TOP,fill = Y)        
        scroll3 = Scrollbar(showdb3, orient=VERTICAL)
        scroll3.pack(side=RIGHT, fill = Y)
        self.grid2.config(yscrollcommand=scroll3.set)
        scroll3.config(command=self.grid2.yview)
        self.grid2['selectmode']='browse'


        #PRESENTADO POR----------------------------------------------------------------------------------
        self.autorproy = Label(self.frame_cinco, text = 'PROYECTO BASE DE DATOS',fg='CadetBlue', bg ='white', font=('Kaufmann BT',40,'bold'))
        self.autorproy.pack(expand=1)
        Label(self.frame_cinco ,image= self.thanks, bg='white').pack(expand=1)
        self.texto1 = Label(self.frame_cinco, text = 'Presentado Por: Gina Stephanie Gonzalez \n Python y MySQL',fg='CadetBlue', bg ='white', font=('Kaufmann BT',25))
        self.texto1.pack(expand=1)  

    def widgetsBuscadmin(self):
        self.imagen_inicio = PhotoImage(file ='imagesproy\inicio.png')
        self.imagen_menu = PhotoImage(file ='imagesproy\menu.png')
        self.imagen_buscar1 = PhotoImage(file ='imagesproy\\buscar1.png')
        self.imagen_buscar2 = PhotoImage(file ='imagesproy\\buscar2.png')
        self.imagen_buscar3 = PhotoImage(file ='imagesproy\\buscar3.png')
        self.imagen_autor = PhotoImage(file ='imagesproy\\autor.png')
        self.logo = PhotoImage(file ='imagesproy\labimg.png')
        self.thanks=PhotoImage(file='imagesproy\\thanks.png')
        self.boton_inicio= Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
        self.boton_inicio.grid(column=0, row=0, padx=12, pady=10)
        self.boton_close = Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black',bd=0, command = self.menu_lateral)
        self.boton_close.grid(column=0, row=0, padx=5, pady=10)	
        
        Button(self.frame_menu, image= self.imagen_buscar1, bg='black', activebackground='black', bd=0, command = self.Lab_equipos).grid(column=0, row=1, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_buscar2, bg='black', activebackground='black', bd=0, command = self.Lab_reactivos).grid(column=0, row=2, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_buscar3, bg='black', activebackground='black', bd=0, command = self.Lab_materiales).grid(column=0, row=3, pady=20,padx=10)
        Button(self.frame_menu, image= self.imagen_autor, bg= 'black',activebackground='black', bd=0, command = self.pantalla_ajustes).grid(column=0, row=4, pady=20,padx=10)
        Label(self.frame_menu, text= 'Equipos', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text= 'Reactivos', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text= 'Materiales', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text= 'Autor', bg= 'black', fg= 'DarkSeaGreen', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)
        
        
        est_pestanas = ttk.Style()
        est_pestanas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
        est_pestanas.theme_use('default')
        est_pestanas.configure("TNotebook", background='black', borderwidth=0)
        est_pestanas.configure("TNotebook.Tab", background="black", borderwidth=0)
        est_pestanas.map("TNotebook", background=[("selected", 'black')])
        est_pestanas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);
        

        self.pestanas = ttk.Notebook(self.frame_principal , style= 'TNotebook') 
        self.pestanas.grid(column=0,row=0, sticky='nsew')
        self.frame_uno = Frame(self.pestanas, bg='Coral')
        self.frame_dos = Frame(self.pestanas, bg='Coral')
        self.frame_tres = Frame(self.pestanas, bg='Coral')
        self.frame_cuatro = Frame(self.pestanas, bg='Coral')
        self.frame_cinco = Frame(self.pestanas, bg='white')
        self.pestanas.add(self.frame_uno)
        self.pestanas.add(self.frame_dos)
        self.pestanas.add(self.frame_tres)
        self.pestanas.add(self.frame_cuatro)
        self.pestanas.add(self.frame_cinco)
        self.id=-1
        self.titulo = Label(self.frame_top,text= 'INVENTARIO DE LABORATORIO', bg='black', fg= 'Coral', font= ('Imprint MT Shadow', 15, 'bold'))
        self.titulo.pack(expand=1)
        Label(self.frame_uno, text= 'LAB IN',bg='Coral', fg= 'white', font= ('Brush Script MT', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno ,image= self.logo, bg='Coral').pack(expand=1)
        #BUSCAR EQUIPOS --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      


        #datos equipos
       
        Label(self.frame_dos, text= 'BUSCAR EQUIPOS', bd=20, bg='Coral', fg= 'White', font= ('Comic Sans MS', 15, 'bold')).place(x=150,y=20,width=200, height=80)
        
        
        acciones=LabelFrame(self.frame_dos, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones.place(x=400,y=20,width=400, height=80)

        self.btnmostar=Button(acciones,text="Mostrar Tabla",command=self.mostrar_datos, bg="#F09909", fg="white")
        self.btnmostar.place(x=80,y=10,width=100, height=30) 
        self.btnvolver=Button(acciones,text="Volver",command=self.Volver, bg="#F09909", fg="white")
        self.btnvolver.place(x=200,y=10,width=100, height=30)


        #datos equipos
       
        datosinv=LabelFrame(self.frame_dos, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv.place(x=40,y=115,width=1200, height=200)

        label1=Label(datosinv, text="Serial del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label1.place(x=240,y=20,width=200, height=30)
        self.serialeq=Entry(datosinv)
        self.serialeq.place(x=490,y=20,width=150,height=30)
        
        label2=Label(datosinv, text="Nombre del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label2.place(x=240,y=70,width=200, height=30)
        self.nombreeq=Entry(datosinv)
        self.nombreeq.place(x=490,y=70, width=150,height=30 )
        
        label3=Label(datosinv, text="Marca del equipo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label3.place(x=240,y=120,width=200, height=30)
        self.marcaeq=Entry(datosinv)
        self.marcaeq.place(x=490,y=120, width=150,height=30)

        self.boton1=Button(datosinv, text="Buscar Serial",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarserial)
        self.boton1.place(x=690,y=20, width=200,height=30)
       
        self.boton2=Button(datosinv, text="Buscar Nombre",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarnombre)
        self.boton2.place(x=690,y=70, width=200,height=30)
        
        self.boton3=Button(datosinv, text="Buscar Marca",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarmarca)
        self.boton3.place(x=690,y=120, width=200,height=30)
        
        
        showdb = Frame(self.frame_dos, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb.place(x=40, y=325, width=1200, height=300)
        Label(showdb, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid = ttk.Treeview(showdb,columns=("col1","col2","col3","col4","col5","col6"))        
        self.grid.column("#0",width=70)
        self.grid.column("col1",width=100, anchor=CENTER)
        self.grid.column("col2",width=100, anchor=CENTER)
        self.grid.column("col3",width=100, anchor=CENTER)
        self.grid.column("col4",width=200, anchor=CENTER)  
        self.grid.column("col5",width=200, anchor=CENTER)       
        self.grid.column("col6",width=70, anchor=CENTER)         
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Serial de equipo", anchor=CENTER)
        self.grid.heading("col2", text="Nombre Equipo", anchor=CENTER)
        self.grid.heading("col3", text="Marca del equipo", anchor=CENTER)
        self.grid.heading("col4", text="Características", anchor=CENTER)      
        self.grid.heading("col5", text="Observaciones", anchor=CENTER)       
        self.grid.heading("col6", text="Cantidad", anchor=CENTER)                          
        self.grid.pack(side=TOP,fill = Y)        
        scroll = Scrollbar(showdb, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=scroll.set)
        scroll.config(command=self.grid.yview)
        self.grid['selectmode']='browse'

        #BUSCAR REACTIVOS
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Label(self.frame_tres, text= 'BUSCAR REACTIVOS', bd=20, bg='Coral', fg= 'White', font= ('Comic Sans MS', 15, 'bold')).place(x=150,y=20,width=220, height=80)
        
        
        acciones2=LabelFrame(self.frame_tres, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones2.place(x=400,y=20,width=400, height=80)

        self.btnmostar2=Button(acciones2,text="Mostrar Tabla",command=self.mostrar_datosreac, bg="#F09909", fg="white")
        self.btnmostar2.place(x=80,y=10,width=100, height=30) 
        self.btnvolver2=Button(acciones2,text="volver",command=self.Volver, bg="#F09909", fg="white")
        self.btnvolver2.place(x=200,y=10,width=100, height=30)


        #datos equipos
       
        datosinv2=LabelFrame(self.frame_tres, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv2.place(x=40,y=115,width=1200, height=200)

        label4=Label(datosinv2, text="Código del Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label4.place(x=240,y=20,width=200, height=30)
        self.codigoreac=Entry(datosinv2)
        self.codigoreac.place(x=490,y=20,width=150,height=30)
        
        label5=Label(datosinv2, text="Nombre del Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label5.place(x=240,y=70,width=200, height=30)
        self.nombrereac=Entry(datosinv2)
        self.nombrereac.place(x=490,y=70, width=150,height=30 )
        
        label6=Label(datosinv2, text="Ubicación del Reactivo", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label6.place(x=240,y=120,width=200, height=30)
        self.ubireac=Entry(datosinv2)
        self.ubireac.place(x=490,y=120, width=150,height=30)

        self.boton4=Button(datosinv2, text="Buscar Código",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarcodreac)
        self.boton4.place(x=690,y=20, width=200,height=30)
       
        self.boton5=Button(datosinv2, text="Buscar Nombre",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarnombrereac)
        self.boton5.place(x=690,y=70, width=200,height=30)
        
        self.boton6=Button(datosinv2, text="Buscar Ubicación",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarubireac)
        self.boton6.place(x=690,y=120, width=200,height=30)
        
        
        showdb2 = Frame(self.frame_tres, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb2.place(x=40, y=325, width=1200, height=300)
        Label(showdb2, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid1 = ttk.Treeview(showdb2,columns=("col1","col2","col3","col4","col5","col6","col7","col8"))        
        self.grid1.column("#0",width=50)
        self.grid1.column("col1",width=100, anchor=CENTER)
        self.grid1.column("col2",width=200, anchor=CENTER)
        self.grid1.column("col3",width=100, anchor=CENTER)
        self.grid1.column("col4",width=100, anchor=CENTER)  
        self.grid1.column("col5",width=150, anchor=CENTER) 
        self.grid1.column("col6",width=100, anchor=CENTER) 
        self.grid1.column("col7",width=100, anchor=CENTER)       
        self.grid1.column("col8",width=70, anchor=CENTER)         
        self.grid1.heading("#0", text="Id", anchor=CENTER)
        self.grid1.heading("col1", text="Codigo Reactivo", anchor=CENTER)
        self.grid1.heading("col2", text="Nombre Reactivo", anchor=CENTER)
        self.grid1.heading("col3", text="Ubicación", anchor=CENTER)
        self.grid1.heading("col4", text="Peligrosidad", anchor=CENTER) 
        self.grid1.heading("col5", text="Peso Reactivo", anchor=CENTER) 
        self.grid1.heading("col6", text="Unidad de Medida", anchor=CENTER) 
        self.grid1.heading("col7", text="Número CAS", anchor=CENTER)       
        self.grid1.heading("col8", text="Cantidad", anchor=CENTER)                         
        self.grid1.pack(side=TOP,fill = Y)        
        scroll2 = Scrollbar(showdb2, orient=VERTICAL)
        scroll2.pack(side=RIGHT, fill = Y)
        self.grid1.config(yscrollcommand=scroll2.set)
        scroll2.config(command=self.grid1.yview)
        self.grid1['selectmode']='browse'

        #BUSCAR MATERIALES ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Label(self.frame_cuatro, text= 'BUSCAR MATERIALES', bd=20, bg='Coral', fg= 'White', font= ('Comic Sans MS', 15, 'bold')).place(x=150,y=20,width=220, height=80)
        
        
        acciones3=LabelFrame(self.frame_cuatro, text="Acciones", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        acciones3.place(x=400,y=20,width=400, height=80)

        self.btnmostar3=Button(acciones3,text="Mostrar Tabla",command=self.mostrar_datosmat, bg="#F09909", fg="white")
        self.btnmostar3.place(x=80,y=10,width=100, height=30) 
        self.btnvolver3=Button(acciones3,text="Volver",command=self.Volver, bg="#F09909", fg="white")
        self.btnvolver3.place(x=200,y=10,width=100, height=30)


        #datos equipos
       
        datosinv3=LabelFrame(self.frame_cuatro, text="Datos Laboratorio", font=("Bodoni Bd BT", 12),bg="#62D5C3", fg="white", relief=RIDGE, bd=10)
        datosinv3.place(x=40,y=115,width=1200, height=200)

        label7=Label(datosinv3, text="Código Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label7.place(x=240,y=20,width=200, height=30)
        self.codigomat=Entry(datosinv3)
        self.codigomat.place(x=490,y=20,width=150,height=30)
        
        label8=Label(datosinv3, text="Nombre del Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label8.place(x=240,y=70,width=200, height=30)
        self.nombremat=Entry(datosinv3)
        self.nombremat.place(x=490,y=70, width=150,height=30 )
        
        label9=Label(datosinv3, text="Ubicación del Material", font=("Bodoni Bd BT", 14), bg="#3BAB9B", fg="white")
        label9.place(x=240,y=120,width=200, height=30)
        self.ubimat=Entry(datosinv3)
        self.ubimat.place(x=490,y=120, width=150,height=30)

        self.boton7=Button(datosinv3, text="Buscar Código",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarcodmat)
        self.boton7.place(x=690,y=20, width=200,height=30)
       
        self.boton8=Button(datosinv3, text="Buscar Nombre",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarnombremat)
        self.boton8.place(x=690,y=70, width=200,height=30)
        
        self.boton9=Button(datosinv3, text="Buscar Ubicación",font=("Bodoni Bd BT", 14), bg="#F09909", fg="white",command=self.Buscarubimat)
        self.boton9.place(x=690,y=120, width=200,height=30)
        
        
        showdb3 = Frame(self.frame_cuatro, bg='#9AB3C8',bd=5, relief=GROOVE)
        showdb3.place(x=40, y=325, width=1200, height=300)
        Label(showdb3, text="Lista Componentes", font=("Bodoni Bd BT", 12,'bold'), bd=4, relief=SUNKEN, bg="#3BAB9B", fg="white").pack()
        self.grid2 = ttk.Treeview(showdb3,columns=("col1","col2","col3","col4","col5","col6"))        
        self.grid2.column("#0",width=50)
        self.grid2.column("col1",width=100, anchor=CENTER)
        self.grid2.column("col2",width=150, anchor=CENTER)
        self.grid2.column("col3",width=120, anchor=CENTER)
        self.grid2.column("col4",width=100, anchor=CENTER)  
        self.grid2.column("col5",width=250, anchor=CENTER)       
        self.grid2.column("col6",width=70, anchor=CENTER)         
        self.grid2.heading("#0", text="Id", anchor=CENTER)
        self.grid2.heading("col1", text="Código Material", anchor=CENTER)
        self.grid2.heading("col2", text="Nombre Material", anchor=CENTER)
        self.grid2.heading("col3", text="Ubicación Material", anchor=CENTER)
        self.grid2.heading("col4", text="Material", anchor=CENTER)      
        self.grid2.heading("col5", text="Observaciones", anchor=CENTER)       
        self.grid2.heading("col6", text="Cantidad", anchor=CENTER)                          
        self.grid2.pack(side=TOP,fill = Y)        
        scroll3 = Scrollbar(showdb3, orient=VERTICAL)
        scroll3.pack(side=RIGHT, fill = Y)
        self.grid2.config(yscrollcommand=scroll3.set)
        scroll3.config(command=self.grid2.yview)
        self.grid2['selectmode']='browse'

        #PRESENTADO POR----------------------------------------------------------------------------------
        self.autorproy = Label(self.frame_cinco, text = 'PROYECTO BASE DE DATOS',fg='CadetBlue', bg ='white', font=('Kaufmann BT',40,'bold'))
        self.autorproy.pack(expand=1)
        Label(self.frame_cinco ,image= self.thanks, bg='white').pack(expand=1)
        self.texto1 = Label(self.frame_cinco, text = 'Presentado Por: Gina Stephanie Gonzalez \n Python y MySQL',fg='CadetBlue', bg ='white', font=('Kaufmann BT',25))
        self.texto1.pack(expand=1)

    
            

    








    
# The main function
if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()
