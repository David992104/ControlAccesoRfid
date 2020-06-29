from tkinter import *
from tkinter import font
from read import *
from consultas import searchData
import os
import time
from tkinter import messagebox

class searchView(Frame):
    def __init__(self, search):
        Frame.__init__(self, search)
        search.title("Busqueda de usuarios")
        search.configure(width=800, height=400)
        self.place(relwidth=1, relheight=1)

        fontLabel = font.Font(family="Arial", size="16")
        
        #area de variables de la ventana
        self.ruta = StringVar()
        self.nombre = StringVar()
        self.ape = StringVar()
        self.matricula = StringVar()
        self.area = StringVar()
        self.puesto = StringVar()
        self.ruta.set("""/home/pulcera/Documentos/rfid/img/avatars.png""")
        self.imagen = PhotoImage(file=self.ruta.get())
        
        #Agregando los campos
        self.avatar = Label(self, image=self.imagen)
        self.avatar.place(x = 50, y=50, width=240, height=300)
        #self.avatar = Canvas(self,width=240, height=300, background="black")
        #self.avatar.grid(column=0, row=0)
        #self.avatar.create_image(50, 50, image=self.imagen, anchor='nw')
        #self.avatar.place(x=50, y=50)
        self.lblNombre = Label(self, text='Nombre: ', font=fontLabel)
        self.lblNombre.place(x=350, y=50)
        self.lblApellidos = Label(self, text="Apellidos: ", font=fontLabel)
        self.lblApellidos.place(x=400, y=100)
        self.lblMatricula = Label(self, text='Matricula', font=fontLabel)
        self.lblMatricula.place(x=350, y=150)
        self.lblArea = Label(self, text='Area: ', font=fontLabel)
        self.lblArea.place(x=350, y=200)
        self.lblPuesto = Label(self, text='Puesto: ', font=fontLabel)
        self.lblPuesto.place(x=350, y=250)
        self.btnNext = Button(self, text='Siguiente', font=fontLabel, command=self.read)
        self.btnNext.place(x=600, y=300)
        
    def read(self):
        self.lblNombre.config(text='Nombre')
        self.lblApellidos.config(text = 'Apellidos')
        self.lblMatricula.config(text='Matricula')
        self.lblArea.config(text='Area')
        self.lblPuesto.config(text='Puesto')
        self.ruta.set("""/home/pulcera/Documentos/rfid/img/avatars.png""")
        self.imagen = PhotoImage(file=self.ruta.get())
        self.avatar.configure(image=self.imagen)
        
        serie = readid()
        clave = readtext()
        print(serie)
        print(clave)
        data = searchData(serie, clave)
        #print(data)
        try:
            self.lblNombre.config(text=data[0][0])
            self.lblApellidos.config(text = data[0][1] + ' ' + data[0][2])
            self.lblMatricula.config(text=data[0][3])
            self.lblArea.config(text=data[0][5])
            self.lblPuesto.config(text=data[0][6])
            
            path = '/home/pulcera/Documentos/rfid/img/imagen.png'
            with open(path, 'wb') as file:
                file.write(data[0][4])
                
            if os.path.exists(path):
           
                self.imagen = PhotoImage(file=path)
                self.avatar.configure(image=self.imagen)
        except:
            print('No existe el usuario')
            messagebox.showwarning("Usuario no existe", "El usuario no existe")
            
         #   os.remove(path)

search = Tk()
app = searchView(search)
app.mainloop()