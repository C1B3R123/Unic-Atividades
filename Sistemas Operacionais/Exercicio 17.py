# Exercício 17: Logger de CPU
import psutil
import time
from datetime import datetime

ARQUIVO_LOG = "cpu_log.txt"
print(f"Registrando CPU a cada 5 segundos no arquivo '{ARQUIVO_LOG}'...")

try:
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as file:
        while True:
            agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cpu = psutil.cpu_percent(interval=1)
            
            linha = f"{agora} - CPU: {cpu}%\n"
            file.write(linha)
            file.flush() # Força a escrita no disco
            
            print(f"Registrado: {linha.strip()}")
            time.sleep(4) # Espera 4s (o interval=1 da cpu já gasta 1s)
except KeyboardInterrupt:
    print("\nLogging encerrado.")