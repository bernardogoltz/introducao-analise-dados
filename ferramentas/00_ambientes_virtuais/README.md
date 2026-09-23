# Ambiente virtual

Parte do curso [Introdução à análise de dados](../../README.md). Outras ferramentas e as colas de comandos estão em [Ferramentas](../README.md).

Um ambiente virtual guarda os pacotes do projeto numa pasta `.venv`, separado do Python do sistema.

## Instalar o uv

### Linux e macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Com pip

```bash
pip install uv
```

## Criar com uv

Cria o `.venv`, instala os pacotes nele e abre o Jupyter nesse ambiente.

```bash
uv venv
uv pip install jupyter pandas numpy matplotlib
uv run jupyter notebook
```

## Criar com venv

Cria o `.venv` com o Python do sistema. O `source` ativa o ambiente; o `pip` instala só dentro dele.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter pandas numpy matplotlib
jupyter notebook
```
