from flask import Flask, request, jsonify

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 