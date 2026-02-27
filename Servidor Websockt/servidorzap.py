import asyncio
import websockets

# Dicionário para guardar as conexões e os nomes: {websocket: "Nome"}
conexoes = {}

async def chat_handler(websocket):
    nome = "Desconhecido"
    try:
        # A primeira mensagem que o cliente enviar será o seu nome
        nome = await websocket.recv()
        conexoes[websocket] = nome
        print(f"Novo usuário '{nome}' conectado. Total na sala: {len(conexoes)}")
        
        # Avisa para todos da sala que um novo usuário entrou
        mensagem_entrada = f"--- {nome} entrou no fórum! ---"
        for conexao in conexoes:
            if conexao != websocket:
                await conexao.send(mensagem_entrada)

        # Fica escutando as mensagens normais do cliente
        async for mensagem in websocket:
            print(f"Servidor repassando mensagem de {nome}: {mensagem}")
            
            # Repassa a mensagem para os OUTROS clientes
            for conexao in conexoes:
                if conexao != websocket:
                    await conexao.send(mensagem)
                    
    except websockets.exceptions.ConnectionClosed:
        pass # Tratado no bloco finally
    finally:
        # Quando o cliente sai, removemos ele da lista e avisamos os outros
        if websocket in conexoes:
            del conexoes[websocket]
            mensagem_saida = f"--- {nome} saiu do fórum. ---"
            
            print(f"{nome} desconectou. Restam: {len(conexoes)}")
            for conexao in conexoes:
                await conexao.send(mensagem_saida)

async def main():
    print("Servidor do Fórum iniciado! Aguardando usuários na porta 6969...")
    async with websockets.serve(chat_handler, "localhost", 6969):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())