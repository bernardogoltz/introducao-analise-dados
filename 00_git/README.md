# Git

O Git guarda o histórico do projeto. Cada mudança registrada vira um commit, e o GitHub é o lugar onde essa cópia fica na internet.

## Conceitos

**Worktree.** A pasta em que você edita os arquivos agora. O Git compara esses arquivos com o último commit.

**Stage.** A lista do que entra no próximo commit. O `git add` coloca os arquivos aqui.

**Commit.** Um registro do projeto naquele momento, com uma mensagem que explica a mudança.

**Branch.** Um ponteiro para um commit. O nome `main` aponta para o commit mais recente dessa linha.

**HEAD.** O ponteiro de onde você está. Em geral aponta para uma branch, e a branch aponta para um commit.

**Stash.** Guarda alterações de lado, sem fazer commit, para retomá-las depois.

**Remoto.** A cópia do repositório em outro lugar. No GitHub, o remoto padrão se chama `origin`.

## Comandos básicos

Na primeira vez, diga ao Git quem você é:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email"
```

Começar um repositório nesta pasta e ver o que mudou:

```bash
git init
git status
git diff
```

Registrar uma mudança:

```bash
git add .
git commit -m "descreve a mudança"
git log
```

Guardar o trabalho de lado e trazê-lo de volta:

```bash
git stash
git stash pop
```

## HEAD e branches

Uma branch é um nome que aponta para um commit. O `HEAD` aponta para a branch atual. Um commit novo move essa branch para frente, e o `HEAD` acompanha.

```
HEAD -> main -> C -> B -> A
```

Trocar de branch muda o `HEAD`. A worktree passa a mostrar os arquivos do commit para onde aquela branch aponta.

```bash
git switch -c feature
git switch main
git branch
git log --oneline --decorate --graph --all
```

O `--decorate` mostra os ponteiros (`HEAD`, `main`, `feature`) ao lado de cada commit.

Se o `HEAD` apontar direto para um commit, e não para uma branch, ele está detached. Um commit feito aí não fica em branch nenhuma até você criar uma:

```bash
git switch -c salvar-aqui
```

## Merge

O merge traz os commits de uma branch para a branch em que o `HEAD` está.

```bash
git switch main
git merge feature
```

Se a `main` não teve commits novos desde que a `feature` saiu dela, o Git só avança o ponteiro da `main` até o mesmo commit da `feature`. Isso é um fast-forward.

Se as duas andaram, o Git cria um commit de merge com dois pais: a ponta da `main` e a ponta da `feature`. A `main` passa a apontar para esse commit.

## Conflitos

O merge para quando as duas branches mudaram as mesmas linhas. O Git deixa as duas versões no arquivo:

```
<<<<<<< HEAD
versão da branch atual
=======
versão que entrou
>>>>>>> feature
```

`HEAD` é a branch que recebe o merge. O outro lado é a branch que você trouxe. Apague as marcas, deixe o conteúdo certo e feche o merge:

```bash
git add arquivo
git commit
```

Para desistir e voltar ao estado de antes do merge:

```bash
git merge --abort
```

## Criar conta no GitHub

1. Abra [github.com](https://github.com) e escolha **Sign up**.
2. Informe e-mail, senha e um nome de usuário.
3. Confirme o e-mail que o GitHub enviar.
4. Em **New repository**, dê um nome ao repositório e crie. Deixe vazio se o projeto já existe na sua máquina.

## Instalar o gh no Windows

O `gh` é a linha de comando do GitHub. No Windows:

```powershell
winget install --id GitHub.cli
```

Abra um terminal novo para o comando `gh` entrar no PATH.

## Conectar a um repositório remoto

Na primeira vez, entre na conta. O GitHub não aceita a senha do site no `git push`.

```bash
gh auth login
```

Projeto já existe na sua máquina. Troque `USUARIO` e `REPO` pelos seus:

```bash
git remote add origin https://github.com/USUARIO/REPO.git
git branch -M main
git push -u origin main
```

O `-u` liga a branch `main` ao `origin`. Nos próximos envios basta:

```bash
git push
git pull
```

Projeto já existe no GitHub. Baixe uma cópia e trabalhe nela:

```bash
git clone https://github.com/USUARIO/REPO.git
cd REPO
```
