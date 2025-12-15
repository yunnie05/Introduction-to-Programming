#cria dois dicionários
#um que mapeia para as traduções atuais
#outro que providencia uma tradução para a lingua pedida
#o value de f é chave de g
def compose(f, g):
    new= {}
    for (key, value) in f.items():
        if value in g:
          new[key]= g[value]
    return new