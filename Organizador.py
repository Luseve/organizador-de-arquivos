import os
import shutil

# Caminho da pasta que você quer organizar
pasta_alvo = 'C:/Users/SeuUsuario/Downloads'  # 🔁 Substitua aqui

# Tipos de arquivos e pastas destino
tipos_arquivos = {
    'imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'videos': ['.mp4', '.mov'],
    'compactados': ['.zip', '.rar'],
    'outros': []
}

# Criar as pastas se não existirem
for categoria in tipos_arquivos:
    caminho = os.path.join(pasta_alvo, categoria)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

# Organizar os arquivos
for arquivo in os.listdir(pasta_alvo):
    caminho_arquivo = os.path.join(pasta_alvo, arquivo)
    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)
        movido = False
        for categoria, extensoes in tipos_arquivos.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(pasta_alvo, categoria, arquivo)
                shutil.move(caminho_arquivo, destino)
                movido = True
                break
        if not movido:
            destino = os.path.join(pasta_alvo, 'outros', arquivo)
            shutil.move(caminho_arquivo, destino)

print("Organização concluída!")
