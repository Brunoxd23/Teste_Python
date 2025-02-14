from flask import Flask, request, jsonify
import asyncio
import time

# Inicializa a aplicação Flask
app = Flask(__name__)

# Endpoint GET para saudação
@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Visitante')
    return jsonify({'mensagem': f'Olá, {nome}! Bem-vindo(a) ao teste da API Flask!'})

# Endpoint POST para soma
@app.route('/soma', methods=['POST'])
def soma():
    try:
        dados = request.get_json()
        numero1 = dados['numero1']
        numero2 = dados['numero2']
        resultado = numero1 + numero2
        return jsonify({'resultado': resultado})
    except (KeyError, TypeError):
        return jsonify({'erro': 'Por favor, envie dois números válidos no formato JSON'}), 400

# Simulação de chamada de rede
async def chamada_rede(delay):
    await asyncio.sleep(delay)
    return f"Resultado após {delay}s"

# Execução ASSÍNCRONA - todas as chamadas em paralelo
@app.route('/async-test', methods=['GET'])
async def teste_async():
    inicio = time.time()
    
    # Executa 3 chamadas em paralelo
    resultados = await asyncio.gather(
        chamada_rede(1),
        chamada_rede(2),
        chamada_rede(3)
    )
    
    tempo_total = time.time() - inicio
    
    return jsonify({
        "modo": "assíncrono",
        "resultados": resultados,
        "tempo_total": tempo_total,
        "explicacao": "Todas as chamadas executadas em paralelo"
    })

# Execução SÍNCRONA - uma chamada após a outra
@app.route('/sync-test', methods=['GET'])
async def teste_sync():
    inicio = time.time()
    
    # Executa 3 chamadas sequencialmente
    resultado1 = await chamada_rede(1)
    resultado2 = await chamada_rede(2)
    resultado3 = await chamada_rede(3)
    
    tempo_total = time.time() - inicio
    
    return jsonify({
        "modo": "síncrono",
        "resultados": [resultado1, resultado2, resultado3],
        "tempo_total": tempo_total,
        "explicacao": "Chamadas executadas uma após a outra"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 