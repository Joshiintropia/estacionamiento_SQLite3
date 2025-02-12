import sqlite3

try:
    conn = sqlite3.connect("./database/estacionamiento.sql3")
    print("Coneccion Establecida")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXIST ventas(
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    placa TEXT NOT NULL,
    hora_entrada TEXT NOT NULL,
    hora_salida TEXT,
    total_pago REAL NOT NULL
    )
    """)

except Exception as ex:
    print(ex)
