#!/bin/bash

# Função para exibir o menu
show_menu() {
    clear
    echo -e "\e[1m##########################################################\e[0m"
    echo -e "\e[1m#                                                        #\e[0m"
    echo -e "\e[1m#                      MENU DE OPÇÕES                    #\e[0m"
    echo -e "\e[1m#                                                        #\e[0m"
    echo -e "\e[1m##########################################################\e[0m"
    echo -e "\e[1m#                                                        #\e[0m"
    echo -e "\e[1m#      \e[32m1. Pré-processo\e[0m                        #\e[0m"
    echo -e "\e[1m#      \e[32m2. Tokenização\e[0m                         #\e[0m"
    echo -e "\e[1m#      \e[32m3. Apagar arquivos\e[0m                     #\e[0m"
    echo -e "\e[1m#      \e[32m4. Sair\e[0m                                #\e[0m"
    echo -e "\e[1m#                                                        #\e[0m"
    echo -e "\e[1m##########################################################\e[0m"
}

# Loop do menu
while true; do
    show_menu

    # Ler a escolha do usuário
    read choice

    case $choice in
        1)
            echo -e "\e[1mExecutando pré-processamento...\e[0m"
            python3 ./commando1.py
            ;;
        2)
            echo -e "\e[1mExecutando tokenizador...\e[0m"
            python3 ./commando2.py
            ;;
        3)
            echo -e "\e[1mApagando arquivos...\e[0m"
            rm -rf ./entrada_txt/*
            rm -rf ./saida_pre_process/*
    

            ;;
        4)
            echo -e "\e[1mSaindo...\e[0m"
            exit 0
            ;;
        *)
            echo -e "\e[1mOpção inválida. Tente novamente.\e[0m"
            ;;
    esac

    echo -e "\e[1mPressione qualquer tecla para continuar...\e[0m"
    read -n 1
done

