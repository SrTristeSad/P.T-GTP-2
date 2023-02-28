import os
import re
from tqdm import tqdm

# Define a pasta com as histórias originais
input_folder = 'entrada_txt'

# Define a pasta para salvar as histórias pré-processadas
output_folder = 'saida_pre_process'

# Define a expressão regular para remover URLs e links
url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# Define um dicionário de abreviações e suas expansões
abbreviations = {
    'não': 'não',
    'você': 'você',
    # Adicione mais abreviações e expansões aqui
}

# Percorre cada arquivo na pasta de entrada
for i, filename in tqdm(enumerate(os.listdir(input_folder)), desc='Processando textos', unit='arquivo'):
    # Gera um nome de arquivo sequencial para o arquivo de saída
    output_filename = '{:02d}.txt'.format(i+1)
    
    # Lê o conteúdo do arquivo original
    with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove URLs e links
    text = url_pattern.sub('', text)
    
    # Remove quebras de linha e outros caracteres especiais
    text = text.replace('\n', ' ').replace('\r', '').replace('\t', ' ')
    text = ''.join(c for c in text if c.isprintable())
    
    # Expande abreviações e contrações
    words = text.split()
    words = [abbreviations.get(word.lower(), word) for word in words]
    text = ' '.join(words)
    
    # Normaliza o texto
    text = text.lower()
    text = re.sub(r'([^\w\s])', r' \1 ', text)
    text = re.sub(r'\s+', ' ', text)
    
    # Divide o texto em frases e parágrafos
    sentences = re.split(r'[.!?]', text)
    paragraphs = []
    current_paragraph = ''
    for sentence in sentences:
        if len(current_paragraph) + len(sentence) + 1 > 500:
            paragraphs.append(current_paragraph.strip())
            current_paragraph = ''
        current_paragraph += sentence + ' '
    if current_paragraph.strip():
        paragraphs.append(current_paragraph.strip())
    
    # Salva o texto pré-processado em um novo arquivo
    with open(os.path.join(output_folder, output_filename), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(paragraphs))

