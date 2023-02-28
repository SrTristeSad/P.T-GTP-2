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
git clone https://github.com/seu-usuario/seu-repositorio.git

# Criar as pastas pré-definidas
mkdir -p seu-repositorio/entrada_txt
mkdir -p seu-repositorio/saida_pre_process
mkdir -p seu-repositorio/saida_tokenizador

# Entrar no diretório do painel
cd seu-repositorio

# Dar permissão de execução para o painel
chmod +x panel.sh

# Adicionar o painel ao .bashrc
echo "source $(pwd)/panel.sh" >> ~/.bashrc

# Exibir mensagem de conclusão
echo "Instalação concluída!"

