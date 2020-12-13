import sys
import os
os.system("cls")

def menu_categorias(categorias_list):
    print("\n:::: Menú Categorias ::::\n")
    print("[1.] Ingresar nueva categoria categoria")
    print("[2.] Listar categorias")
    print("[3.] Buscar categorias")
    print("[4.] Eliminar Categoria")
    print("[5.] Modificar categoria")
    print("[6.] volver al menú Principal")
    op = input(".:: Digite una opción: ")
    
    if op == '1' :
        ingresar_categoria()
    elif op == '2' :
        listar_categorias()
    elif op == '3' :
        buscar_categoria()
    elif op == '4' :
        eliminar_categoria()
    elif op == '5' :
        modificar_categoria()
    elif op == '6' :
        menu_principal()
    else :
        print("::: Vuelve pronto :::")



def ingresar_categoria():
    '''Registra una nueva categoria'''
    categoria_list.append(categoria)

def listar_categorias():
    '''Listar una categoria'''
    print("listar categorias")

def buscar_categoria():
    '''Buscar una categoria'''
    print("Buscar categoria")

def eliminar_categoria():
    '''Eliminar una categoria'''
    print("Eliminar categoria")

def modificar_categoria():
    '''Modificar una categoria'''
    print("Modificar categoria")

#-----------------------------------------