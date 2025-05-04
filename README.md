# 📘 Learning Log

**Learning Log** é uma aplicação web desenvolvida em **Django**, com o objetivo de ajudar usuários a registrar e organizar anotações relacionadas aos seus estudos.  

---

## 🚀 Tecnologias Utilizadas

- **[Django](https://www.djangoproject.com/)** – framework web Python de alto nível.
- **[Tailwind CSS](https://tailwindcss.com/)** – framework CSS utilitário para estilização moderna e responsiva.
- **SQLite3** – banco de dados leve e integrado ao Django por padrão, ideal para desenvolvimento local.

---

## ⚙️ Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/cassiusdbrito/LearningLog
cd learning_log
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Aplique as migrações:

```bash
python manage.py migrate
```

5. Rode o servidor local:

```bash
python manage.py runserver
```

6. Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## 📂 Estrutura do Projeto

- `learning_log/` – configuração principal do projeto Django.
- `LLog/` – app principal da aplicação com os modelos e views.
- `users/` – gerenciamento de autenticação de usuários (login, registro).
- `templates/` – templates HTML utilizando Tailwind CSS.
- `db.sqlite3` – banco de dados SQLite usado para armazenar os dados localmente.

---

## 👤 Autor

Desenvolvido por **Cassius Duarte**
