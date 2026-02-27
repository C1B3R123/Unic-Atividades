#Exercicio 11: Monitor simples de RAM
import psutil
import time

try:
    while True:
        ram = psutil.virtual_memory()
        total_mb = ram.total / (1024 ** 2)
        usada_mb = ram.used / (1024 ** 2)
        livre_mb = ram.available / (1024 ** 2)
        
        print("\n--- Monitor de RAM ---")
        print(f"Total: {total_mb:.2f} MB")
        print(f"Em uso: {usada_mb:.2f} MB")
        print(f"Livre: {livre_mb:.2f} MB ({100 - ram.percent:.1f}%)")
        
        time.sleep(2)
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")