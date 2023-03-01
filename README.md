## fiz teste na instalação só não testei novamente após criar o instalador não lembro se coloque todas as Biblioteca no instalado para funcionar 100%, mas vou fazer teste, para verificar se o instalador está perfeito.
## e também pensando por uma função para pega dados através da nuvem para não precisa acessar SFTP para enviar texto.
O instalador pode falha na instalação só executar novamente o commando assim finalizar a instalação.


A recomendação de usar o Ubuntu 20 para instalar o P.T-GTP-2 e o comando `curl -s https://raw.githubusercontent.com/SrTristeSad/P.T-GTP-2/main/install.sh | bash` é uma opção conveniente e fácil para usuários que desejam instalar todas as dependências automaticamente.

O script P.T-GTP-2 é uma combinação de Shell e Python3 que tem como objetivo realizar o pré-processamento de texto para iniciar o treinamento do modelo de inteligência artificial GTP-2 (Generative Pretrained Transformer 2). O pré-processamento é uma etapa fundamental no treinamento de modelos de linguagem, pois ajuda a preparar os dados para que o modelo possa aprender de forma mais eficiente.

O script possui um menu de opções que permite ao usuário escolher entre três ações: pré-processamento de texto, tokenização de texto e exclusão de arquivos. Ao selecionar a opção de pré-processamento de texto, o script executa o arquivo commando1.py, que realiza a remoção de caracteres especiais e a conversão de letras maiúsculas para minúsculas. Já a opção de tokenização de texto executa o arquivo commando2.py, que utiliza o pacote nltk para realizar a tokenização do texto, removendo palavras irrelevantes como preposições e artigos.

Por fim, a opção de exclusão de arquivos remove todos os arquivos presentes nas pastas de entrada e saída do script. Isso pode ser útil quando se deseja reiniciar o processo de pré-processamento e treinamento do modelo a partir do zero.

Em resumo, o P.T-GTP-2 é um script útil para quem deseja treinar o modelo de linguagem GTP-2 com seus próprios dados de treinamento e precisa realizar o pré-processamento e tokenização desses dados. Ele ajuda a automatizar essas etapas, tornando o processo de treinamento mais eficiente e menos suscetível a erros.
