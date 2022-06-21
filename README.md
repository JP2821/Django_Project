# Estoque
Um projeto para controle de estoque básico

## Como rodar o projeto ?

* Clone o repositório.
* Crie um virtualenv com Python.
* Ativa a virtualenv.
* Instale as dependências.
* Rode as migrations.

```
git clone https://github.com/JP2821/Django_Project.git
cd estoque
python -m venv venv
.\venv\Scripts\Activate.ps1 (Para PowerShell)
.\venv\Scripts\Activate.bat (Para cmd)
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```
