# remove o fundo de imagem.17º projeto.linguagem utilizada Python

# criado por: Leonardo de Oliveira Prado
# Instagram: arduino2.0tecnologico

# Data de inicio do projeto 18/12/2023
# Data de término do projeto 18/12/2023
from rembg import remove
from PIL import Image


caminho_entrada_imagem = "imagem.jpg"#onde esta a imagem
caminho_saida_imagem="imagem_SemFundo.png"#onde vai salvar a imagem

imagem =Image.open(caminho_entrada_imagem)

remove_imagem = remove(imagem)#remove o fondo

remove_imagem.save(caminho_saida_imagem)#salva a imagem