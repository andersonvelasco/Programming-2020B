import os
from login import *
list_productos = []

def productos ():
  os.system('cls')
  print(":::: MENU PRODUCTOS ::::")
  print("[1.] INGRESAR NUEVO PRODUCTO")
  print("[2.] LISTAR PRODUCTOS")
  print("[3.] BUSCAR PRODUCTOS")
  print("[4.] MODIFICAR PRODUCTO")
  print("[5.] ELIMINAR PRODUCTO")
  print("[6.] VOLVER AL MENU")
  
  op = input(".:: Digite una opción: ")

  if op == '1' :
    ingresar_producto()
  elif op == '2' :
    listar_producto()
  elif op == '3' :
    buscar_producto()
  elif op == '4' :
    modificar_producto()
  elif op == '5' :
    eliminar_producto()
    
  elif op == '6':
    producto()
  else :
    print("::: Vuelve pronto :::")
    
def ingresar_producto():
  os.system('clear')
  print("::: INGRESO NUEVO PRODUCTO ::: ")
  nomproducto = (input(" DIGITE PRODUCTO A ALMACENAR: "))
  list_productos.append(nomproducto)
  key = input(" EL PRODUCTO HA SIDO ALMACENADO CON EXITO ! . Presione cualquier tecla para volver al menú")
  productos()

def listar_producto():
  os.system('clear')
  print("::: LISTADO DE PRODUCTOS ::: ")
  if len(list_productos) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :  
    print(list_productos)
    
  key = input("Presione cualquier tecla para volver al menú") 
  productos()

def buscar_producto():
  os.system('clear')
  buscar = 0
  print("::: BÚSQUEDA DE PRODUCTOS ::: ")
  if len(list_productos) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE PRODUCTO A BUSCAR: ")
    i = 0
    encontrado = False
    while i < len(list_productos) :#-1
      if buscar == list_roductos[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      print("::: EL PRODUCTO FUE ENCONTRADO EN LA LISTA")
    else :
      print("::: EL PRODUCTO NO FUE ENCONTRADO EN LA LISTA")
          
  key = input("Presione cualquier tecla para volver al menú")
  productos()

def modificar_producto():
  os.system('cls')
  print("::: MODIFICACIÓN DE PRODUCTO ::: ")
  if len(list_roductos) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE PRODUCTO A MODIFICAR: ")
    i = 0
    encontrado = False
    while i < len(list_productos) :#-1
      if buscar == list_productos[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      #Categorias.remove = Categorias[i]
      modificar = input(" DIGITE EL PRODUCTO")
      list_productos.insert(list_productos, modificar)
    else :
      print("::: EL PRODUCTO NO FUE ENCONTRADO EN LA LISTA")
  key = input("Presione cualquier tecla para volver al menú")
  productos()

def eliminar_productos():
	os.system('cls')
	print("::::::: ELIMINAR PRODUCTOS :::::::")
	elim = input("DIGITE PRODUCTO A ELIMINAR")
	list_produ.remove(elim)
	key = input("	Persione cualquier tecla para volver al menu")
	productos()