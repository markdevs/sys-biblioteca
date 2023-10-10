### Exemplo de um sistema de gerenciamento de biblioteca
### Aqui está uma descrição básica de cada classe:

1.Livro:

- Atributos: Título, Autor, ISBN (um identificador único para cada livro)
- Métodos: __init__ (construtor) para inicializar os atributos.

2.Pessoa:

- Atributos: Nome
- Métodos: __init__ (construtor) para inicializar o atributo.

3.Biblioteca:

Atributos:
- Uma lista de livros disponíveis.
- Uma lista de livros emprestados.

Métodos:
- __init__ (construtor) para inicializar as listas.
- adicionar_livro(self, livro) para adicionar um livro à lista de livros disponíveis.
- emprestar_livro(self, livro, pessoa) para emprestar um livro a uma pessoa.
- devolver_livro(self, livro) para devolver um livro à biblioteca.
- listar_livros_disponiveis(self) para listar os livros disponíveis.

