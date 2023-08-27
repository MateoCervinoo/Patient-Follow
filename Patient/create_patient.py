import sqlite3
import pandas as pd

conn = sqlite3.connect("Patients.db")
cursor = conn.cursor()

name = input('Ingrese el nombre y apellido del paciente: ')

phone_number = input('Ingrese el número de teléfono del paciente: ')
#Agregar validacion de que es una secuencia numerica

operation_date = input('Ingrese la fecha de la operación: ')

hospital = input('Ingrese el hospital donde se realizó la operación: ')

medicare = input('Ingrese el nombre de la obra social del paciente: ')

print("Registro del paciente exitoso\n")

cursor.execute('INSERT INTO Patients VALUES (1 ,?, ?, ?, ?, ?) ', (name, phone_number, operation_date, hospital, medicare))

conn.commit()

conn.close()