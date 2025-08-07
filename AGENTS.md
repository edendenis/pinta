# Instruções Gerais

* O usuário irá fornecer uma tarefa.
* A tarefa envolve trabalhar com repositórios Git no seu diretório de trabalho atual.
* Aguarde até que todos os comandos de terminal sejam concluídos (ou cancelados) antes de finalizar.

## Git

Se for necessário criar ou modificar arquivos:

* **Não** crie novos `branches`.
* Use o Git para **commitar** suas alterações.
* Se o *pre-commit* falhar, corrija e tente novamente.
* Verifique `git status` para confirmar que sua *worktree* está limpa.
* Apenas o código **committed** será avaliado.
* **Não** modifique ou altere *commits* existentes.
* Sempre faça as alterações baseadas no último `commit` da branch `main`.

## Especificação de `AGENTS.md`

* Repositórios podem conter arquivos `AGENTS.md` em `/`, `~` ou pastas internas.
* Eles orientam sobre convenções de código, organização e execução do projeto.
* Se contiverem instruções sobre mensagens de Pull Request, **respeite-as**.
* O escopo é a árvore de diretórios a partir de onde estão.
* `AGENTS.md` aninhados têm precedência sobre os mais gerais.
* Instruções de sistema/desenvolvedor/usuário na conversa têm precedência sobre o `AGENTS.md`.
* Se o `AGENTS.md` define checagens programáticas, **execute-as** e certifique-se de que passam.

## Instruções de Citação

* Se navegar em arquivos ou usar comandos de terminal, **cite** no texto final:
  * **Arquivo**: `【F:<caminho_do_arquivo>†L<linha_inicial>(-L<linha_final>)?】`
  * **Terminal**: `【<chunk_id>†L<linha_inicial>(-L<linha_final>)?】`
* Prefira citações de **arquivo**.
* Não cite commits nem URLs diretas.

## Convenções de Código e Documentação

### Python

1. **Cabeçalho**:

```python
# -*- coding: utf-8 -*-
```

2. **Linguagem**:

* Texto da resposta: **português brasileiro**.
* Comentários: **português brasileiro**.
* Identificadores: **inglês (EUA)**.
* Saídas (`print`, `input`): **inglês (EUA)**.

3. **Estilo PEP8 / PEP257**:

* Sem espaços em branco no final.
* 100 colunas por linha.

4. **Docstrings & Sphinx**:

```python
r"""
Docstring em pt-BR com bloco Sphinx:

.. math:: \dfrac{u}{v}
"""
```
