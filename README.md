# Introdução à análise de dados

Estes passos são na sua máquina. O ambiente do `uv` fica só com você e não entra no GitHub.

Cada instalação tem os comandos para os três terminais: PowerShell e cmd no Windows, bash no Linux, no macOS e no Git Bash do Windows.

As colas de comandos de terminal, Git, `uv` e Jupyter, e o material sobre Git e ambiente virtual, estão em [Ferramentas](ferramentas/README.md).

> [!TIP]
> No Windows, siga o [Windows passo a passo](ferramentas/windows.md). Ele junta estes passos só com PowerShell e cmd e mostra em que pasta o terminal tem que estar em cada um.

1. [Escolher o terminal](#1-escolher-o-terminal)
2. [Instalar o Git](#2-instalar-o-git)
3. [Instalar o GitHub CLI](#3-instalar-o-github-cli)
4. [Clonar o repositório](#4-clonar-o-repositório)
5. [Instalar o uv](#5-instalar-o-uv)
6. [Criar e ativar o ambiente virtual](#6-criar-e-ativar-o-ambiente-virtual)
7. [Rodar os notebooks](#7-rodar-os-notebooks)

## 1. Escolher o terminal

Use o terminal que preferir. Os comandos mudam um pouco de um para outro, e cada passo abaixo mostra a versão de cada um.

| Terminal | Onde tem | Como abrir | Como a linha começa |
| --- | --- | --- | --- |
| PowerShell | Windows | Botão direito no menu Iniciar > **Terminal** (Windows 11) ou **Windows PowerShell** (Windows 10) | `PS C:\Users\bernardo>` |
| cmd | Windows | `Win + R`, digite `cmd`, Enter | `C:\Users\bernardo>` |
| Git Bash | Windows, depois de instalar o Git | Menu Iniciar > **Git Bash** | `bernardo@PC MINGW64 ~` |
| bash | Linux e macOS | Abra o app **Terminal** | `bernardo@maquina:~$` |

Nos exemplos, o usuário se chama `bernardo`. No seu computador aparece o nome do seu usuário.

Não precisa abrir o terminal como administrador.

No Windows, as instalações usam o `winget`, que já vem no Windows 10 e 11. Na primeira vez ele pergunta se você aceita os termos da loja: responda sim com a letra que aparecer na tela (`Y` ou `S`) e aperte Enter. Se o terminal disser que o `winget` não existe, instale o **Instalador de Aplicativo** pela Microsoft Store.

> [!IMPORTANT]
> Depois de cada instalação, feche o terminal e abra outro. Um terminal que já estava aberto não enxerga os programas novos e responde que o comando "não é reconhecido".

## 2. Instalar o Git

O Git guarda o histórico dos arquivos. O GitHub CLI usa o Git para clonar o repositório, então ele vem primeiro.

### Windows

Se o Windows pedir permissão de administrador durante a instalação, aceite.

#### PowerShell

```powershell
winget install --id Git.Git -e --source winget
```

#### cmd

```bat
winget install --id Git.Git -e --source winget
```

#### bash

O Git Bash vem junto com o Git, então ainda não existe. Instale pelo PowerShell ou pelo cmd. A partir daqui, o Git Bash aparece no menu Iniciar.

### Linux (bash)

No Fedora:

```bash
sudo dnf install git
```

No Ubuntu:

```bash
sudo apt install git
```

### macOS (bash)

```bash
brew install git
```

### Conferir e configurar

Num terminal novo, em qualquer um dos três:

```bash
git --version
```

Diga ao Git seu nome e seu e-mail. Eles aparecem em cada commit. Use o mesmo e-mail da sua conta do GitHub. Os comandos são iguais em bash, PowerShell e cmd:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "voce@exemplo.com"
```

## 3. Instalar o GitHub CLI

O `gh` é a linha de comando do GitHub. Ele faz o login na sua conta e clona o repositório.

### Windows

#### PowerShell

```powershell
winget install --id GitHub.cli -e
```

#### cmd

```bat
winget install --id GitHub.cli -e
```

#### bash (Git Bash)

```bash
winget install --id GitHub.cli -e
```

### Linux (bash)

No Fedora:

```bash
sudo dnf install gh
```

No Ubuntu:

```bash
sudo apt install gh
```

Outras distribuições: [instalação do GitHub CLI](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).

### macOS (bash)

```bash
brew install gh
```

### Conferir

Num terminal novo:

```bash
gh --version
```

## 4. Clonar o repositório

Entre na conta. O comando é igual nos três terminais:

```bash
gh auth login
```

O `gh` faz algumas perguntas. Escolha `GitHub.com`, depois `HTTPS`, responda `Y` para autenticar o Git com suas credenciais e escolha `Login with a web browser`. Ele mostra um código de 8 caracteres; aperte Enter, cole o código na página que abrir e autorize.

Vá para uma pasta qualquer, crie a subpasta `projetos` e clone o curso aí. Esses comandos também são iguais em bash, PowerShell e cmd:

```bash
mkdir projetos
cd projetos
gh repo clone bernardogoltz/introducao-analise-dados
cd introducao-analise-dados
```

O endereço do repositório é [github.com/bernardogoltz/introducao-analise-dados](https://github.com/bernardogoltz/introducao-analise-dados).

> [!NOTE]
> Depois do último `cd`, o terminal está na raiz do repositório, a pasta `introducao-analise-dados`. Os próximos passos partem dela. No Windows, não clone dentro de uma pasta sincronizada com o OneDrive: o OneDrive tenta enviar os milhares de arquivos do `.venv`. Veja o [Windows passo a passo](ferramentas/windows.md#4-clonar-o-repositório).

## 5. Instalar o uv

O `uv` cria ambientes virtuais e instala pacotes do Python. Não precisa instalar o Python antes: o `uv` baixa um na primeira vez que você cria um ambiente.

### Windows

O comando é o mesmo nos três terminais. Ele abre um PowerShell, baixa o instalador oficial e roda. O `-ExecutionPolicy ByPass` libera scripts só para esse comando; a configuração do Windows continua a mesma. Como o comando começa chamando o `powershell`, o cmd e o Git Bash conseguem rodá-lo também.

#### PowerShell

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### cmd

```bat
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### bash (Git Bash)

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Se o instalador for bloqueado

O antivírus ou a política de um computador da empresa ou da faculdade pode barrar o comando acima. Nesse caso, instale pelo `winget`, com o mesmo comando nos três terminais:

```bat
winget install --id=astral-sh.uv -e
```

### Linux e macOS (bash)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Conferir

Feche o terminal e abra outro. Se você usa o terminal do VS Code, feche o VS Code inteiro. Depois rode, em qualquer terminal:

```bash
uv --version
```

Tem que aparecer `uv` e o número da versão.

### Se o terminal disser que o `uv` não é reconhecido

No cmd a mensagem é:

```text
'uv' não é reconhecido como um comando interno ou externo, um programa operável ou um arquivo em lotes.
```

No PowerShell:

```text
uv : O termo 'uv' não é reconhecido como nome de cmdlet, função, arquivo de script ou programa operável.
```

No bash:

```text
bash: uv: command not found
```

O instalador põe o `uv` na pasta `.local\bin` do seu usuário e adiciona essa pasta ao PATH. Se a mensagem continuar num terminal novo, coloque a pasta no PATH só nessa janela para testar.

#### PowerShell

```powershell
$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
uv --version
```

#### cmd

```bat
set PATH=%USERPROFILE%\.local\bin;%PATH%
uv --version
```

#### bash (Linux, macOS e Git Bash)

```bash
export PATH="$HOME/.local/bin:$PATH"
uv --version
```

Se agora aparecer a versão, o `uv` está instalado e falta gravar o PATH de vez.

- Windows: procure "variáveis de ambiente" no menu Iniciar e abra **Editar as variáveis de ambiente para sua conta**. Selecione `Path`, clique em **Editar**, depois em **Novo**, cole `%USERPROFILE%\.local\bin` e confirme com **OK**.
- Linux e macOS: rode o instalador de novo. Ele grava o PATH no arquivo de configuração do seu shell.

Abra um terminal novo e teste outra vez.

Isso vale para o instalador. Se você instalou pelo `winget` e o `uv` não aparece, rode o `winget install` de novo e reabra o terminal.

### Atualizar

Igual nos três terminais:

```bash
uv self update
```

Se instalou pelo `winget`, use `winget upgrade astral-sh.uv`.

## 6. Criar e ativar o ambiente virtual

Um ambiente virtual é uma pasta `.venv` dentro da pasta do projeto. Ela guarda um Python e os pacotes só daquele projeto, sem mexer no resto do computador. Cada aula tem o próprio `.venv`.

### Entrar na pasta

Os comandos desta seção rodam na pasta da aula:

```text
projetos/
└── introducao-analise-dados/      raiz do repositório
    └── 1_introducao_pandas/       pasta da aula: rode uv venv, activate e jupyter lab aqui
        ├── .venv/                 criada pelo uv venv
        ├── data/
        └── src/
```

Da raiz do repositório, entre na pasta da aula. O comando é igual nos três terminais:

```bash
cd 1_introducao_pandas
```

> [!IMPORTANT]
> O `.venv` nasce na pasta onde o terminal está. Antes do `uv venv`, confira se o caminho no começo da linha termina em `1_introducao_pandas`. No bash e no PowerShell, `pwd` mostra a pasta atual; no cmd, `cd` sem nada depois. Se você rodar em `projetos` ou na raiz do repositório, o ambiente vai parar no lugar errado.

### Criar o ambiente

Igual nos três terminais:

```bash
uv venv
```

A saída termina assim:

```text
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

A linha `Activate with:` mostra o comando de ativação. No Windows ela aparece com `.venv\Scripts\activate`.

Para escolher a versão do Python, passe `--python`, por exemplo `uv venv --python 3.12`. O `uv` baixa essa versão se você não tiver.

Só precisa criar uma vez por pasta. Se o `.venv` já existir, o `uv` não troca por um novo sem sua confirmação. Para recriar do zero, use `uv venv --clear`, que apaga os pacotes instalados.

### Ativar o ambiente

Ativar faz o `python` e o `jupyter` daquele terminal serem os do `.venv`.

> [!IMPORTANT]
> Ative da pasta que tem o `.venv`, a `1_introducao_pandas`. O caminho `.venv\Scripts\activate` é relativo à pasta atual: se o terminal estiver em `src` ou em outra pasta, o arquivo não é encontrado. De `src`, volte com `cd ..`.

#### PowerShell

```powershell
.venv\Scripts\activate
```

Na primeira vez, o PowerShell pode recusar:

```text
.venv\Scripts\activate : O arquivo C:\...\activate.ps1 não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.
```

Libere os scripts criados na sua máquina para o seu usuário. Só precisa fazer isso uma vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Se ele pedir confirmação, responda `S`. Depois rode `.venv\Scripts\activate` de novo. Se preferir não mudar essa configuração, use `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process`, que vale só até fechar a janela.

#### cmd

```bat
.venv\Scripts\activate
```

#### bash (Git Bash no Windows)

No Windows o `.venv` usa a pasta `Scripts`:

```bash
source .venv/Scripts/activate
```

#### bash (Linux e macOS)

```bash
source .venv/bin/activate
```

### Conferir se ativou

O nome da pasta aparece entre parênteses no começo da linha. No PowerShell fica assim:

```text
(1_introducao_pandas) PS C:\Users\bernardo\projetos\introducao-analise-dados\1_introducao_pandas>
```

Para confirmar qual Python está em uso, rode em qualquer terminal:

```bash
python -c "import sys; print(sys.prefix)"
```

O caminho impresso tem que terminar em `1_introducao_pandas\.venv` (Windows) ou `1_introducao_pandas/.venv` (Linux e macOS).

### Instalar pacotes

Com o ambiente ativo, igual nos três terminais:

```bash
uv pip install jupyterlab pandas numpy matplotlib
```

> [!WARNING]
> Use `uv pip install`, e não `pip install`. O `uv venv` não coloca o `pip` dentro do `.venv`, então um `pip install` vai dar erro ou instalar no Python do sistema.

### Desativar

Igual nos três terminais:

```bash
deactivate
```

O nome entre parênteses some da linha.

### Da próxima vez

O ambiente continua na pasta, mas cada terminal novo começa desativado. Abra o terminal, entre na pasta da aula com `cd` e rode o comando de ativação do seu terminal. Não precisa rodar `uv venv` nem instalar os pacotes de novo.

Sem ativar, dá para rodar um comando dentro do ambiente com `uv run`. Ele usa o `.venv` da pasta atual:

```bash
uv run jupyter lab
```

## 7. Rodar os notebooks

Com o ambiente da pasta `1_introducao_pandas` ativo, abra o Jupyter Lab. Igual nos três terminais:

```bash
jupyter lab
```

No navegador, abra `src/01_EDA_leitura.ipynb` e `src/02_EDA_pandas.ipynb`.

Para fechar o Jupyter, volte ao terminal e aperte `Ctrl + C` duas vezes.

> [!WARNING]
> O `uv venv` cria a pasta `.venv` só na sua máquina. Não rode `uv init` aqui. Não faça commit de `.venv`, `uv.lock` nem `pyproject.toml`: nada do `uv` vai para o GitHub.
