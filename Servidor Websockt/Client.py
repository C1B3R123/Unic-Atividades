import asyncio
import websockets

async def receber_mensagens(websocket):
    try:
        async for mensagem in websocket:
            # O \r empurra a mensagem nova para o começo, não estragando o que você está digitando
            print(f"\r{mensagem}")
            print("Responder: ", end="", flush=True)
    except websockets.exceptions.ConnectionClosed:
        print("\n[Aviso] Conexão com o servidor foi encerrada.")

async def enviar_mensagens(websocket):
    while True:
        mensagem = await asyncio.to_thread(input, "Responder: ")
        
        if not mensagem.strip():
            continue
            
        if mensagem.lower() == 'sair':
            print("Saindo do chat...")
            break
            
        await websocket.send(mensagem)

async def main():
    ip_servidor = input("Digite o IP do servidor (ou aperte Enter para jogar sozinho): ")
    if not ip_servidor.strip():
        ip_servidor = "localhost"
        
    uri = f"ws://{ip_servidor}:6969"
    print(f"Tentando conectar ao servidor {uri}...")
    
    try:
        async with websockets.connect(uri) as websocket:
            print("Conectado com sucesso!\n")
            
            # --- SISTEMA DE LOGIN VERIFICADO ---
            while True:
                nome = ""
                while not nome.strip():
                    nome = await asyncio.to_thread(input, "Digite seu nome para entrar no chat: ")
                
                await websocket.send(nome)
                
                # Fica esperando a resposta oficial do Servidor
                resposta = await websocket.recv()
                
                if "[Erro]" in resposta:
                    print(resposta) # Mostra o erro e o loop pede o nome de novo
                elif resposta == "[OK]":
                    break # Nome aprovado! Quebra o loop e vai pro chat
            
            # --- SÓ INICIA O CHAT SE O NOME FOI APROVADO ---
            tarefa_receber = asyncio.create_task(receber_mensagens(websocket))
            tarefa_enviar = asyncio.create_task(enviar_mensagens(websocket))
            
            done, pending = await asyncio.wait(
                [tarefa_receber, tarefa_enviar],
                return_when=asyncio.FIRST_COMPLETED
            )
            for task in pending:
                task.cancel()
                
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar. O Servidor está rodando ou o IP está errado?")

if __name__ == "__main__":
    asyncio.run(main())