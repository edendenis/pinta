#!/usr/bin/env python
# coding: utf-8

# # Como instalar o `pdftotext` no `Linux Ubuntu`

# ## Resumo
# 
# Este documento apresenta os passos necessários para instalar o utilitário `pdftotext` no `Linux Ubuntu`.

# ## _Abstract_
# 
# _This document shows the steps required to install the `pdftotext` utility on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `pdftotext`
# 
# O `pdftotext` é uma ferramenta de linha de comando, geralmente parte do pacote `Poppler` ou `Xpdf`, que converte o conteúdo de arquivos PDF em texto simples. Ele extrai o texto mantendo a ordem de leitura e pode preservar ou não a formatação de colunas e quebras de linha, conforme opções configuráveis. É muito útil para automatizar a extração de texto de documentos PDF em _scripts_ e fluxos de trabalho de análise de dados ou indexação.
# 
# ### `translate-shell`
# 
# O `translate-shell` é uma ferramenta de linha de comando de código aberto que oferece a capacidade de traduzir texto e palavras entre vários idiomas diretamente do `Terminal Emulator`. Ele utiliza serviços de tradução _online_, como o `Google Translate`, para fornecer traduções rápidas e precisas. O `translate-shell` suporta uma ampla variedade de idiomas e pode ser usado tanto para traduções simples de palavras e frases quanto para traduções mais complexas de texto completo. Além disso, ele oferece opções avançadas, como tradução de áudio, detecção automática de idioma e pronúncia de palavras, tornando-se uma ferramenta útil para estudantes, viajantes e qualquer pessoa que precise de traduções instantâneas e convenientes diretamente do `Terminal Emulator`.
# 
# ### `pdfimages`
# 
# O `pdfimages` é uma ferramenta para extrair imagens de arquivos PDF. Caso seu PDF contenha imagens e você queira extraí-las, pode ser útil antes de uma conversão com OCR, como no caso de um PDF digitalizado.
# 
# ### `qpdf`
# 
# O `qpdf` é uma ferramenta para manipular arquivos PDF de maneira avançada. Você pode usá-lo para fazer operações como quebra de PDFs, mesclagem, e até mesmo para manipular metadados.
# 
# ### `pdfunite`
# 
# O `pdfunite` é uma ferramenta de linha de comando, integrante do pacote Poppler, que permite mesclar vários arquivos PDF em um único documento. Basta informar na chamada os arquivos de entrada e o nome do PDF de saída. É ideal para scripts e fluxos de trabalho automatizados de organização e consolidação de documentos.
# 
# ### `tesseract`
# 
# O `Tesseract` é um mecanismo de OCR (Reconhecimento Óptico de Caracteres) de código aberto, originalmente desenvolvido pela HP e atualmente mantido pelo Google. Ele converte imagens de texto em texto editável, suportando múltiplos idiomas e formatos de imagem, além de oferecer opções de treinamento para reconhecer fontes e caracteres personalizados. Muito utilizado em projetos de digitalização e extração automatizada de dados, o `Tesseract` é integrado a diversas aplicações e bibliotecas em linguagens como `Python`, `Java` e `C++`.
# 
# ### `gImageReader`
# 
# O `gImageReader` é uma aplicação de código aberto que oferece uma interface amigável para a extração de texto de imagens ou arquivos `.pdf`. Ele utiliza tecnologias de reconhecimento óptico de caracteres (OCR) para digitalizar documentos e converter o texto contido neles em formato editável. Com recursos como suporte a vários idiomas e opções de formatação, o gImageReader é uma ferramenta útil para transformar documentos digitalizados em texto pesquisável e editável.
# 
# **ATENÇÃO**: Você pode utilizar o `pdftotext` e/ou o `tesseract` em arquivos `.pdf` para converter em `.txt` e depois traduzir para o português brasileiro com os comandos do `translate-shell` que serão apresentados depois do passo a passo de como instalar o `translate-shell`.

# ## 1. Instalar o `pdftotext` no `Linux Ubuntu`
# 
# Para instalar o `pdftotext`, siga os passos abaixo:
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
# 3. Instale o `pdftotext` (pacote `poppler-utils`) e verifique a instalação:
#     ```bash
#     sudo apt update
#     sudo apt install poppler-utils
#     pdftotext -v
#     ```
# 

# ## 2. Converter um arquivo .pdf em .txt
# 
# Você pode usar o comando `pdftotext` para converter um arquivo PDF em um arquivo de texto. O comando básico é:
# ```bash
# pdftotext input.pdf output.txt
# ```
# Isso vai converter o arquivo `input.pdf` para o arquivo de texto `output.txt`.

# ## 3. Converter um arquivo .pdf em .txt a partir de uma variável de terminal e mantê-lo com o mesmo nome
# 
# Você pode usar variáveis no terminal para manipular os nomes dos arquivos. Aqui está um exemplo onde o nome do arquivo PDF é armazenado em uma variável e a conversão é feita mantendo o mesmo nome para o arquivo de saída, apenas com a extensão `.txt`.
# ```bash
# pdf_file="documento.pdf"
# txt_file="${pdf_file%.pdf}.txt"
# pdftotext "$pdf_file" "$txt_file"
# ```
# A instrução `txt_file="${pdf_file%.pdf}.txt"` cria a variável `txt_file` substituindo a extensão `.pdf` por `.txt`. O comando `pdftotext "$pdf_file" "$txt_file"` executa a conversão usando os valores das variáveis.

# ## Referências
# 
# [1] OPENAI. ***Instalar pdftotext no Linux Ubuntu***. Disponível em: <https://chatgpt.com/c/6862cf14-11c8-8002-8a1d-96488e72f5cf>. ChatGPT. Acessado em: 11/03/2025 14:23.
