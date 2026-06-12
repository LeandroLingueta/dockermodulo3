import os
import time


print("Aplicação iniciada!")

db_name = os.getenv("POSTGRES_DB")

while True:
    print(f"Conectado ao banco: meubanco")
    time.sleep(10)