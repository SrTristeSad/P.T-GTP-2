#!/bin/bash

# Instalar o Python3 e o pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Instalar as dependências necessárias
sudo pip3 install nltk
sudo pip3 install tqdm

# Download dos recursos adicionais do NLTK
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Clonar o repositório do seu painel
git clone https://github.com/SrTristeSad/P.T-GTP-2.git

# Criar as pastas pré-definidas
mkdir -p P.T-GTP-2/entrada_txt
mkdir -p P.T-GTP-2/saida_pre_process
mkdir -p P.T-GTP-2/saida_tokenizador

# Entrar no diretório do painel
cd P.T-GTP-2

# Dar permissão de execução para o painel
chmod +x pt-gtp2.sh

# Adicionar o painel ao .bashrc
echo "source $(pwd)/pt-gtp2.sh" >> ~/.bashrc

# Exibir mensagem de conclusão
echo "Instalação concluída!"

