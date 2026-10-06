# Visualização de dados com matplotlib e seaborn

Na pasta `2_visualizacao`, no PowerShell ou no cmd:

```bat
uv venv
.venv\Scripts\activate
uv pip install jupyterlab pandas numpy matplotlib
jupyter lab
```

Se o PowerShell bloquear a ativação, rode uma vez e ative de novo:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
## Matplotlib

- Ferramenta construida em cima do numpy para plotar no estilo MATLAB no console IPython CLI.
- Muito utilizado na atualidade pois suporta varios SO's e motores graficos. 
- Seaborn, pandas e outros tem suas ferramentas de visualizacao de dados construida em cima do matplotlib. 

- pyplot (`plt`) é a interface para visualização sem entrar no mérito do back-end. 
`import matplotlib.pyplot as plt`
 
https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
`In[2]: plt.style.use('classic')`

### plt.show()

#### Scripts
  - `plt.show()` começa um _event loop_, vai abrir uma janela interativa que mostra a figura. 
  
#### IPython CLI

```shell
uv venv 
source venv/bin/actitvate 
uv pip install ipython matplotlib pyqt6
```

- IPython Notebook
```shell
uv add jupyterlab ipympl
uv run jupyter lab
```

```python
%matplotlib widget
import matplotlib.pyplot as plt 
```

