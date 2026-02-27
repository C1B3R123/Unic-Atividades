# Exercício 13: Gerenciador de espaço em disco
import psutil

print(f"{'Partição':<15} | {'Total (GB)':<12} | {'Usado (GB)':<12} | {'Livre (GB)':<12} | {'Uso (%)'}")
print("-" * 70)

for part in psutil.disk_partitions(all=False):
    try:
        uso = psutil.disk_usage(part.mountpoint)
        total_gb = uso.total / (1024 ** 3)
        usado_gb = uso.used / (1024 ** 3)
        livre_gb = uso.free / (1024 ** 3)
        
        print(f"{part.mountpoint:<15} | {total_gb:<12.2f} | {usado_gb:<12.2f} | {livre_gb:<12.2f} | {uso.percent}%")
    except PermissionError:
        # Pula partições sem permissão (como CD-ROM vazios no Windows)
        continue