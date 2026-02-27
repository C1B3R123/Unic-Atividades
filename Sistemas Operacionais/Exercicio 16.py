# Exercício 16: Monitor de CPU
import psutil
import time

try:
    print("Iniciando monitor de CPU...")
    while True:
        cpu_total = psutil.cpu_percent(interval=1)
        cpu_nucleos = psutil.cpu_percent(interval=None, percpu=True)
        
        print(f"\nCPU Total: {cpu_total}%")
        nucleos_str = " | ".join([f"Núcleo {i}: {uso}%" for i, uso in enumerate(cpu_nucleos)])
        print(nucleos_str)
        
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")