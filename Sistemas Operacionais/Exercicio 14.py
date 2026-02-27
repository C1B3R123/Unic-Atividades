# Exercício 14: Alerta de disco
import psutil

limite_livre = float(input("Mostrar partições com espaço livre menor que qual %? (Ex: 10) ") or 10)

print("\n--- Analisando partições críticas ---")
encontrou_critica = False

for part in psutil.disk_partitions(all=False):
    try:
        uso = psutil.disk_usage(part.mountpoint)
        perc_livre = 100 - uso.percent
        
        if perc_livre < limite_livre:
            print(f"⚠️ ALERTA: Partição {part.mountpoint} possui apenas {perc_livre:.1f}% de espaço livre!")
            encontrou_critica = True
    except PermissionError:
        continue

if not encontrou_critica:
    print("Nenhuma partição está em estado crítico baseada no seu limite.")