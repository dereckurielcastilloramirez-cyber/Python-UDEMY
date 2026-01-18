from tkinter import *
import random
import datetime
from tkinter import messagebox, filedialog
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

operador = ''

#funcion para calcular el total
def click_boton(numero):
    global operador #para usar la variable global
    operador = operador + numero
    visor_calculadora.delete(0, END) #borrar el contenido del visor
    visor_calculadora.insert(END, operador)

def borrar():
    global operador #para usar la variable global
    visor_calculadora.delete(0, END)
    operador = ''

def obtener_resultado():
    global operador #para usar la variable global
    resultado = str(eval(operador)) #funcion de evaluacion de expresion que recibe el operador y devuelve el resultado y hace el casting a string
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)
    operador = ''

def revisar_check():
    x = 0#contador de indices
    for c in cuadros_comida:
        if variables_comidas[x].get() == 1: #si el checkbox esta seleccionado
            cuadros_comida[x].config(state=NORMAL) #habilitar el cuadro de entrada 
            if cuadros_comida[x].get() == '0': #si el cuadro esta vacio
                cuadros_comida[x].delete(0, END) #deshabilitar el cero de texto
            cuadros_comida[x].focus() #enfocar el cursor en el cuadro de entrada
        else:
            cuadros_comida[x].config(state=DISABLED) #deshabilitar el cuadro de entrada 
            texto_comida[x].set('0') #escribir cero en el cuadro de texto
        x += 1

    y = 0#contador de indices
    for b in cuadros_bebida:
        if variables_bebidas[y].get() == 1: #si el checkbox esta seleccionado
            cuadros_bebida[y].config(state=NORMAL) #habilitar el cuadro de entrada 
            if cuadros_bebida[y].get() == '0':
                cuadros_bebida[y].delete(0, END) #deshabilitar el cero de texto
            cuadros_bebida[y].focus() #enfocar el cursor en el cuadro de entrada
        else:
            cuadros_bebida[y].config(state=DISABLED) #deshabilitar el cuadro de entrada 
            texto_bebida[y].set('0') #escribir cero en el cuadro de texto
        y += 1
    
    z = 0#contador de indices
    for p in cuadros_postres:
        if variables_postres[z].get() == 1: #si el checkbox esta seleccionado
            cuadros_postres[z].config(state=NORMAL) #habilitar el cuadro de entrada 
            if cuadros_postres[z].get() == '0':
                cuadros_postres[z].delete(0, END) #deshabilitar el cero de texto
            cuadros_postres[z].focus() #enfocar el cursor en el cuadro de entrada
        else:
            cuadros_postres[z].config(state=DISABLED) #deshabilitar el cuadro de entrada 
            texto_postres[z].set('0') #escribir cero en el cuadro de texto
        z += 1

#funcion para calcular el total-----------------------------------------------
def total():
    sub_total_comida = 0
    p=0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) *precios_comida[p])
        p+=1

    sub_total_bebida = 0
    p=0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) *precios_bebida[p])
        p+=1

    sub_total_postres = 0
    p=0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) *precios_postres[p])
        p+=1
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.16
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida,2)}') #redondeo a 2 decimales
    var_costo_bebida.set(f'$ {round(sub_total_bebida,2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres,2)}')
    var_subtotal.set(f'$ {round(sub_total,2)}')
    var_impuestos.set(f'$ {round(impuestos,2)}')
    var_TOTAL.set(f'$ {round(total,2)}')

#IMPRESION DE RECIBOS-----------------------------------------------
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*50 + '\n')
    texto_recibo.insert(END, f'items\t Cant.\tCosto Items\n')
    texto_recibo.insert(END, f'-'*60 + '\n')

    x= 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t{comida.get()}\t\t${round(precios_comida[x],2)}\n')
        x += 1
    x= 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t{bebida.get()}\t\t${round(precios_bebida[x],2)}\n')
        x += 1
    x= 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t{postre.get()}\t\t${round(precios_postres[x],2)}\n')
        x += 1
    texto_recibo.insert(END, f'-'*58 + '\n')
    texto_recibo.insert(END, f'Costo de Comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de Bebida:\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de Postres:\t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'Subtotal:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos 16%:\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'TOTAL:\t\t\t{var_TOTAL.get()}\n')

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')#pedir que guarde como archivo
    archivo.write(info_recibo)
    archivo.close() 
    messagebox.showinfo('Guardado', 'Recibo Guardado')

def resetear():
    texto_recibo.delete(1.0, END)
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, '')
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for variable in variables_comidas:
        variable.set(0)
    for variable in variables_bebidas:
        variable.set(0)
    for variable in variables_postres:
        variable.set(0)
    
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_TOTAL.set('')

# Iniciar tkinter
app = Tk()

#Tamaño de la ventana
app.geometry("1020x630+0+0")

#evitar que se pueda redimensionar la ventana
app.resizable(0,0)

#titulo de la ventana
app.title("RESTAURANTE - SISTEMA DE FACTURACION")

#Color de fondo
app.configure(bg="burlywood")

#Panel superior
panel_superior = Frame(app, bd = 1, relief = SUNKEN)
panel_superior.pack(side = TOP)

#etiqueta
etiqueta_titulo = Label(panel_superior, text = "SISTEMA DE FACTURACION", fg = "black", font = ("Dosis", 50), bg = "gray", width = 27)
etiqueta_titulo.grid(row = 0, column = 0)

#Panel izquierdo
panel_izquierdo = Frame(app, bd = 1, relief = SUNKEN)
panel_izquierdo.pack(side = LEFT)

#panel  costos
panel_costos = Frame(panel_izquierdo, bd = 1, bg = "azure4", relief = SUNKEN)
panel_costos.pack(side= BOTTOM)

# panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text = "Comidas", font = ("Dosis", 19, "bold"), bd = 1, relief = SUNKEN, fg = "azure4")
panel_comidas.pack(side= LEFT)

# panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text = "Bebidas", font = ("Dosis", 19, "bold"), bd = 1, relief = SUNKEN, fg = "azure4")
panel_bebidas.pack(side= LEFT)

# panel de postres
panel_postres = LabelFrame(panel_izquierdo, text = "Postres", font = ("Dosis", 19, "bold"), bd = 1, relief = SUNKEN, fg = "azure4")
panel_postres.pack(side= RIGHT)

# panel derecho
panel_derecho = Frame(app, bd = 1, relief = SUNKEN)
panel_derecho.pack(side = RIGHT)        

#panel calculadora
panel_calculadora = Frame(panel_derecho, bd = 1, relief = SUNKEN, bg = "burlywood")
panel_calculadora.pack(side = TOP)

#pane facturas
panel_facturas = Frame(panel_derecho, bd = 1, relief = SUNKEN, bg = "burlywood")
panel_facturas.pack()

#panel de botones
panel_botones = Frame(panel_derecho, bd = 1, relief = SUNKEN, bg = "burlywood")
panel_botones.pack()

#Lista de alimentos
lista_comidas = ["Pollo", "Carne", "Pescado", "Arroz", "Pasta", "Ensalada","Burrito", "Tacos"]
lista_bebidas = ["Agua", "Refresco", "Cerveza", "Vino", "Jugo", "Cafe", "Ron", "Tequila"]
lista_postres = ["Helado", "Pastel", "Fruta", "Flan", "Yogur", "Dulce", "Carlota", "Chocoflan"]

#Variables de costos
#lista de variables 
var_costo_comida = StringVar() #variable de tipo string que permite crear Tkinter
var_costo_comida.set('0') #establecer el texto de cada cuadro de entrada

var_costo_bebida = StringVar() #variable de tipo string que permite crear Tkinter
var_costo_bebida.set('0') #establecer el texto de cada cuadro de entrada

var_costo_postres = StringVar() #variable de tipo string que permite crear Tkinter
var_costo_postres.set('0') #establecer el texto de cada cuadro de entrada

var_subtotal = StringVar() #variable de tipo string que permite crear Tkinter
var_subtotal.set('0') #establecer el texto de cada cuadro de entrada

var_impuestos = StringVar() #variable de tipo string que permite crear Tkinter  
var_impuestos.set('0') #establecer el texto de cada cuadro de entrada

var_TOTAL = StringVar() #variable de tipo string que permite crear Tkinter  
var_TOTAL.set('0') #establecer el texto de cada cuadro de entrada
#generar items comida
variables_comidas = []
cuadros_comida = []
texto_comida = []
contador = 0
#checkbuttons
for comida in lista_comidas:    

    #crear checkbuttons  
    variables_comidas.append('') #para almacenar las elecciones de los checkbox
    variables_comidas[contador] = IntVar() #variable entera que permite crear Tkinter
                        #onvalue -> valor que va a tener la casilla al activarse y offvalue -> valor que va a tener la casilla al desactivarse
    comida = Checkbutton(panel_comidas, 
                         text = comida.title(), 
                         font = ("Dosis", 14, "bold"), 
                         onvalue = 1, offvalue = 0, 
                         variable=variables_comidas[contador],
                         command = revisar_check) #crear checkbox y almacenarla en variables_comidas
    comida.grid(row = contador, column = 0, sticky = W) #establecer filas y columnas  acomodado a la izquierda 
    
    #crear cuadros de entrada
    cuadros_comida.append('') #para almacenar los cuadros de entrada
    texto_comida.append('') #para almacenar los cuadros de entrada
    texto_comida[contador] = StringVar() #variable de tipo string que permite crear Tkinter
    texto_comida[contador].set('0') #establecer el texto de cada cuadro de entrada
    cuadros_comida[contador] = Entry(panel_comidas, 
                                     font = ('Dosis', 14, 'bold'),
                                     bd=1,
                                     width = 6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador]) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
    cuadros_comida[contador].grid(row = contador, 
                                  column = 1) #establecer filas y columnas
    contador += 1

#generar items bebida
variables_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador2 = 0
#checkbuttons
for bebida in lista_bebidas:      
    variables_bebidas.append('') #para almacenar las elecciones de los checkbox
    
    variables_bebidas[contador2] = IntVar() #variable entera que permite crear Tkinter
                        #onvalue -> valor que va a tener la casilla al activarse y offvalue -> valor que va a tener la casilla al desactivarse
    bebida = Checkbutton(panel_bebidas, 
                         text = bebida.title(), 
                         font = ("Dosis", 14, "bold"), 
                         onvalue = 1, offvalue = 0, 
                         variable=variables_bebidas[contador2],
                         command=revisar_check) #crear checkbox y almacenarla en variables_comidas
    bebida.grid(row = contador2, column = 1, sticky = W) #establecer filas y columnas  acomodado a la izquierda 
    
    #crear cuadros de entrada
    cuadros_bebida.append('') #para almacenar los cuadros de entrada
    texto_bebida.append('') #para almacenar los cuadros de entrada
    texto_bebida[contador2] = StringVar() #variable de tipo string que permite crear Tkinter
    texto_bebida[contador2].set('0') #establecer el texto de cada cuadro de entrada
    cuadros_bebida[contador2] = Entry(panel_bebidas, 
                                     font = ('Dosis', 14, 'bold'),
                                     bd=1,
                                     width = 6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador2]) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
    cuadros_bebida[contador2].grid(row = contador2, 
                                  column = 2) #establecer filas y columnas
    
    
    
    contador2 += 1


#generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador3 = 0
#checkbuttons
for postre in lista_postres:      
    variables_postres.append('') #para almacenar las elecciones de los checkbox
    variables_postres[contador3] = IntVar() #variable entera que permite crear Tkinter
                        #onvalue -> valor que va a tener la casilla al activarse y offvalue -> valor que va a tener la casilla al desactivarse
    postre = Checkbutton(panel_postres, 
                         text = postre.title(), 
                         font = ("Dosis", 14, "bold"), 
                         onvalue = 1, offvalue = 0, 
                         variable=variables_postres[contador3],
                         command=revisar_check) #crear checkbox y almacenarla en variables_comidas
    postre.grid(row = contador3, column = 2, sticky = W) #establecer filas y columnas  acomodado a la izquierda 
    
    #crear cuadros de entrada----------------------------------------
    cuadros_postres.append('') #para almacenar los cuadros de entrada
    texto_postres.append('') #para almacenar los cuadros de entrada
    texto_postres[contador3] = StringVar() #variable de tipo string que permite crear Tkinter
    texto_postres[contador3].set('0') #establecer el texto de cada cuadro de entrada
    cuadros_postres[contador3] = Entry(panel_postres, 
                                     font = ('Dosis', 14, 'bold'),
                                     bd=1,
                                     width = 6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador3]) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
    cuadros_postres[contador3].grid(row = contador3, 
                                  column = 3) #establecer filas y columnas
    
    contador3 += 1

#generar etiquetas de costos  COMIDA -----------------------------------
etiqueta_costo_comida = Label(panel_costos, 
                              text = "Costo Comida", 
                              font = ("Dosis", 14, "bold"), 
                              bg = "azure4", 
                              fg = "white")
etiqueta_costo_comida.grid(row = 0, 
                           column = 0) #pérmite ubicarla segun cuadricula

#CUADRO DE ENTRADA COMIDA 
texto_costo_comida = Entry(panel_costos, 
                           font = ('Dosis', 14, 'bold'),
                           bd=1,
                           width = 8,
                           state='readonly',
                           textvariable=var_costo_comida) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
texto_costo_comida.grid(row = 0, 
                        column = 1, padx = 41) #establecer filas y columnas

#generar etiquetas de costos  bebida ----------------------------------
etiqueta_costo_bebida = Label(panel_costos, 
                              text = "Costo Bebida", 
                              font = ("Dosis", 14, "bold"), 
                              bg = "azure4", 
                              fg = "white")
etiqueta_costo_bebida.grid(row = 1, 
                           column = 0) #pérmite ubicarla segun cuadricula

#CUADRO DE ENTRADA BEBIDAS 
texto_costo_bebida = Entry(panel_costos, 
                           font = ('Dosis', 14, 'bold'),
                           bd=1,
                           width = 8,
                           state='readonly',
                           textvariable=var_costo_bebida) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
texto_costo_bebida.grid(row = 1, 
                        column = 1, padx = 41) #establecer filas y columnas


#generar etiquetas de costos  POSTRES ----------------------------------
etiqueta_costo_postres = Label(panel_costos, 
                              text = "Costo Postres", 
                              font = ("Dosis", 14, "bold"), 
                              bg = "azure4", 
                              fg = "white")
etiqueta_costo_postres.grid(row = 2, 
                           column = 0) #pérmite ubicarla segun cuadricula

#CUADRO DE ENTRADA POSTRES 
texto_costo_postres = Entry(panel_costos, 
                           font = ('Dosis', 14, 'bold'),
                           bd=1,
                           width = 8,
                           state='readonly',
                           textvariable=var_costo_postres) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
texto_costo_postres.grid(row = 2, 
                        column = 1, padx = 41) #establecer filas y columnas


# SUBTOTALES ----------------------------------------------------------
etiqueta_subtotal = Label(panel_costos, 
                              text = "SUBTOTAL", 
                              font = ("Dosis", 14, "bold"), 
                              bg = "azure4", 
                              fg = "white")
etiqueta_subtotal.grid(row = 0, 
                           column = 2) #pérmite ubicarla segun cuadricula

#CUADRO DE ENTRADA POSTRES 
texto_subtotal = Entry(panel_costos, 
                           font = ('Dosis', 14, 'bold'),
                           bd=1,
                           width =8,
                           state='readonly',
                           textvariable=var_subtotal) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
texto_subtotal.grid(row = 0, 
                        column = 3, padx = 41) #establecer filas y columnas

# IMPUESTOS ----------------------------------------------------------
etiqueta_impuestos = Label(panel_costos, 
                              text = "IMPUESTOS", 
                              font = ("Dosis", 14, "bold"), 
                              bg = "azure4", 
                              fg = "white")
etiqueta_impuestos.grid(row = 1, 
                           column = 2) #pérmite ubicarla segun cuadricula

#CUADRO DE ENTRADA POSTRES 
texto_impuestos = Entry(panel_costos, 
                           font = ('Dosis', 14, 'bold'),
                           bd=1,
                           width = 8,
                           state='readonly',
                           textvariable=var_impuestos) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
texto_impuestos.grid(row = 1, 
                        column = 3, padx = 41) #establecer filas y columnas

# TOTAL ----------------------------------------------------------
etiqueta_TOTAL = Label(panel_costos, 
                              text = "TOTAL", 
                              font = ("Dosis", 14, "bold"), 
                              bg = "azure4", 
                              fg = "white")
etiqueta_TOTAL.grid(row = 2, 
                           column = 2) #pérmite ubicarla segun cuadricula

#CUADRO DE ENTRADA POSTRES 
texto_TOTAL = Entry(panel_costos, 
                           font = ('Dosis', 14, 'bold'),
                           bd=1,
                           width = 8,
                           state='readonly',
                           textvariable=var_TOTAL) #cada uno de los elementos de la lista de comidas tiene un cuadro de entrada
texto_TOTAL.grid(row = 2, 
                        column = 3, padx = 41) #establecer filas y columnas

#Botones ----------------------------------------------------------
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, 
                   text = boton.title(), 
                   font = ("Dosis", 16, "bold"), 
                   fg = "white",
                   bg = "azure4",
                   bd = 1,
                   width = 7)
    
    botones_creados.append(boton) #guardar los botones en una lista
    boton.grid(row = 0, column = columnas) #pérmite ubicarla segun cuadricula
    columnas += 1 #aumentar columnas
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
#AREA DE RECIBOS ----------------------------------------------------------
texto_recibo = Text(panel_facturas,
                    font = ('Dosis', 13, 'bold'),
                    bd=1,
                    width = 40,
                    height = 6)

texto_recibo.grid(row = 0, column = 0) #establecer filas y columnas

#calculadora

visor_calculadora = Entry(panel_calculadora,
                          font = ('Dosis', 16, 'bold'),
                          width=32,
                          bd = 1)
visor_calculadora.grid(row = 0, 
                       column=0,
                       columnspan = 4)

# botones
botones = ['7', '8', '9', '+',
           '4', '5', '6', '-',
           '1', '2', '3', '*',
           '=', 'B', '0', '/']

botones_guardados = []

fila = 1
columna = 0

for boton in botones:
    boton = Button(panel_calculadora, 
                   text = boton.title(), 
                   font = ("Dosis", 18, "bold"), 
                   fg = "white",
                   bg = "azure4",
                   bd = 1,
                   width = 6)
    
    botones_guardados.append(boton) #guardar los botones en una lista
    boton.grid(row = fila, 
               column = columna) #pérmite ubicarla segun cuadricula
    
    if columna == 3:
        fila += 1
    
    columna += 1 #aumentar columnas
    
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)

#evitar que se cierre la ventana
app.mainloop()