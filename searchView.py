from tkinter import *
from tkinter import font

class searchView(Frame):
    def __init__(self, search):
        super().__init__(search)
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
        self.btnNext = Button(self, text='Siguiente', font=fontLabel)
        self.btnNext.place(x=600, y=300)
        
    def read(self):
        

search = Tk()
app = searchView(search)
app.mainloop()