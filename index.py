
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        
        
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        

class Biblioteca:
    def __init__(self):
        self.lista_disponiveis = []
        self.lista_emprestados = []
        
    def inserir_livros_disponiveis(self, livro):
        self.lista_disponiveis.append(livro)
        print(f'{livro.titulo} inserido com sucesso no acervo')
        
    def emprestar_livros(self, livro, pessoa):
        if livro in self.lista_disponiveis:
            self.lista_disponiveis.remove(livro)
            self.lista_emprestados.append(livro)
            print(f'{pessoa.nome} pegou emprestado o livro {livro.titulo}.')
        else:
            print("Livro não disponível para empréstimo.")
            
    def devolver_livros(self, livro):
        if livro in self.lista_emprestados:
            self.lista_emprestados.remove(livro)
            self.lista_disponiveis.append(livro)
            print(f'O livro {livro.titulo} foi devolvido.')
        else: 
            print("Este livro não pertence à nossa biblioteca.")
            
    def listar_livros_disponiveis(self):
        print('Livros disponíveis: ')
        for livro in self.lista_disponiveis:
             print(f'{livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')
            
        

livro1 = Livro('Harry Potter', 'John Textor', '231233-443')
livro2 = Livro('Joanaa Darc', 'Chico Xavier', '234564-4458')

pessoa1 = Pessoa('José')
pessoa2 = Pessoa('Alice')

biblioteca = Biblioteca()
biblioteca.inserir_livros_disponiveis(livro1)
biblioteca.inserir_livros_disponiveis(livro2)

biblioteca.emprestar_livros(livro1, pessoa1)
biblioteca.devolver_livros(livro1)

biblioteca.listar_livros_disponiveis()