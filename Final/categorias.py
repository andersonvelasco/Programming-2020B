import os
from login import *
list_categorias = []

def categorias ():
  os.system('cls')
  print(":::: MENU CATEGORIAS ::::")
  print("[1.] INGRESAR NUEVA CATEGORIA")
  print("[2.] LISTAR CATEGORIAS")
  print("[3.] BUSCAR UNA CATEGORIA")
  print("[4.] MODIFICAR CATEGORIA")
  print("[5.] ELIMINAR CATEGORIA")
  print("[6.] VOLVER AL MENU")
  print("[7.] SALIR")
  
  op = input(".:: DIGITE UNA OPCION: ")

  if op == '1' :
    ingresar_categoria()
  elif op == '2' :
    listar_categoria()
  elif op == '3' :
    buscar_categoria()
  elif op == '4' :
    modificar_categoria()
  elif op == '5' :
    eliminar_categoria()
    
  elif op == '6':
    categorias()
  elif op == '7':
    salir()
    
def ingresar_categoria():
  os.system('cls')
  print("::: INGRESO NUEVA CATEGORIA ::: ")
  nomcategoria = (input(" DIGITE CATEGORIA A ALMACENAR: "))
  list_categorias.append(nomcategoria)
  key = input(" LA CATEGORIA HA SIDO ALMACENADA CON EXITO !. Presione cualquier tecla para volver al menú")
  categorias()

def listar_categoria():
  os.system('cls')
  print("::: LISTADO DE CATEGORIAS ::: ")
  if len(list_categorias) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :  
    print(list_categorias)
    
  key = input("Presione cualquier tecla para volver al menú") 
  categorias()

def buscar_categoria():
  os.system('cls')
  buscar = 0
  print("::: BÚSQUEDA DE CATEGORIAS ::: ")
  #Here we must to look for a number
  
  if len(list_categorias) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CATEGORIA A BUSCAR: ")
    i = 0
    encontrado = False
    while i < len(list_categorias) :#-1
      if buscar == list_categorias[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      print("::: LA CATEGORIA FUE ENCONTRADA EN LA LISTA")
    else :
      print("::: LA CATEGORIA NO FUE ENCONTRADA EN LA LISTA")
          
  key = input("Presione cualquier tecla para volver al menú")
  categorias()

def modificar_categoria():
  os.system('cls')
  print("::: MODIFICACIÓN DE CATEGORIA ::: ")
  if len(list_categorias) == 0 :
    print("::: LA LISTA ESTÁ VACÍA :::")
  else :
    buscar = input("DIGITE CATEGORIA A MODIFICAR: ")
    i = 0
    encontrado = False
    while i < len(list_categorias) :#-1
      if buscar == list_categorias[i] :
        encontrado = True
      i += 1

    if encontrado == True :
      #Categorias.remove = Categorias[i]
      modificar = input(" DIGITE NUEVA CATEGORIA")
      list_categorias.insert(len(list_categorias),modificar)
    else :
      print("::: LA CATEGORIA NO FUE ENCONTRADA EN LA LISTA")
  key = input("Presione cualquier tecla para volver al menú")
  categorias()

def eliminar_categoria():
	os.system('cls')
	print("::::::: ELIMINAR CATEGORIA :::::::")
	elim = input("DIGITE CATEGORIA A ELIMINAR")
	list_categorias.remove(elim)
	key = input("	Persione cualquier tecla para volver al menu")
	categorias()

def salir ():
    print("Hasta Luego, vuelve pronto, eres importante, cuidate")
    sys.exit()