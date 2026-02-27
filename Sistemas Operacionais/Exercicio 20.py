# Exercício 20: Painel Integrado (Dashboard)
import psutil
import time
import os

# Determina a partição principal baseado no SO
particao_principal = 'C:\\' if os.name == 'nt' else '/'

try:
    net_old = psutil.net_io_counters()
    
    while True:
        # Pega métricas
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        
        try:
            disco = psutil.disk_usage(particao_principal)
            disco_livre_gb = disco.free / (1024**3)
        except:
            disco_livre_gb = 0.0

        net_new = psutil.net_io_counters()
        down_kbps = (net_new.bytes_recv - net_old.bytes_recv) / 1024
        up_kbps = (net_new.bytes_sent - net_old.bytes_sent) / 1024
        net_old = net_new
        
        # Limpa o terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Imprime o dashboard
        print("="*45)
        print("PAINEL DE MONITORAMENTO DO SISTEMA (Ctrl+C para sair)")
        print("="*45)
        print(f"CPU: Uso Total: {cpu}%")
        print(f"RAM: {ram.percent}% Usado | {ram.used / (1024**2):.0f} MB")
        print(f"DISCO ({particao_principal}): {disco_livre_gb:.1f} GB Livres")
        print(f"REDE: ↓ {down_kbps:.1f} kB/s | ↑ {up_kbps:.1f} kB/s")
        print("="*45)
        
        time.sleep(1) # O total de pausa é 2s (1s do sleep + 1s do intervalo da CPU)
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Painel encerrado com sucesso.")