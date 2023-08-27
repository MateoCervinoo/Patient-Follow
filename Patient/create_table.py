import sqlite3
import pandas as pd

conn = sqlite3.connect("Patients.db")

query = '''
    CREATE TABLE "Patients" ("PatientNumber" INTEGER, "Name" TEXT, "PhoneNumber" INTEGER, "OperationDate" TEXT,
    "Hospital" TEXT, "Medicare" TEXT,
    PRIMARY KEY ("PatientNumber")
)
'''

pd.read_sql_query(query, conn)

print("Tabla creada exitosamente\n")