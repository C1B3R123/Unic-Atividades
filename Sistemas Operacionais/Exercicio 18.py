# Exercício 18: Informações do Processador
import psutil
import platform
import subprocess

print("--- Informações da CPU ---")
print(f"Processador (Modelo): {platform.processor() or 'Desconhecido'}")
print(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
print(f"Núcleos Lógicos (Threads): {psutil.cpu_count(logical=True)}")

freq = psutil.cpu_freq()
if freq:
    print(f"Frequência Atual: {freq.current:.2f} MHz (Max: {freq.max:.2f} MHz)")

# Tentativa de obter o número de série (Dependente do SO)
print("\nTentando obter o número de série do hardware...")
try:
    if platform.system() == "Windows":
        output = subprocess.check_output("wmic cpu get processorid", shell=True).decode()
        serial = output.strip().split("\n")[1].strip()
        print(f"ID do Processador: {serial}")
    elif platform.system() == "Linux":
        # Extração comum no Raspberry Pi, CPUs convencionais x86 não expõem serial fácil no Linux
        output = subprocess.check_output("cat /proc/cpuinfo | grep Serial", shell=True).decode()
        print(f"Serial: {output.split(':')[1].strip()}")
    else:
         print("Recurso não suportado para o seu SO atual neste script.")
except Exception:
    print("Não foi possível obter o número de série. Isso ocorre pois a restrição varia entre hardware e o nível de privilégio do SO.")