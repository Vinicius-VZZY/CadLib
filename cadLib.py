from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Livro1',
        'autor': 'Autor1'
    },
    {
        'id': 2, 'titulo':
        'Livro2',
        'autor': 'Autor2'
    },
    {
        'id': 3,
        'titulo': 'Livro3',
        'autor': 'Autor3'
    }
]

@app.route('/livros', methods=['GET'])
def consultar_livros():
    return jsonify(livros)

@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro_por_id(id):
    livro_atualizado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_atualizado)
            return jsonify(livros[indice])

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)

app.run(host='localhost', port=8080, debug=True)