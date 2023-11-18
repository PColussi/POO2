class Material:
    def __init__(self, titulo, autor_ou_editora) -> None:
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora
        pass

    def exibir_informacoes(self):
        return f"Título: {self.titulo}\nAutor/Editora: {self.autor_ou_editora}"
    


class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
    
    def exibir_informacoes(self):
         super().exibir_informacoes()
         print(f"Genêro: {self.genero}")
        

class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao) -> None:
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    
    def exibir_informacoes(self):
         super().exibir_informacoes()
         print(f"Edição: {self.edicao}")
        


livro = Livro("Aprendendo Python", "John Doe", "Programação")
revista = Revista("Revista de Ciência", "Editora ABC", "Edição de Janeiro")

print("Detalhes do Livro:")
livro.exibir_informacoes()
print("\nDetalhes da Revista:")
revista.exibir_informacoes()
