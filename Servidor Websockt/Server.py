import asyncio
import websockets
import time

conexoes = {}
historico_mensagens = []

def limpar_historico_antigo():
    tempo_atual = time.time()
    historico_limpo = [msg for msg in historico_mensagens if (tempo_atual - msg[0]) <= 300]
    historico_mensagens[:] = historico_limpo

async def chat_handler(websocket):
    nome = "Desconhecido"
    try:
        # --- SISTEMA DE LOGIN VERIFICADO ---
        while True:
            nome = await websocket.recv()
            nomes_ativos = [n.lower() for n in conexoes.values()]
            
            if nome.lower() in nomes_ativos:
                await websocket.send("\n[Erro] Esse nome já está em uso! Tente outro.")
            else:
                await websocket.send("[OK]") # Manda a autorização para o Cliente!
                break
        
        conexoes[websocket] = nome
        print(f"Novo usuário '{nome}' conectado. Total na sala: {len(conexoes)}")

        limpar_historico_antigo()
        
        if historico_mensagens:
            await websocket.send("\n--- Histórico de Mensagens (Últimos 5 min) ---")
            for timestamp, msg_antiga in historico_mensagens:
                await websocket.send(msg_antiga)
            await websocket.send("----------------------------------------------\n")

        hora_atual = time.strftime("[%H:%M]")
        mensagem_entrada = f"{hora_atual} --- {nome} entrou no fórum! ---"
        historico_mensagens.append((time.time(), mensagem_entrada))
        
        for conexao in conexoes:
            if conexao != websocket:
                await conexao.send(mensagem_entrada)

        async for mensagem in websocket:
            if not mensagem.strip():
                continue

            hora_atual = time.strftime("[%H:%M]")
            mensagem_formatada = f"{hora_atual} {nome}: {mensagem}"
            
            print(f"Servidor repassando: {mensagem_formatada}")

            historico_mensagens.append((time.time(), mensagem_formatada))
            limpar_historico_antigo() 

            for conexao in conexoes:
                if conexao != websocket:
                    await conexao.send(mensagem_formatada)

    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        if websocket in conexoes:
            del conexoes[websocket]
            hora_atual = time.strftime("[%H:%M]")
            mensagem_saida = f"{hora_atual} --- {nome} saiu do fórum. ---"
            historico_mensagens.append((time.time(), mensagem_saida))
            
            print(f"{nome} desconectou. Restam: {len(conexoes)}")
            for conexao in conexoes:
                await conexao.send(mensagem_saida)

async def main():
    print("Servidor do Fórum iniciado! Aguardando usuários na porta 6969...")
    async with websockets.serve(chat_handler, "0.0.0.0", 6969):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())