# Exercício 12: Monitor de RAM com alerta
import psutil
import time

limite = float(input("Defina o limite de alerta para a RAM (em %): "))

try:
    while True:
        ram = psutil.virtual_memory()
        
        print(f"Uso atual: {ram.percent}%")
        if ram.percent > limite:
            print(f"⚠️ ALERTA: O uso de RAM ({ram.percent}%) ultrapassou o limite de {limite}%!")
            
        time.sleep(2)
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")