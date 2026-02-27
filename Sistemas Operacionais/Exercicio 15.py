# Exercício 15: Monitor de rede
import psutil
import time

try:
    print("Monitorando rede... (Pressione Ctrl+C para sair)")
    net_old = psutil.net_io_counters()
    
    while True:
        time.sleep(1)
        net_new = psutil.net_io_counters()
        
        # Calcula a diferença em bytes e converte para KB
        bytes_recv = (net_new.bytes_recv - net_old.bytes_recv) / 1024
        bytes_sent = (net_new.bytes_sent - net_old.bytes_sent) / 1024
        
        print(f"Download: {bytes_recv:.2f} kB/s | Upload: {bytes_sent:.2f} kB/s")
        
        # Atualiza a referência para a próxima iteração
        net_old = net_new
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")