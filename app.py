# No terminal:
# 1) Criamos um ambiente virtual com o comando:
#Python -m venv .venv
# 2) Ativamos o ambiente virtual com o comando:
# .\.ven\Scripts\activate
# 3) Instalamos o flask com o comando:
# PIP install flask
# Caso o seu ambiente virtual não seja ativado é preciso pesquisar
# Internet como liberar a execução
# Dele no powershell e voltar a ativar o ambiente depois

from flask import Flask, jsonify,make_response,request
from bd_livros import livros # aqui eu estou importando a lista de livros criado (Banco de dados)

#BIBLIOTECAS
# jsonify = Trasforma lista, dicionários etc em arquivos json. só funciona com status code 200, ou seja
# Quando a requisição é bem sucedida
# Make_Response = Transforma os json em métodos HTTP e permite que estilizamos nossa resposta
# E trata os erros
# Request = faz as requisições

app = Flask(__name__) # Instanciando o flask, ou seja, estou tornando o molde num objeto
app.config['JSON_SORT_KEYS']= False

# GET  - listar todos os livros do nosso "Banco de dados"
@app.route('/livros', methods=['GET'])
def get_Livros():
    return make_response(jsonify( 
        mensagem= 'Lista de livros cadastrados',
        dados = livros
    ),200)
    
# GET - Buscar apenas um livro pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    for livro in livros: # Precorrer a lista de livros
        if livro.get('id') == id:
            return make_response(jsonify( 
                mensagem=f'livro de ID {id} encontrado',
                dados = livro
       
            ),200)
    return make_response(jsonify(mensagem='livro não encontrado'),404)

# POST - Adicionar um novo livro
@app.route('/livros', methods=['POST'])
def create_livro():
    novo_livro = request.json
    livros.append(novo_livro)
    return make_response(jsonify(
        mensagem='Novo livro adicionado com sucesso',
        dados = novo_livro
    ),201)

# PUT - atualizr livro por completo
@app.route('/livros/<int:id>',methods=['PUT'])
def update_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            novo_dados = request.json
            livro.update(novo_dados) # Substitui todos os dados
            return make_response(jsonify(
                mensagem=f'livro ID {id} atualizado com sucesso (PUT)'
            ),200)
        return make_response(jsonify(mensagem='livro não encontrado'),404)

# PATCH - Atualizar parcialmente um livro
@app.route('/livros/<int:id>', methods=['PATCH'])
def patch_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            dados = request.json
            livro.update(dados) # Só altera os campos enviados
            return make_response(jsonify(
                mensagem=f'livro ID {id} atualizado parcialmente (PATCH).',
                dados = livro
            ),200)
        return make_response(jsonify(mensagem='livro não encontrado'),404)

#DELETE - remover um livro
@app.route('/livros/<int:id>',methods=['DELETE'])
def delete_livro(id):
    for livro in livros:
        if livros.get('id')== id:
            livros.remove(livro)
            return make_response(jsonify(
                mensagem=f'livro ID {id} foi removido com sucessso.'
            ),200)
    return make_response(jsonify(mensagem='livro não encontrado.'),404)
    
if __name__ == '__main__': # Esse comando permite que API seja executada de maneira independente em outros arquivos
    app.run(debug=True)
   