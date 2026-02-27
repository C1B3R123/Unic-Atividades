# Exercício 19: Dispositivos E/S (Armazenamento)
import psutil

particoes = psutil.disk_partitions()

print("Dispositivos de Armazenamento Detectados (E/S):\n")
for i, part in enumerate(particoes):
    print(f"{i}. {part.device} (Montado em: {part.mountpoint} | Sistema: {part.fstype})")

escolha = int(input("\nEscolha o número do dispositivo para ver detalhes: "))

if 0 <= escolha < len(particoes):
    part_escolhida = particoes[escolha]
    try:
        uso = psutil.disk_usage(part_escolhida.mountpoint)
        print(f"\nDetalhes de {part_escolhida.device}:")
        print(f"Espaço Total: {uso.total / (1024**3):.2f} GB")
        print(f"Espaço Livre: {uso.free / (1024**3):.2f} GB")
        print(f"Em Uso: {uso.percent}%")
    except PermissionError:
        print("Sem permissão para ler detalhes deste dispositivo (provavelmente protegido ou vazio).")
else:
    print("Opção inválida.")