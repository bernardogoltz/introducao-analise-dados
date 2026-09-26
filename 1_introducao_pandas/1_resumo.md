# Ativar o ambiente e abrir o Jupyter

O terminal fica em `1_introducao_pandas` para criar o ambiente, ativar e abrir o Jupyter.

```text
projetos/introducao-analise-dados/1_introducao_pandas
```

| O que fazer | Pasta |
| --- | --- |
| Abrir o terminal | `1_introducao_pandas`, pelo Explorador de Arquivos |
| `uv venv`, ativar, `uv pip install`, `jupyter lab` | `1_introducao_pandas` |
| Abrir o notebook | no navegador, em `src/` |

A linha do terminal termina em `1_introducao_pandas`. Se terminar em `src`, volte um nível com `cd ..`.

## Toda vez

### Abrir o PowerShell já na pasta

No Explorador de Arquivos, entre em `projetos\introducao-analise-dados\1_introducao_pandas`. Clique com o botão direito num espaço vazio dessa pasta:

- Windows 11: **Abrir no Terminal**
- Windows 10: segure Shift, clique com o botão direito e escolha **Abrir janela do PowerShell aqui**

O PowerShell abre com a linha já terminando em `1_introducao_pandas`. Aí são dois comandos:

```powershell
.venv\Scripts\activate
jupyter lab
```

Na barra de endereço do Explorador, digitar `powershell` e apertar Enter abre o PowerShell nessa mesma pasta.

### Se o terminal abriu na pasta do usuário

Aí o `cd` entra na aula antes de ativar.

PowerShell:

```powershell
cd ~\projetos\introducao-analise-dados\1_introducao_pandas
.venv\Scripts\activate
jupyter lab
```

cmd:

```bat
cd %USERPROFILE%\projetos\introducao-analise-dados\1_introducao_pandas
.venv\Scripts\activate
jupyter lab
```

Linux e macOS:

```bash
cd ~/projetos/introducao-analise-dados/1_introducao_pandas
source .venv/bin/activate
jupyter lab
```

Git Bash no Windows:

```bash
cd ~/projetos/introducao-analise-dados/1_introducao_pandas
source .venv/Scripts/activate
jupyter lab
```

A ativação deu certo quando a linha começa com `(1_introducao_pandas)`. No navegador, abra `src/01_EDA_leitura.ipynb`. Para fechar, `Ctrl + C` duas vezes no terminal.

## Primeira vez nesta aula

Ainda em `1_introducao_pandas`, crie o ambiente uma vez:

```bash
uv venv
```

Ative com o comando do seu terminal, no bloco acima, e instale os pacotes:

```bash
uv pip install jupyterlab pandas numpy matplotlib
```

Depois rode `jupyter lab`. Nas próximas vezes, abra o PowerShell na pasta e rode os dois comandos de ativar e `jupyter lab`.

Se o PowerShell recusar a ativação, libere os scripts uma vez, responda `S` e ative de novo:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
