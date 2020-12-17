import os
from login import *
list_clientes = []

def categorias ():
  os.system('cls')
  print(":::: MENU CLIENTES ::::")
  print("[1.] INGRESAR NUEVO CLIENTE")
  print("[2.] LISTAR CLIENTES")
  print("[3.] BUSCAR UN CLIENTE")
  print("[4.] MODIFICAR UN CLIENTE")
  print("[5.] ELIMINAR CLIENTE")
  print("[6.] VOLVER AL MENU")
  print("[7.] SALIR")
  
  op = input(".:: DIGITE UNA OPCION: ")

  if op == '1' :
    ingresar_cliente()
  elif op == '2' :
    listar_cliente()
  elif op == '3' :
    buscar_cliente()
  elif op == '4' :
    modificar_cliente()
  elif op == '5' :
    eliminar_cliente()
    
  elif op == '6':
    clientes()

  elif op == '7':
      salir()
    
def ingresar_cliente():
  os.system('cls')
  print("::: INGRESO NUEVO CLIENTE ::: ")
  nomclient = (input(" DIGITE CLIENTE: "))
  list_clientes.append(nomclient)
  key = input(" EL CLIENTE HA SIDO ALMACENADA CON EXITO !. Presione cualquier tecla para volver al menú")
  categorias()

def listar_cliente():
  os.system('cls')
  print("::: LISTADO DE CLIENTES ::: ")
  if len(list_clientes) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :  
    print(list_clientes)
    
  key = input("Presione cualquier tecla para volver al menú") 
  clientes()

def buscar_cliente():
  os.system('cls')
  buscar = 0
  print("::: BÚSQUEDA DE CLIENTES ::: ")
  
  if len(list_categorias) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CLEINTE A BUSCAR: ")
    i = 0
    encontrado = False
    while i < len(list_clientes) :#-1
      if buscar == list_clientes[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      print("::: CLIENTE FUE ENCONTRADO EN LA LISTA")
    else :
      print("::: CLIENTE NO FUE ENCONTRADA EN LA LISTA")
          
  key = input("Presione cualquier tecla para volver al menú")
  clientes()

def modificar_cliente():
  os.system('cls')
  print("::: MODIFICACIÓN DE CLIENTE ::: ")
  if len(list_clientes) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CLIENTE A MODIFICAR: ")
    i = 0
    encontrado = False
    while i < len(list_clientes) :
      if buscar == list_clientes[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      modificar = input(" DIGITE NUEVO CLIENTES")
      list_clientes.insert(len(list_clientes),modificar)
    else :
      print("::: EL CLIENTE NO FUE ENCONTRADO EN LA LISTA")
  key = input("Presione cualquier tecla para volver al menú")
  clientes()

def eliminar_cliente():
	os.system('cls')
	print("::::::: ELIMINAR CLIENTE :::::::")
	elim = input("DIGITE CLIENTE A ELIMINAR")
	list_clientes.remove(elim)
	key = input("	Persione cualquier tecla para volver al menu")
	clientes()

def salir ():
    print("Hasta Luego, vuelve pronto, eres importante, cuidate")
    sys.exit()