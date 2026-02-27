import asyncio
import websockets

# Conjunto para guardar todos os clientes conectados
conexoes = set()

async def chat_handler(websocket):
    # Quando um cliente conecta, adicionamos ele ao conjunto
    user = input("Digite seu nome: ")
    conexoes.add(websocket)
    print(f"Novo usuário chamado {user} conectado. Total na sala: {len(conexoes)}")

    try:
        # Fica escutando as mensagens desse cliente
        async for mensagem in websocket:
            print(f"Servidor repassando: {mensagem}")
            
            # Envia a mensagem para todos os OUTROS clientes
            for conexao in conexoes:
                if conexao != websocket:
                    await conexao.send(mensagem)
                    
    except websockets.exceptions.ConnectionClosed:
        print("Um cliente perdeu a conexão.")
    finally:
        # Garante que o cliente seja removido ao sair
        conexoes.remove(websocket)
        print(f"Cliente desconectado. Restam: {len(conexoes)}")

async def main():
    print("Servidor de chat iniciado! Aguardando conexões na porta 6969...")
    # Inicia o servidor na porta 6969
    async with websockets.serve(chat_handler, "localhost", 6969):
        await asyncio.Future()  # Mantém o servidor rodando para sempre

if __name__ == "__main__":
    asyncio.run(main())