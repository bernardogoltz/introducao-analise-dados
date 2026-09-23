# Ferramentas

Material de apoio do curso [Introdução à análise de dados](../README.md). O repositório está em [github.com/bernardogoltz/introducao-analise-dados](https://github.com/bernardogoltz/introducao-analise-dados).

Antes das aulas, siga o [README principal](../README.md): ele instala o Git, o GitHub CLI e o `uv`, clona o repositório e cria o ambiente virtual. Volte aqui quando precisar lembrar um comando.

Aulas:

- [Aula 1: introdução ao pandas](../1_introducao_pandas/)

Ferramentas:

- [Windows passo a passo](windows.md): todos os passos do curso no Windows, com a pasta certa para cada comando.
- [Git](00_git/README.md): conceitos, branches, merge e conflitos.
- [Ambiente virtual](00_ambientes_virtuais/README.md): criar um `.venv` com `uv` ou com `venv`.

Esta página junta os comandos que você mais vai usar no terminal. As tabelas mostram a versão de cada terminal lado a lado: bash (Linux, macOS e Git Bash no Windows), PowerShell e cmd.

1. [Como ler um comando](#como-ler-um-comando)
2. [Atalhos do terminal](#atalhos-do-terminal)
3. [Pastas e arquivos](#pastas-e-arquivos)
4. [Procurar, variáveis e saída](#procurar-variáveis-e-saída)
5. [Git](#git)
6. [GitHub CLI](#github-cli)
7. [uv](#uv)
8. [Jupyter](#jupyter)
9. [Para consultar depois](#para-consultar-depois)

## Como ler um comando

```bash
git commit -m "corrige a leitura do csv"
```

- `git` é o programa.
- `commit` é o subcomando, a ação que o programa vai fazer.
- `-m` é uma opção. Opções começam com `-` (forma curta, como `-m`) ou `--` (forma longa, como `--message`).
- `"corrige a leitura do csv"` é o valor da opção. As aspas juntam as palavras num valor só.

Quase todo programa mostra a própria ajuda:

| bash | PowerShell | cmd |
| --- | --- | --- |
| `git --help` | `git --help` | `git --help` |
| `man ls` (Linux e macOS) | `Get-Help Get-ChildItem` | `dir /?` |

## Atalhos do terminal

| Atalho | O que faz |
| --- | --- |
| `Tab` | Completa o nome de arquivo, pasta ou comando. Digite o começo e aperte. |
| `↑` e `↓` | Anda pelos comandos que você já rodou. |
| `Ctrl + R` | Busca no histórico (bash e PowerShell). No cmd, `F7` mostra a lista. |
| `Ctrl + C` | Interrompe o comando que está rodando. |
| `Ctrl + L` | Limpa a tela (bash e PowerShell). No cmd, rode `cls`. |
| `Ctrl + Shift + V` | Cola no terminal do Linux. No Windows é `Ctrl + V` ou o botão direito do mouse; no macOS, `Cmd + V`. |

Caminhos:

- `.` é a pasta atual, `..` é a pasta de cima e `~` é a sua pasta de usuário. No cmd, use `%USERPROFILE%` no lugar de `~`.
- O bash separa pastas com `/`. O cmd usa `\`. O PowerShell aceita os dois.
- Nome com espaço vai entre aspas: `cd "Meus Documentos"`.

No PowerShell, `ls`, `cp`, `mv`, `rm` e `cat` são apelidos de comandos do próprio PowerShell. O nome funciona, mas as opções do bash não. `ls -la` e `rm -rf` dão erro; use as versões da tabela abaixo.

## Pastas e arquivos

| Tarefa | bash | PowerShell | cmd |
| --- | --- | --- | --- |
| Mostrar onde estou | `pwd` | `pwd` | `cd` |
| Listar arquivos | `ls` | `ls` | `dir` |
| Listar com ocultos | `ls -la` | `ls -Force` | `dir /a` |
| Entrar numa pasta | `cd dados` | `cd dados` | `cd dados` |
| Voltar uma pasta | `cd ..` | `cd ..` | `cd ..` |
| Ir para a pasta do usuário | `cd ~` | `cd ~` | `cd %USERPROFILE%` |
| Criar pasta | `mkdir dados` | `mkdir dados` | `mkdir dados` |
| Criar arquivo vazio | `touch notas.txt` | `New-Item notas.txt` | `type nul > notas.txt` |
| Ver o conteúdo | `cat notas.txt` | `cat notas.txt` | `type notas.txt` |
| Ver as 5 primeiras linhas | `head -n 5 dados.csv` | `Get-Content dados.csv -TotalCount 5` | `more dados.csv` (paginado, `q` sai) |
| Copiar arquivo | `cp a.txt b.txt` | `cp a.txt b.txt` | `copy a.txt b.txt` |
| Copiar pasta | `cp -r origem destino` | `cp -Recurse origem destino` | `xcopy origem destino /E /I` |
| Mover ou renomear | `mv a.txt b.txt` | `mv a.txt b.txt` | `move a.txt b.txt` |
| Apagar arquivo | `rm a.txt` | `rm a.txt` | `del a.txt` |
| Apagar pasta e o que tem dentro | `rm -r pasta` | `rm -Recurse pasta` | `rmdir /s /q pasta` |
| Limpar a tela | `clear` | `cls` | `cls` |
| Abrir a pasta no gerenciador de arquivos | `xdg-open .` (Linux), `open .` (macOS), `explorer .` (Git Bash) | `explorer .` | `explorer .` |
| Abrir a pasta no VS Code | `code .` | `code .` | `code .` |

Os comandos de apagar não mandam nada para a lixeira. O arquivo some de vez.

## Procurar, variáveis e saída

| Tarefa | bash | PowerShell | cmd |
| --- | --- | --- | --- |
| Achar arquivos pelo nome | `find . -name "*.csv"` | `Get-ChildItem -Recurse -Filter *.csv` | `dir /s /b *.csv` |
| Procurar um texto dentro dos arquivos | `grep -rn "pandas" .` | `Select-String -Path *.py -Pattern "pandas"` | `findstr /s /n "pandas" *.py` |
| Ver onde está um programa | `which python` | `Get-Command python` | `where python` |
| Ver o PATH | `echo $PATH` | `$env:Path` | `echo %PATH%` |
| Criar uma variável nesta janela | `export NOME=valor` | `$env:NOME = "valor"` | `set NOME=valor` |
| Salvar a saída num arquivo | `ls > lista.txt` | `ls > lista.txt` | `dir > lista.txt` |
| Acrescentar ao fim do arquivo | `ls >> lista.txt` | `ls >> lista.txt` | `dir >> lista.txt` |
| Rodar o segundo só se o primeiro der certo | `cd dados && ls` | `cd dados; ls` | `cd dados && dir` |

O `&&` funciona no PowerShell 7. O Windows PowerShell 5.1, que vem instalado no Windows, não aceita; use `;`, que roda o segundo comando mesmo se o primeiro falhar.

A variável criada com `export`, `$env:` ou `set` some quando você fecha o terminal.

## Git

Os comandos do Git são iguais nos três terminais. Os conceitos (stage, commit, branch, `HEAD`) estão explicados no [README do Git](00_git/README.md).

### Configurar

| Comando | O que faz |
| --- | --- |
| `git config --global user.name "Seu Nome"` | Define o nome que aparece nos commits. |
| `git config --global user.email "voce@exemplo.com"` | Define o e-mail dos commits. Use o da conta do GitHub. |
| `git config --global init.defaultBranch main` | Faz o `git init` criar a branch `main`. |
| `git config --global core.editor "code --wait"` | Usa o VS Code para escrever mensagens de commit. |
| `git config --list` | Mostra a configuração atual. |

### Começar

| Comando | O que faz |
| --- | --- |
| `git init` | Transforma a pasta atual num repositório. |
| `git clone URL` | Baixa um repositório para uma pasta nova. |

### Dia a dia

| Comando | O que faz |
| --- | --- |
| `git status` | Mostra o que mudou e o que está no stage. |
| `git diff` | Mostra as linhas alteradas que ainda não estão no stage. |
| `git diff --staged` | Mostra o que vai entrar no próximo commit. |
| `git add arquivo.py` | Coloca um arquivo no stage. |
| `git add .` | Coloca tudo da pasta atual no stage. |
| `git commit -m "mensagem"` | Registra o que está no stage. |
| `git log --oneline` | Lista os commits, um por linha. |
| `git log --oneline --graph --all` | Desenha as branches e os commits. |
| `git show` | Mostra o último commit com as mudanças. |

### Branches

| Comando | O que faz |
| --- | --- |
| `git branch` | Lista as branches. A atual tem `*`. |
| `git switch -c nome` | Cria uma branch e vai para ela. |
| `git switch main` | Volta para a `main`. |
| `git merge nome` | Traz os commits de `nome` para a branch atual. |
| `git branch -d nome` | Apaga uma branch que já passou por merge. |

### Remoto

| Comando | O que faz |
| --- | --- |
| `git remote -v` | Mostra para onde o repositório envia e de onde baixa. |
| `git push` | Envia seus commits para o GitHub. |
| `git push -u origin nome` | Envia uma branch nova pela primeira vez. |
| `git pull` | Baixa os commits do GitHub e junta com os seus. |
| `git fetch` | Baixa os commits do GitHub sem mexer nos seus arquivos. |

### Desfazer

| Comando | O que faz |
| --- | --- |
| `git restore arquivo.py` | Descarta as alterações do arquivo desde o último commit. Não tem volta. |
| `git restore --staged arquivo.py` | Tira o arquivo do stage e mantém as alterações. |
| `git commit --amend -m "nova mensagem"` | Troca a mensagem do último commit. Use só antes do `git push`. |
| `git revert HASH` | Cria um commit novo que desfaz o commit `HASH`. Serve para commits que já foram para o GitHub. |
| `git stash` | Guarda as alterações de lado e limpa a pasta. |
| `git stash pop` | Traz de volta o que foi guardado. |
| `git rm -r --cached .venv` | Para de acompanhar uma pasta que entrou no Git por engano. Os arquivos continuam no seu disco. |

O `HASH` é o código que aparece no começo de cada linha do `git log --oneline`, como `1a76a7b`.

Se você rodar `git commit` sem o `-m`, o Git abre um editor para a mensagem, geralmente o Vim. Para sair: aperte `Esc`, digite `:wq` e Enter para salvar, ou `:q!` e Enter para cancelar o commit.

## GitHub CLI

Iguais nos três terminais.

| Comando | O que faz |
| --- | --- |
| `gh auth login` | Entra na sua conta. |
| `gh auth status` | Mostra com qual conta você está logado. |
| `gh repo clone usuario/repo` | Clona um repositório do GitHub. |
| `gh repo create meu-projeto --private --source=. --push` | Cria o repositório no GitHub a partir da pasta atual e envia os commits. |
| `gh browse` | Abre o repositório atual no navegador. |
| `gh repo list` | Lista os seus repositórios. |
| `gh pr create` | Abre um pull request da branch atual. |
| `gh pr list` | Lista os pull requests abertos. |
| `gh issue list` | Lista as issues abertas. |

## uv

Iguais nos três terminais, menos a ativação.

| Comando | O que faz |
| --- | --- |
| `uv venv` | Cria o `.venv` na pasta atual. |
| `uv venv --python 3.12` | Cria o `.venv` com o Python 3.12. Baixa essa versão se precisar. |
| `uv pip install pandas` | Instala um pacote no `.venv`. |
| `uv pip install -r requirements.txt` | Instala os pacotes de uma lista. |
| `uv pip list` | Mostra os pacotes instalados. |
| `uv pip freeze > requirements.txt` | Salva a lista de pacotes com as versões. |
| `uv pip uninstall pandas` | Remove um pacote. |
| `uv run python script.py` | Roda um script com o Python do `.venv`, sem ativar. |
| `uv python list` | Mostra as versões do Python disponíveis. |
| `uv self update` | Atualiza o `uv`. |

Ativar e desativar o `.venv` da pasta atual:

| | bash (Linux e macOS) | bash (Git Bash) | PowerShell | cmd |
| --- | --- | --- | --- | --- |
| Ativar | `source .venv/bin/activate` | `source .venv/Scripts/activate` | `.venv\Scripts\activate` | `.venv\Scripts\activate` |
| Desativar | `deactivate` | `deactivate` | `deactivate` | `deactivate` |

Se o PowerShell recusar a ativação, veja a seção [Ativar o ambiente](../README.md#ativar-o-ambiente) do README principal.

## Jupyter

No terminal, com o `.venv` ativo:

| Comando | O que faz |
| --- | --- |
| `jupyter lab` | Abre o Jupyter Lab no navegador. |
| `jupyter lab --port 8889` | Abre em outra porta, se a 8888 estiver ocupada. |
| `jupyter server list` | Mostra os servidores abertos e o endereço de cada um. |
| `Ctrl + C` duas vezes | Fecha o servidor. |

Dentro do notebook:

| Atalho | O que faz |
| --- | --- |
| `Shift + Enter` | Roda a célula e vai para a próxima. |
| `Ctrl + Enter` | Roda a célula e fica nela. |
| `Esc` | Sai da edição da célula. Os atalhos abaixo funcionam nesse modo. |
| `Enter` | Volta a editar a célula. |
| `A` / `B` | Cria uma célula acima / abaixo. |
| `M` / `Y` | Transforma a célula em Markdown / código. |
| `D`, `D` | Apaga a célula. |
| `Z` | Desfaz a última operação com células. |
| `Tab` | Completa nomes de variáveis, funções e colunas. |
| `Shift + Tab` | Mostra a documentação da função onde está o cursor. |

## Para consultar depois

- [Pro Git em português](https://git-scm.com/book/pt-br/v2): o livro oficial do Git, de graça.
- [Git cheat sheet do GitHub](https://education.github.com/git-cheat-sheet-education.pdf): uma página com os comandos principais, em PDF.
- [Manual do GitHub CLI](https://cli.github.com/manual/): todos os comandos do `gh`.
- [Documentação do uv](https://docs.astral.sh/uv/)
- [explainshell.com](https://explainshell.com/): cole um comando de bash e ele explica cada parte.
- [SS64](https://ss64.com/): referência de comandos de bash, PowerShell e cmd.
