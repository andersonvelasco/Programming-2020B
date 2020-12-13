import time
import os
import sys
import getpass

categorias_list = []
proveedores_list = []
productos_list = []
Clientes_list = []
name_list = ["Anderson"]
last_name_list = ["Velasco"]
telephone_list = ["3104011389"]
email_list = ["anderson.velasco.21@hotmail.com"]
nickname_list = ["andersonvelasco"]
password_list = ["123"]
status_list = ["Activo"]
#Functions

def menu_login():
  os.system("cls")
  '''Muestra el menú Login'''
  print(":::: Menú login ::::")
  print("[1.] Iniciar sesión")
  print("[2.] Crear cuenta de Usuario")
  print("[3.] Salir")
  op = input(".:: Digite una opción: ")

  if op == '1' :
    init_sesion()
  elif op == '2' :
    register_us()
  else :
    print("::: Vuelve pronto :::")

'''Menú Principal'''

def menu_principal(usuario):
    os.system("cls")
    print("\n:::: Menú principal ::::\n")
    print("[1.] Categorias")
    print("[2.] Proveedores")
    print("[3.] Productos")
    print("[4.] Clientes")
    print("[5.] Reportes")
    print("[6.] Salir")
    op = input(".:: Digite una opción: ")
    
    if op == '1' :
        print("Categorias")
        
    elif op == '2' :
        print("Proveedores")
    elif op == '3' :
        print("Productos")
    elif op == '4' :
        print("clientes")
    elif op == '5' :
        print("reportes")
    else :
        print("::: Vuelve pronto :::")

def validate_user(usuario,passw):
    if usuario in nickname_list:
        if passw in password_list:
            return 1
        else:
            print("\n\t Password incorrecta")
    else:
        return 2

def init_sesion():
    print("::: Inicio de Sesión ::: ")
    init_nickname = input("Digite nickname: ")
    init_pass = getpass.getpass("Password: ")
    if validate_user(init_nickname,init_pass)==1:
        print("Bienvenido\n Sesión Iniciada con el Usuario : ", init_nickname)
        menu_principal(init_nickname)
    else:
        print("ERROR! Revisa los datos ingresados")
    init_sesion()

def register_us():
    os.system("cls")
    print("::: Formulario de Registro ::: ")
    name_user = input("Digite Nombres: ")
    name_list.append(name_user)
    last_name_user = input("Digite Apellidos: ")
    last_name_list.append(last_name_user)
    telephone_user = input("Digite No. Telefono: ")
    telephone_list.append(telephone_user)
    email_user = input("Digite Correo Electronico: ")
    email_list.append(email_user)
    nickname = input("Digite nickname: ")
    nickname_list.append(nickname)
    password_user = getpass.getpass(input("Digite Contraseña: "))
    password_list.append(password_user)
    key = input("Los datos han sido almacenados. Presione cualquier tecla para volver al menú")
    menu_login()
