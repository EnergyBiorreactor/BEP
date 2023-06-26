import tkinter as tk
import numpy as np
from PIL import*
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import math as m

#crear una ventana
root = tk.Tk()
#root.configure(bg="hot pink")

#imagen de reactor

imagen1 = ImageTk.PhotoImage(Image.open("biorreactor_1.png"))

#imagen de logo Universidad
imagen2 = ImageTk.PhotoImage(Image.open("logo_udea.png"))

#objeto label
foto1 = tk.Label(root,image = imagen1).grid(row = 1, column = 5, rowspan = 13)#, columnspan = )#, , padx = 5, pady = 5)

#objeto label
foto2 = tk.Label(root,image = imagen2).grid(row = 0, column = 0, columnspan = 3)#, rowspan = 8, padx = 5, pady = 5)


#titulo de la ventana
root.title("Necesidades energeticas en bio-reactores (Batch)")



print("+++++++++++++++++++++++++++++++++++++++++++")

# Crear etiquetas y cuadros de entrada para cada característica
etiqueta1 = tk.Label(root, text="volumen del reactor (l)").grid(row=1,column=0)
etiqueta2 = tk.Label(root, text="volumen de chaqueta (l)").grid(row=2)
etiqueta3 = tk.Label(root, text="Temperatura del nucleo del reactor (°C)").grid(row=3)
etiqueta4 = tk.Label(root, text="Temperatura de la chaqueta (°C)").grid(row=4)
etiqueta5 = tk.Label(root, text="densidad del flujo del reactor (g/l)").grid(row=5)
etiqueta6 = tk.Label(root, text="densidad del flujo de la chaqueta (g/l)").grid(row=6)
etiqueta7 = tk.Label(root, text="capacidad calorifica de la biomasa del reactor  (J/(kgmolK))").grid(row=7)
etiqueta8 = tk.Label(root, text="capacidad calorifica del fluido de la chaqueta del reactor (J/(kgmolK))").grid(row=8)
etiqueta9 = tk.Label(root, text="coeficiente de transferencia de calor (J/hm2K)").grid(row=9)
etiqueta10 = tk.Label(root, text="cambio  de entalpia (kJ/mol )").grid(row=10)
etiqueta11 = tk.Label(root, text="constante de gas ideal").grid(row=11)
etiqueta12 = tk.Label(root, text="area total de tranferencia de calor (m2)").grid(row=12)
etiqueta13 = tk.Label(root, text="flujo de la chaqueta (1/h)").grid(row=13)

#RECUADROS DE ENTRADA DE DATOS
volumen_del_reactor_entry = tk.Entry(root)
volumen_del_reactor_entry.grid(row=1, column=1)
volumen_de_chaqueta_entry = tk.Entry(root)
volumen_de_chaqueta_entry.grid(row=2, column=1)
temperatura_del_nucleo_del_reactor_entry = tk.Entry(root)
temperatura_del_nucleo_del_reactor_entry.grid(row=3, column=1)
temperatura_de_la_chaqueta_entry = tk.Entry(root)
temperatura_de_la_chaqueta_entry.grid(row=4, column=1)
densidad_del_flujo_del_reactor_entry = tk.Entry(root)
densidad_del_flujo_del_reactor_entry.grid(row=5, column=1)
densidad_del_flujo_de_la_chaqueta_entry = tk.Entry(root)
densidad_del_flujo_de_la_chaqueta_entry.grid(row=6, column=1)
capacidad_calorifica_de_la_biomasa_del_reactor_entry = tk.Entry(root)
capacidad_calorifica_de_la_biomasa_del_reactor_entry.grid(row=7, column=1)
capacidad_calorifica_del_fluido_de_la_chaqueta_del_reactor_entry = tk.Entry(root)
capacidad_calorifica_del_fluido_de_la_chaqueta_del_reactor_entry.grid(row=8, column=1)
coeficiente_de_transferencia_de_calor_entry = tk.Entry(root)
coeficiente_de_transferencia_de_calor_entry.grid(row=9, column=1)
cambio_de_entalpia_entry = tk.Entry(root)
cambio_de_entalpia_entry.grid(row=10, column=1)
constante_de_gas_ideal_entry = tk.Entry(root)
constante_de_gas_ideal_entry.grid(row=11, column=1)
area_total_de_transferencia_de_calor_entry = tk.Entry(root)
area_total_de_transferencia_de_calor_entry.grid(row=12, column=1)
flujo_de_la_chaqueta_entry = tk.Entry(root)
flujo_de_la_chaqueta_entry.grid(row=13, column=1)

# Función para borrar el contenido de los campos de entrada
def clear_entries():
    volumen_del_reactor_entry.delete(0, tk.END)
    volumen_de_chaqueta_entry.delete(0, tk.END)
    temperatura_del_nucleo_del_reactor_entry.delete(0, tk.END)
    temperatura_de_la_chaqueta_entry.delete(0, tk.END)
    densidad_del_flujo_del_reactor_entry.delete(0, tk.END)
    densidad_del_flujo_de_la_chaqueta_entry.delete(0, tk.END)
    capacidad_calorifica_de_la_biomasa_del_reactor_entry.delete(0, tk.END)
    capacidad_calorifica_del_fluido_de_la_chaqueta_del_reactor_entry.delete(0, tk.END)
    coeficiente_de_transferencia_de_calor_entry.delete(0, tk.END)
    cambio_de_entalpia_entry.delete(0, tk.END)
    constante_de_gas_ideal_entry.delete(0, tk.END)
    area_total_de_transferencia_de_calor_entry.delete(0, tk.END)
    flujo_de_la_chaqueta_entry.delete(0, tk.END)

# Crear un botón para borrar el contenido de los campos de entrada
clear_button = tk.Button(root, text="Limpiar", command=clear_entries)
clear_button.grid(row=14, column=1, padx=10, pady=5)


# Función para realizar la predicción
def predict_energy():
  #INDICAR QUE SE HA PRESIONADO EL BOTÓN
  print("¡El botón fue presionado!")

  # Obtener los valores de entrada del usuario
  volumen_del_reactor = float(volumen_del_reactor_entry.get())
  volumen_de_chaqueta = float(volumen_de_chaqueta_entry.get())
  temperatura_del_nucleo_del_reactor = float(temperatura_del_nucleo_del_reactor_entry.get())
  temperatura_de_la_chaqueta= float(temperatura_de_la_chaqueta_entry.get())
  densidad_del_flujo_del_reactor = float(densidad_del_flujo_del_reactor_entry.get())
  densidad_del_flujo_de_la_chaqueta= float(densidad_del_flujo_de_la_chaqueta_entry.get())
  capacidad_calorifica_de_la_biomasa_del_reactor = float(capacidad_calorifica_de_la_biomasa_del_reactor_entry.get())
  capacidad_calorifica_del_fluido_de_la_chaqueta_del_reactor = float(capacidad_calorifica_del_fluido_de_la_chaqueta_del_reactor_entry.get())
  coeficiente_de_transferencia_de_calor = float(coeficiente_de_transferencia_de_calor_entry.get())
  cambio_de_entalpia = float(cambio_de_entalpia_entry.get())
  constante_de_gas_ideal = float(constante_de_gas_ideal_entry.get())
  area_total_de_transferencia_de_calor = float(area_total_de_transferencia_de_calor_entry.get())
  flujo_de_la_chaqueta = float(flujo_de_la_chaqueta_entry.get())
  

#DATOS CONOCIDOS
  A = area_total_de_transferencia_de_calor # area de transferencia de calor (m**2)
  cpr  = capacidad_calorifica_de_la_biomasa_del_reactor #capacidad_calorifica (j/gramos°C)
  cpj = capacidad_calorifica_del_fluido_de_la_chaqueta_del_reactor #capacidad_calorifica_en_chaqueta(j/gramos°C)
  Fj  = flujo_de_la_chaqueta
  Tjin  = temperatura_de_la_chaqueta
  U = coeficiente_de_transferencia_de_calor
  V = volumen_del_reactor
  Vj = volumen_de_chaqueta
  rhor = densidad_del_flujo_del_reactor
  rhoj = densidad_del_flujo_de_la_chaqueta
  dH = cambio_de_entalpia
  R = constante_de_gas_ideal
  Ea = 55000 # Energia de activacion (j/mol)
  Cs0 = 15 # concentracion del sustrato (g/l)
  CP0 = 0 # concentracion del producto (g/l)
  k0 = 9.5e8

  #CICLO DE TEMPERATURAS
  
  T0 =  temperatura_del_nucleo_del_reactor
  Tj0 = temperatura_del_nucleo_del_reactor
  Tj = 21.5
  h = 1e-3
  i = 0


  #ECUACIONES DIFERENCIALES
  def funcion_1(T, Tj, Cs, CP):
      return -k0*m.exp(-Ea/(R*(T+273.15)))*Cs

  def funcion_2(T, Tj, Cs, CP):
      return k0*m.exp(-Ea/(R*(T+273.15)))*Cs

  def funcion_3(T, Tj, Cs, CP):
      return -(U*A/(V*rhor*cpr))*(T-Tj) + ((-dH)/(rhor*cpr))*k0*m.exp(-Ea/(R*(T+273.15)))*Cs

  def funcion_4(T, Tj, Cs, CP):
      return ((Fj/Vj)*(Tjin-Tj)) + (U*A/(Vj*rhoj*cpj))*(T-Tj)
  
  
  #definición del paso
  h = 1e-4

  temp_reactor = []
  temp_chaqueta = []
  tiempo = []
  c_sustrato = []
  c_producto = []

  #Condiciones iniciales cuanto t = 0
  t_k      = 0
  Cs_k    = Cs0
  CP_k    = CP0
  T_k     = T0
  Tj_k    = Tj0

  #Implementación del método:
  k = 0
  while t_k <= 60:
      #añadiendo las variables a listas
      temp_reactor.append(T_k)
      temp_chaqueta.append(Tj_k)
      tiempo.append(t_k)
      c_sustrato.append(Cs_k)
      c_producto.append(CP_k)

      #Funciones
      Cs_kmas1    = Cs_k  + h*funcion_1(T_k, Tj_k, Cs_k, CP_k)
      CP_kmas1    = CP_k  + h*funcion_2(T_k, Tj_k, Cs_k, CP_k)
      T_kmas1     = T_k   + h*funcion_3(T_k, Tj_k, Cs_k, CP_k)
      Tj_kmas1    = Tj_k  + h*funcion_4(T_k, Tj_k, Cs_k, CP_k)

     
      #Actualizacion de funciones
      Cs_k    = Cs_kmas1
      CP_k    = CP_kmas1
      T_k     = T_kmas1
      Tj_k    = Tj_kmas1

      #paso del tiempo
      t_k = t_k + h
      k = k + 1

      #A las 2 horas
      if t_k >= 5.0 and t_k <= 5.0001:
          print('5.0h Cs = ', Cs_kmas1)
          print('5.0h CPs = ', CP_kmas1)
          print('5.0h Tj = ', Tj_kmas1)
          print('5.0h T = ', T_kmas1)
          print('5.0h k = ', k)
          print(funcion_1(T_k, Tj_k, Cs_k, CP_k))


  print('Estado estable Cs = ', Cs_kmas1)
  print('Estado estable CPs = ', CP_kmas1)
  print('Estado estable Tj = ', Tj_kmas1)
  print('Estado estable T = ', T_kmas1)
  print('Estado estable k = ', k)
  print(funcion_1(T_k, Tj_k, Cs_k, CP_k))

  plt.subplot(1, 2, 1)
  plt.plot(tiempo, temp_reactor, label = 'reactor')
  plt.plot(tiempo, temp_chaqueta, label = 'chaqueta')
  plt.xlabel('Tiempo (h)')
  plt.ylabel('Temperatura (°C)')
  plt.legend(loc = 'best')

  plt.subplot(1, 2, 2)
  plt.plot(tiempo, c_sustrato, label = 'sustrato')
  plt.plot(tiempo, c_producto, label = 'producto')    
  plt.xlabel('Tiempo (h)')
  plt.ylabel('Concentración (g/l)')
  plt.legend(loc = 'best')
  plt.show()



  
# Crear un botón para realizar la predicción
predict_button = tk.Button(root, text="prediccion", command=predict_energy)
predict_button.grid(row=15, column=1, columnspan=3)
predict_button.configure(bg="white")

# Crear una etiqueta para mostrar el resultado de la predicción
result_label = tk.Label(root, text="resultados")
result_label.grid(row=16, column=1, columnspan=3)

button = tk.Button(root, text="Haz clic aquí",command = predict_energy)

root.mainloop()


#Datos
k0 = 9.5e8
A = 0.2
Cs0 = 15
CP0 = 0
cpr = 4.18
cpj = 4.18
Ea = 55000
Fj = 5
T0 = 21.5
Tj0 = 21.5
Tjin = 21.5
U = 3.6e5
V = 20
Vj = 6.637
rhor = 1080
rhoj = 1000
dH = 518
R = 8.314




"""# Crear un botón para realizar la predicción
predict_button = tk.Button(root, text="prediccion", command=predict_energy)
predict_button.grid(row=15, column=1, columnspan=3)
predict_button.configure(bg="white")

# Crear una etiqueta para mostrar el resultado de la predicción
result_label = tk.Label(root, text="resultados")
result_label.grid(row=16, column=1, columnspan=3)

button = tk.Button(root, text="Haz clic aquí",command = predict_energy)"""