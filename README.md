# Introdução à análise de dados

Estes passos são na sua máquina. O ambiente do `uv` fica só com você e não entra no GitHub.

## Instalar o GitHub CLI

O `gh` é a linha de comando do GitHub. Abra um terminal novo depois de instalar.

### Windows

```powershell
winget install --id GitHub.cli
```

### macOS

```bash
brew install gh
```

### Linux

No Fedora:

```bash
sudo dnf install gh
```

No Ubuntu:

```bash
sudo apt install gh
```

Outras distribuições: [instalação do GitHub CLI](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).

## Clonar o repositório

Entre na conta:

```bash
gh auth login
```

Vá para uma pasta qualquer, crie a subpasta `projetos` e clone o curso aí:

```bash
mkdir projetos
cd projetos
gh repo clone bernardogoltz/introducao-analise-dados
cd introducao-analise-dados
```

O endereço do repositório é [github.com/bernardogoltz/introducao-analise-dados](https://github.com/bernardogoltz/introducao-analise-dados).

## Instalar o uv

### Linux e macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Feche e abra o terminal para o comando `uv` valer.

## Rodar os notebooks

Dentro do repositório clonado, crie um ambiente do zero e abra o Jupyter Lab na pasta da aula:

```bash
cd 1_introducao_pandas
uv venv
uv pip install jupyterlab pandas numpy matplotlib
uv run jupyter lab
```

No navegador, abra `src/01_EDA_leitura.ipynb` e `src/02_EDA_pandas.ipynb`.

O `uv venv` cria a pasta `.venv` só na sua máquina. Não rode `uv init` aqui. Não faça commit de `.venv`, `uv.lock` nem `pyproject.toml`: nada do `uv` vai para o GitHub.
