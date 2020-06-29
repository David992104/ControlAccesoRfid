import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog
import time
#from getData import *
from generateClave import generate
from write import writeClave
from consultas import saveUser, getCarreras, getOcupacion
from read import readid

class main(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master=None)
        self.master.title("Registro de usuarios")        
        self.master.configure(width=900, height=600)  
        self.place(relwidth=1, relheight=1)

        #Estilo de letras para cada cosa
        fontTitle = tkFont.Font(family="Lucida Grande", size=20, weight='bold')  
        fontLabel = tkFont.Font(family="Arial", size="16")
        fontEntry = tkFont.Font(family="Lucida", size="16")

        #Seccion de los titulos tienen una altura de 105px
        self.titulo = ttk.Label(self, text="Registro de usuario y", font=fontTitle)
        self.titulo.place(x=300, y=15, width=300, height=35)
        self.titulo2 = ttk.Label(self, text="Asignacion de tarjetas", font=fontTitle)
        self.titulo2.place(x=300, y=50, width=300, height=35)
        self.separatorH = ttk.Separator(orient='horizontal')
        self.separatorH.place(x=0, y=100, width=900, height=5)

        #Seccion de imagen tendran una altura de 495px y anchura de 300px
        self.ruta = StringVar()
        self.ruta.set("/home/pulcera/Documentos/rfid/img/avatars.png")
        self.imagen = PhotoImage(file=self.ruta.get())
        self.avatar = Label(self, image=self.imagen)     
        self.avatar.place(x=30, y=135, width=240, height=300)               
        self.btnLoad = ttk.Button(self, text='Cargar imagen', command=self.cargarImagen)
        self.btnLoad.place(x=100, y=485, width=100, height=30)
        self.btnCapture = ttk.Button(self, text='Tomar imagen', command=self.capturarImagen)
        self.btnCapture.place(x=100, y=525, width=100, height=30)
        self.separatorV = ttk.Separator(orient='vertical')
        self.separatorV.place(x=300, y=105, width=5, height=495)

        #Seccion del registro altura 495px anchura 295px
        self.lblNombre = ttk.Label(self, text="Nombre (s): ", font=fontLabel)
        self.lblNombre.place(x=365, y=135, width=240, height=30)
        self.lblApe1 = ttk.Label(self, text='Apellido 1: ', font=fontLabel)
        self.lblApe1.place(x=365, y=185, width=240, height=30)
        self.lblApe2 = ttk.Label(self, text='Apellido 2: ', font=fontLabel)
        self.lblApe2.place(x=365, y=235, width=240, height=30)
        self.lblMatricula = ttk.Label(self, text='Matricula: ', font=fontLabel)
        self.lblMatricula.place(x=365, y=285, width=240, height=30)
        self.lblCarrera = ttk.Label(self, text='Carrera: ', font=fontLabel)
        self.lblCarrera.place(x=365, y=335, width=240, height=30)
        self.lblOcupacion = ttk.Label(self, text='Ocupacion: ', font=fontLabel)
        self.lblOcupacion.place(x=365, y=385, width=240, height=30)

        #Area de variables
        self.nombre = tk.StringVar()
        self.ape1 = tk.StringVar()
        self.ape2 = tk.StringVar()
        self.matricula = tk.StringVar()

        self.txtNombre = ttk.Entry(self, textvariable=self.nombre, font=fontEntry)
        self.txtNombre.place(x=500, y=135, width=300, height=30)
        self.txtApe1 = ttk.Entry(self, textvariable=self.ape1, font=fontEntry)
        self.txtApe1.place(x=500, y=185, width=300, height=30)
        self.txtApe2 = ttk.Entry(self, textvariable=self.ape2, font=fontEntry)
        self.txtApe2.place(x=500, y=235, width=300, height=30)
        self.txtMatricula = ttk.Entry(self, textvariable=self.matricula, font=fontEntry)
        self.txtMatricula.place(x=500, y=285, width=300, height=30)
        self.cmbCarrera = ttk.Combobox(self, font=fontEntry, state='readonly')
        self.cmbCarrera.place(x=500, y=335, width=300, height=30)
        self.cmbCarrera['values'] = getCarreras()
        self.cmbOcupacion = ttk.Combobox(self, font=fontEntry, state='readonly')
        self.cmbOcupacion.place(x=500, y=385, width=300, height=30)
        self.cmbOcupacion['values'] = getOcupacion()

        self.btnCancelar = ttk.Button(self, text='Cancelar', command=self.cancelar)
        self.btnCancelar.place(x=350, y=450, width=150, height=40)
        self.btnGuardar = ttk.Button(self, text='Guardar', command=self.enviarDatos)
        self.btnGuardar.place(x=600, y=450, width=150, height=40)
            
    def cancelar(self):
        op = MessageBox.askokcancel('Salir', '¿Desea Salir ?')
        if op == True:
            self.master.destroy()
        
    def enviarDatos(self):
        title = 'Guadar datos de ' + str(self.nombre.get())
        nombre = str(self.nombre.get())
        ape1 = str(self.ape1.get())
        ape2 = str(self.ape2.get())
        mat = str(self.matricula.get())
        carrera = str(self.cmbCarrera.get())
        ocup = str(self.cmbOcupacion.get())
        ruta = self.ruta
        
        d = saveData(root, title, nombre, ape1, ape2, mat, carrera, ocup, ruta)
        self.destroy()
        self.__init__(self.master)
        

    def cargarImagen(self):
        print('Cargando imagen')
        file_path = filedialog.askopenfilename()
        self.ruta = (file_path)
        print(self.ruta)
        self.imagen = PhotoImage(file=file_path)
        self.avatar.image = self.imagen
        self.avatar.configure(image=self.imagen)

    def capturarImagen(self):
        print('Capturando')
        
        
class saveData:
    def __init__(self, parent, title, nom, ape1, ape2, matricula, car, ocup, img):
        self.saveData = Toplevel(parent)
        self.saveData.transient(parent)
        self.saveData.grab_set()
        self.saveData.title(title)
        self.saveData.configure(width=500, height=400)
        
        fontLabel = tkFont.Font(family="Arial", size="16")
        
        self.nombre = 'Nombre: ' + nom + ' ' + ape1 + ' ' + ape2
        mat = 'Matricula: ' + matricula
        carrera = 'Area ' + car
        ocupacion = 'Siendo ' +  ocup
        self.lblNombre = Label(self.saveData, text=self.nombre, font=fontLabel)
        self.lblNombre.place(x=20, y=20)
        self.lblMat = Label(self.saveData, text=mat, font=fontLabel)
        self.lblMat.place(x=20, y=50)
        self.lblCarrera = Label(self.saveData, text=carrera, font=fontLabel)
        self.lblCarrera.place(x=20, y= 80)
        self.lblOcupacion = Label(self.saveData, text=ocupacion, font=fontLabel)
        self.lblOcupacion.place(x=20, y= 110)
        
        self.btnCancel = Button(self.saveData, text='Cancelar', command=self.cancelar)
        self.btnCancel.place(x=20, y=250)
        self.btnConfirmar = Button(self.saveData, text='Confirmar', command=self.confirmar)
        self.btnConfirmar.place(x=300, y=250)
        
        self.idTarjeta = StringVar()
        self.claveTarjeta = StringVar()
        self.nom = nom
        self.ape1 = ape1
        self.ape2 = ape2
        self.matricula = matricula
        self.car = car
        self.ocup = ocup
        self.img = img
        
    def cancelar(self):
        self.saveData.destroy()
        
    def confirmar(self):
        MessageBox.showinfo("Añadir tarjeta", 'Prepara tu objeto con sensor a registrar y colocalo en el sensor ')
        
        addcard = addCard(root, 'Añade tarejeta para ' + self.nombre, self.claveTarjeta, self.idTarjeta)
        
        saveUser(self.nom, self.ape1, self.ape2, self.matricula, self.car, self.ocup, self.img, str(self.claveTarjeta.get()), str(self.idTarjeta.get()))
        
        self.saveData.destroy()
        
    
class addCard:
    def __init__(self, parent, title, idClave, serie):
        self.idClave = idClave
        self.serieTag = serie
        
        self.card = Toplevel(parent)
        self.card.transient(parent)
        self.card.grab_set()
        self.card.title(title)
        self.card.configure(width=400, height=200)
        
        self.idRfid = Label(self.card, text="Coloca tu tarjeta ")
        self.idRfid.place(x=100, y=30, width=200, height=30)
        self.btnLeer = Button(self.card, text='Leer otra tarjeta', command=self.readId)
        self.btnLeer.place(x=250, y=150, width=150, height=30)
        self.btnCancelar = Button(self.card, text='Cancelar', command=self.cancelId)
        self.btnCancelar.place(x=50, y=150, width=100, height=30)
        
        self.readId()
                    
    def readId(self):
        idTag = str(readid())
        
        self.idRfid.config(text='Numero ' + idTag)

        self.serieTag.set(idTag)
        
        #ClaveUser sera el identificadore de la tarjeta para el usuario
        claveUser = generate()
        writeClave(claveUser)
        self.idClave.set(claveUser)
                
        time.sleep(1)
        res = MessageBox.askokcancel('Continuar', 'Desea guaradar a el usuario')
        
        if res == True:
            MessageBox.showinfo("Guardado ", 'Usuario guardado')
            self.card.destroy()
            
    def cancelId(self):
        self.card.destroy()
        


root = tk.Tk()
a = main(root)
root.mainloop()



