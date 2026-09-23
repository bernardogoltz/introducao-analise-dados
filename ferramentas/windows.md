# Windows passo a passo

Parte do curso [Introdução à análise de dados](../README.md). Este guia repete os passos do [README principal](../README.md) só para Windows e mostra em que pasta o terminal tem que estar em cada um. As explicações de cada comando e os erros menos comuns estão no README principal.

Os comandos estão em PowerShell e cmd. Quando os dois usam o mesmo comando, aparece um bloco só.

## As pastas

No fim do guia, seu computador vai ter esta estrutura. Nos exemplos, o usuário do Windows se chama `bernardo`; no seu computador aparece o nome do seu usuário.

```text
C:\Users\bernardo\                        o terminal abre aqui
└── projetos\
    └── introducao-analise-dados\         raiz do repositório: git e gh
        ├── README.md
        ├── ferramentas\
        └── 1_introducao_pandas\          pasta da aula: uv venv, activate e jupyter lab
            ├── .venv\                    criada pelo uv venv
            │   └── Scripts\activate
            ├── data\
            │   └── samp-2025-convencional.parquet
            └── src\
                ├── 01_EDA_leitura.ipynb
                └── 02_EDA_pandas.ipynb
```

| Passo | Pasta onde o terminal tem que estar |
| --- | --- |
| Instalar Git, GitHub CLI e uv | Qualquer uma |
| `gh auth login` e `git config` | Qualquer uma |
| `git clone` ou `gh repo clone` | `C:\Users\bernardo\projetos` |
| `git pull` e `git status` | `C:\Users\bernardo\projetos\introducao-analise-dados` ou qualquer pasta dentro dela |
| `uv venv`, ativar, `uv pip install` e `jupyter lab` | `C:\Users\bernardo\projetos\introducao-analise-dados\1_introducao_pandas` |

> [!TIP]
> O próprio terminal mostra a pasta atual no começo da linha. No PowerShell aparece `PS C:\Users\bernardo\projetos>`; no cmd, `C:\Users\bernardo\projetos>`. Olhe essa parte antes de rodar cada comando.

## 1. Abrir o terminal

- PowerShell: botão direito no menu Iniciar > **Terminal** (Windows 11) ou **Windows PowerShell** (Windows 10).
- cmd: `Win + R`, digite `cmd` e aperte Enter.

Não abra como administrador. O terminal de administrador começa em `C:\Windows\system32`, e é fácil acabar criando pastas lá.

O terminal normal abre na sua pasta de usuário, `C:\Users\bernardo`. Se ele estiver em outra pasta, volte para ela:

PowerShell:

```powershell
cd ~
```

cmd:

```bat
cd %USERPROFILE%
```

## 2. Instalar Git, GitHub CLI e uv

Pasta: qualquer uma. Igual no PowerShell e no cmd:

```bat
winget install --id Git.Git -e --source winget
winget install --id GitHub.cli -e
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Se o Windows pedir permissão de administrador na instalação do Git, aceite. Na primeira vez que usar o `winget`, ele pergunta se você aceita os termos da loja; responda sim.

> [!IMPORTANT]
> Feche o terminal e abra outro depois de instalar. O terminal que estava aberto não enxerga os programas novos e responde que `git`, `gh` ou `uv` "não é reconhecido". Se você usa o terminal do VS Code, feche o VS Code inteiro.

No terminal novo, confira as três instalações:

```bat
git --version
gh --version
uv --version
```

Cada comando tem que mostrar um número de versão. Se algum disser que não é reconhecido mesmo num terminal novo, veja [Instalar o uv](../README.md#5-instalar-o-uv) no README principal, que traz a correção do PATH.

## 3. Configurar o Git e entrar no GitHub

Pasta: qualquer uma. Diga ao Git seu nome e seu e-mail, que aparecem em cada commit. Use o mesmo e-mail da conta do GitHub. Igual no PowerShell e no cmd:

```bat
git config --global user.name "Seu Nome"
git config --global user.email "voce@exemplo.com"
```

Depois entre na conta do GitHub pelo `gh`:

```bat
gh auth login
```

Escolha `GitHub.com`, `HTTPS`, responda `Y` e escolha `Login with a web browser`. O `gh` mostra um código de 8 caracteres; aperte Enter, cole o código na página que abrir e autorize. Com isso o `git` também passa a usar a sua conta.

## 4. Clonar o repositório

Comece na sua pasta de usuário.

PowerShell:

```powershell
cd ~
```

cmd:

```bat
cd %USERPROFILE%
```

Crie a pasta `projetos` e entre nela. Igual no PowerShell e no cmd:

```bat
mkdir projetos
cd projetos
```

Se a pasta `projetos` já existir, o `mkdir` avisa e você segue para o `cd projetos`. O terminal fica assim:

```text
PS C:\Users\bernardo\projetos>
```

Agora clone o curso. Use o `git` ou o `gh`: os dois criam a mesma pasta `introducao-analise-dados` dentro de `projetos`.

### Com o git

Igual no PowerShell e no cmd:

```bat
git clone https://github.com/bernardogoltz/introducao-analise-dados.git
```

O endereço é o da página do repositório no GitHub com `.git` no fim. Você também encontra esse endereço no botão verde **Code**, na aba **HTTPS**.

Se o Git pedir login, o Git para Windows abre uma janela para entrar no GitHub pelo navegador. Entre com a sua conta e o clone continua. A senha do site não funciona digitada no terminal.

O `git clone` baixa o repositório, cria a pasta com o nome dele e já configura o remoto `origin` apontando para o GitHub. Por isso o `git pull` funciona depois sem mais nada.

Para clonar numa pasta com outro nome, passe o nome no fim:

```bat
git clone https://github.com/bernardogoltz/introducao-analise-dados.git curso-dados
```

Este guia usa o nome padrão, `introducao-analise-dados`.

### Com o gh

Igual no PowerShell e no cmd:

```bat
gh repo clone bernardogoltz/introducao-analise-dados
```

No `gh`, basta `usuario/repositorio`, sem o endereço completo. Ele usa o login do passo 3.

### Entrar no repositório

Igual no PowerShell e no cmd:

```bat
cd introducao-analise-dados
git remote -v
```

O `git remote -v` mostra o endereço do GitHub duas vezes, uma para `fetch` e outra para `push`. Se aparecer, o clone deu certo.

Agora o terminal está na raiz do repositório:

```text
PS C:\Users\bernardo\projetos\introducao-analise-dados>
```

> [!WARNING]
> Não clone dentro de uma pasta sincronizada com o OneDrive, como `Documentos` ou `Área de Trabalho` em muitos Windows 11. Se o caminho tiver `OneDrive`, você está numa delas. O OneDrive tenta enviar os milhares de arquivos do `.venv` e pode bloquear arquivos enquanto o Python usa. `C:\Users\bernardo\projetos` fica fora do OneDrive.

## 5. Entrar na pasta da aula

Da raiz do repositório. Igual no PowerShell e no cmd:

```bat
cd 1_introducao_pandas
```

O terminal fica assim:

```text
PS C:\Users\bernardo\projetos\introducao-analise-dados\1_introducao_pandas>
```

Liste os arquivos para conferir. No PowerShell use `ls`; no cmd, `dir`. Tem que aparecer `data`, `src` e `README.md`.

## 6. Criar o ambiente virtual

> [!IMPORTANT]
> Rode o `uv venv` dentro de `1_introducao_pandas`. O `.venv` nasce na pasta onde o terminal está: se você rodar em `projetos` ou na raiz do repositório, o ambiente vai parar no lugar errado e a ativação da pasta da aula não vai achá-lo.

Igual no PowerShell e no cmd:

```bat
uv venv
```

Liste os arquivos de novo. Agora aparece a pasta `.venv` ao lado de `data` e `src`.

Só precisa criar uma vez por aula. Na próxima aula, entre na pasta dela e rode `uv venv` lá também: cada aula tem o próprio `.venv`.

## 7. Ativar o ambiente

> [!IMPORTANT]
> Ative da pasta que tem o `.venv`, a `1_introducao_pandas`. O caminho `.venv\Scripts\activate` é relativo: se o terminal estiver em `src` ou em qualquer outra pasta, o Windows não encontra o arquivo. Se estiver em `src`, volte com `cd ..`.

PowerShell:

```powershell
.venv\Scripts\activate
```

cmd:

```bat
.venv\Scripts\activate
```

Git Bash:

```bash
source .venv/Scripts/activate
```

Deu certo quando o nome da pasta aparece entre parênteses no começo da linha:

```text
(1_introducao_pandas) PS C:\Users\bernardo\projetos\introducao-analise-dados\1_introducao_pandas>
```

Se o PowerShell disser que "a execução de scripts foi desabilitada neste sistema", rode uma vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Responda `S` se ele pedir confirmação e ative de novo. O cmd não tem essa trava.

## 8. Instalar os pacotes

Com o ambiente ativo, na pasta da aula. Igual no PowerShell e no cmd:

```bat
uv pip install jupyterlab pandas numpy matplotlib
```

> [!WARNING]
> Use `uv pip install`, e não `pip install`. O `.venv` do `uv` não tem `pip` dentro, então o `pip install` dá erro ou instala os pacotes no Python do sistema, fora do ambiente.

Também é uma vez por aula. Os pacotes ficam guardados no `.venv`.

## 9. Abrir os notebooks

Com o ambiente ativo, na pasta da aula. Igual no PowerShell e no cmd:

```bat
jupyter lab
```

O navegador abre com a pasta `1_introducao_pandas` na lateral. Entre em `src` e abra `01_EDA_leitura.ipynb`.

> [!TIP]
> Abra o Jupyter a partir de `1_introducao_pandas`. A lateral só mostra a pasta onde você rodou o comando e as que estão dentro dela. Os notebooks leem os dados de `../data`, então não mude os arquivos de pasta.

Para fechar, volte ao terminal e aperte `Ctrl + C` duas vezes.

## Da próxima vez

O ambiente e os pacotes continuam no disco, mas todo terminal novo começa na pasta de usuário e com o ambiente desativado. São três comandos.

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

Para baixar aulas novas, rode `git pull` na raiz do repositório antes:

PowerShell:

```powershell
cd ~\projetos\introducao-analise-dados
git pull
```

cmd:

```bat
cd %USERPROFILE%\projetos\introducao-analise-dados
git pull
```

## Erros comuns

| O que aparece | Por quê | O que fazer |
| --- | --- | --- |
| `git`, `gh` ou `uv` "não é reconhecido" | O terminal foi aberto antes da instalação. | Feche e abra o terminal. Se continuar, veja [Instalar o uv](../README.md#5-instalar-o-uv). |
| O terminal não encontra `.venv\Scripts\activate` | O terminal está fora da pasta da aula, ou o `uv venv` não foi rodado nela. | Confira a pasta no começo da linha, entre em `1_introducao_pandas` e liste os arquivos. Se não houver `.venv`, rode `uv venv`. |
| "A execução de scripts foi desabilitada neste sistema" | O PowerShell bloqueia scripts por padrão. | Rode `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` uma vez. |
| Um `.venv` apareceu em `projetos` ou na raiz do repositório | O `uv venv` rodou na pasta errada. | Na pasta errada, apague com `rm -Recurse .venv` (PowerShell) ou `rmdir /s /q .venv` (cmd). Depois crie o ambiente dentro de `1_introducao_pandas`. |
| `jupyter` "não é reconhecido" | O ambiente não está ativo ou os pacotes não foram instalados. | Ative o ambiente e rode `uv pip list`. Se o `jupyterlab` não estiver na lista, instale os pacotes. |
| `ModuleNotFoundError: No module named 'pandas'` no notebook | O Jupyter que abriu é de outro Python, como o do Anaconda. | Feche o Jupyter, ative o `.venv` e rode `jupyter lab` de novo. `Get-Command jupyter` (PowerShell) ou `where jupyter` (cmd) tem que mostrar um caminho com `1_introducao_pandas\.venv\Scripts`. |

Outros comandos de terminal, Git e `uv` estão nas [colas de comandos](README.md).
