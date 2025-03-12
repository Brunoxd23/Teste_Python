from flask import Flask, request, jsonify
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
import asyncio
import time
from datetime import datetime

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados e secret key
app.config['SECRET_KEY'] = 'chave-secreta-da-aplicacao'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo para registrar operações
class Operacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))  # 'saudacao', 'soma', 'async_test', 'sync_test'
    entrada = db.Column(db.String(200))  # Dados de entrada em formato string
    resultado = db.Column(db.String(200))  # Resultado em formato string
    tempo_execucao = db.Column(db.Float)  # Tempo de execução em segundos
    data = db.Column(db.DateTime, default=datetime.utcnow)

# Configuração do Admin
admin = Admin(app, name='Painel de Controle', template_mode='bootstrap3')
from flask_admin.contrib.sqla import ModelView
admin.add_view(ModelView(Operacao, db.session))

# Endpoint GET para saudação
@app.route('/saudacao', methods=['GET'])
def saudacao():
    inicio = time.time()
    nome = request.args.get('nome', 'Visitante')
    mensagem = f'Olá, {nome}! Bem-vindo(a) ao teste da API Flask!'
    
    # Registra a operação
    operacao = Operacao(
        tipo='saudacao',
        entrada=f'nome={nome}',
        resultado=mensagem,
        tempo_execucao=time.time() - inicio
    )
    db.session.add(operacao)
    db.session.commit()
    
    return jsonify({'mensagem': mensagem})

# Endpoint POST para soma
@app.route('/soma', methods=['POST'])
def soma():
    inicio = time.time()
    try:
        dados = request.get_json()
        numero1 = dados['numero1']
        numero2 = dados['numero2']
        resultado = numero1 + numero2
        
        # Registra a operação
        operacao = Operacao(
            tipo='soma',
            entrada=f'numero1={numero1}, numero2={numero2}',
            resultado=str(resultado),
            tempo_execucao=time.time() - inicio
        )
        db.session.add(operacao)
        db.session.commit()
        
        return jsonify({'resultado': resultado})
    except (KeyError, TypeError):
        erro = 'Por favor, envie dois números válidos no formato JSON'
        # Registra o erro
        operacao = Operacao(
            tipo='soma_erro',
            entrada=str(request.get_json()),
            resultado=erro,
            tempo_execucao=time.time() - inicio
        )
        db.session.add(operacao)
        db.session.commit()
        return jsonify({'erro': erro}), 400

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
    
    # Registra a operação
    operacao = Operacao(
        tipo='async_test',
        entrada='chamadas_paralelas=3',
        resultado=str(resultados),
        tempo_execucao=tempo_total
    )
    db.session.add(operacao)
    await db.session.commit()
    
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
    
    # Registra a operação
    operacao = Operacao(
        tipo='sync_test',
        entrada='chamadas_sequenciais=3',
        resultado=str([resultado1, resultado2, resultado3]),
        tempo_execucao=tempo_total
    )
    db.session.add(operacao)
    await db.session.commit()
    
    return jsonify({
        "modo": "síncrono",
        "resultados": [resultado1, resultado2, resultado3],
        "tempo_total": tempo_total,
        "explicacao": "Chamadas executadas uma após a outra"
    })

# Criar o banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
