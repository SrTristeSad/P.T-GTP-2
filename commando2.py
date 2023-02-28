import os
import re
import nltk
from tqdm import tqdm

nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Define a pasta com as histórias pré-processadas
input_folder = 'saida_pre_process'

# Define a pasta para salvar as histórias processadas
output_folder = 'saida_tokenizador'

# Define a expressão regular para remover pontuações
punctuation_pattern = re.compile(r'[^\w\s]')

# Define a lista de arquivos na pasta de entrada
files = os.listdir(input_folder)

# Inicializa o progress bar
pbar = tqdm(total=len(files), desc='Processando textos', unit='arquivo')

# Percorre cada arquivo na pasta de entrada
for i, filename in enumerate(files):
    # Gera um nome de arquivo sequencial para o arquivo de saída
    output_filename = '{:02d}.txt'.format(i+1)

    # Lê o conteúdo do arquivo pré-processado
    with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove pontuações
    text = punctuation_pattern.sub('', text)

    # Tokeniza o texto
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('portuguese'))
    tokens = [token for token in tokens if token.lower() not in stop_words]

    # Salva o texto processado em um novo arquivo
    with open(os.path.join(output_folder, output_filename), 'w', encoding='utf-8') as f:
        f.write(' '.join(tokens))

    # Atualiza o progress bar
    pbar.update(1)

# Fecha o progress bar
pbar.close()
