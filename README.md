# API Flask - Endpoints de Saudação e Soma

Este projeto é uma API simples desenvolvida com Flask que fornece dois endpoints para demonstração de operações básicas de GET e POST.

## Funcionalidades

### 1. Endpoint de Saudação (GET)
- **Rota**: `/saudacao`
- **Método**: GET
- **Parâmetro**: `nome` (opcional)
- **Exemplo de uso**: `/saudacao?nome=Maria`
- **Resposta**: Retorna uma mensagem de saudação personalizada em formato JSON  "mensagem": "Olá, Maria! Bem-vindo(a)! à API Flask"

### 2. Endpoint de Soma (POST)
- **Rota**: `/soma`
- **Método**: POST
- **Corpo da requisição**: JSON com dois números
- **Exemplo de corpo**: `{"numero1": 10, "numero2" 10: 20}`

## 📋 Requisitos

- Python 3.x
- Flask

## 🔧 Instalação e Configuração

### Configurando o Ambiente Virtual (venv)

é uma boa prática criar um ambiente virtual!

 1. Clone o repositório:

 git clone [https://github.com/Brunoxd23/Teste_Python.git]
 cd [Teste_Python]

 2. Crie o ambiente virtual:

```bash
Windows
python -m venv venv
Linux/Mac
python3 -m venv venv
```

3. Ative o ambiente virtual:

```bash
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
```
4. Instale as dependências:
pip install -r requirements.txt

5. Execute a aplicação:
python app.py


### ❗ Notas Importantes
- Sempre ative o ambiente virtual antes de executar o projeto
- Para desativar o ambiente virtual, use o comando `deactivate`
- Para atualizar as dependências: `pip freeze > requirements.txt`

## 🧪 Testando os Endpoints com Thunder Client

### Configurando o Thunder Client
1. Abra o VS Code
2. Instale a extensão "Thunder Client" na aba de extensões
3. Clique no ícone do Thunder Client na barra lateral esquerda (ícone de raio ⚡)

### Testando o Endpoint de Saudação (GET)
1. Clique em "New Request"
2. Configure a requisição:
   - Método: GET
   - URL: `http://localhost:5000/saudacao?nome=Maria`
3. Clique em "Send"
4. Resposta esperada:

{
"mensagem": "Olá, Maria! Bem-vindo(a)!"
}


### Testando o Endpoint de Soma (POST)
1. Clique em "New Request"
2. Configure a requisição:
   - Método: POST
   - URL: `http://localhost:5000/soma`
3. Na aba "Body":
   - Selecione "JSON"
   - Cole o seguinte conteúdo:

   {
"numero1": 10,
"numero2": 20
}

4. Clique em "Send"
5. Resposta esperada:


{
"resultado": 30
}

### 💡 Dicas para Testes no Thunder Client
- Verifique se o servidor Flask está rodando (`python app.py`)
- Certifique-se que a porta 5000 está livre
- Para testar diferentes cenários, você pode:
  - Alterar os números no body
  - Testar com números decimais
  - Testar com números negativos
  - Testar erros enviando dados inválidos

### Exemplos de Testes Realizados com Sucesso
1. Soma de números inteiros:

{
"numero1": 15,
"numero2": 25
}
// Resultado: {"resultado": 40}


2. Soma com decimais:

{
"numero1": 10.5,
"numero2": 20.5
}
// Resultado: {"resultado": 31.0}


. Soma com negativos:

{
"numero1": -10,
"numero2": 20
}
// Resultado: {"resultado": 10}
