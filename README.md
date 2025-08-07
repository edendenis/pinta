# Como instalar o `pinta` no `Linux Ubuntu`

## Resumo

Este documento apresenta os passos necessários para instalar o utilitário `pinta` no `Linux Ubuntu`.

## _Abstract_

_This document shows the steps required to install the `pinta` utility on `Linux Ubuntu`._

## Descrição [2]

### `pinta`

O `pinta` é um editor de imagens simples inspirado no `Paint.NET` e voltado para ambientes `Linux`.

## 1. Instalar o `pinta` no `Linux Ubuntu`

Para instalar o `pinta`, siga os passos abaixo:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    ```bash
    sudo apt clean
    ```

    2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
    ```bash
    sudo apt clean
    ```

    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt full-upgrade -y
    ```

3. Instale o `pinta` e verifique a instalação:
    ```bash
    sudo apt update
    sudo apt install pinta
    pinta --version
    ```

## 2. Abrir o `pinta` pelo terminal

Você pode executar o `pinta` diretamente no terminal:
```bash
pinta
```
Esse comando abre a interface do programa.

## 3. Abrir uma imagem usando variável de terminal

Também é possível definir o caminho de uma imagem em uma variável antes de chamar o `pinta`:
```bash
img_file="~/Imagens/exemplo.png"
pinta "$img_file"
```

## Referências

<<<<<<< HEAD
[1] OPENAI. ***Instalar catfish no Linux Ubuntu***. Disponível em: <https://chatgpt.com/c/6862cf14-11c8-8002-8a1d-96488e72f5cf>. ChatGPT. Acessado em: 11/03/2025 14:23.
=======
[1] OPENAI. ***Instalar pinta no Linux Ubuntu***. Disponível em: <https://chatgpt.com/c/68942e26-b7a0-832f-9c96-7c57044cb43a>. ChatGPT. Acessado em: 07/08/2025 05:14.
>>>>>>> codex/revise-project-documentation-for-pinta-installation

