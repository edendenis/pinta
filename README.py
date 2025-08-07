#!/usr/bin/env python
# coding: utf-8

# # Como instalar o `catfish` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Este documento apresenta os passos necessários para instalar o utilitário `catfish` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document shows the steps required to install the `catfish` utility on `Linux Ubuntu`._
# 
# ## Descrição [2]
# 
# ### `catfish`
# 
# O `catfish` é uma ferramenta de busca para ambientes `Linux`. Ela combina utilitários como `locate` e `find` para localizar arquivos e pastas rapidamente por meio de uma interface simples.
# 
# 
# 
# ## 1. Instalar o `catfish` no `Linux Ubuntu`
# 
# Para instalar o `catfish`, siga os passos abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt full-upgrade -y
#     ```
# 
# 3. Instale o `catfish` (pacote `poppler-utils`) e verifique a instalação:
#     ```bash
#     sudo apt update
#     sudo apt install poppler-utils
#     catfish -v
#     ```
# 
# 
# ## 2. Realizar uma busca simples
# 
# Você pode executar o `catfish` informando um diretório para a pesquisa:
# ```bash
# catfish ~/Documentos
# ```
# Esse comando abre a interface do programa iniciando a busca na pasta `Documentos`.
# 
# ## 3. Usar uma variável de terminal para definir o caminho de busca
# 
# Também é possível definir o diretório em uma variável antes de chamar o `catfish`:
# ```bash
# search_dir="~/Documentos"
# catfish "$search_dir"
# ```
# 
# ## Referências
# 
# [1] OPENAI. ***Instalar catfish no Linux Ubuntu***. Disponível em: <https://chatgpt.com/c/6862cf14-11c8-8002-8a1d-96488e72f5cf>. ChatGPT. Acessado em: 11/03/2025 14:23.
# 
