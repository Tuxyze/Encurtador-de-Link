# 🔗 Encurtador de URLs

Projeto full stack simples de encurtador de links feito com Flask + SQLite + HTML + JavaScript.

Transforma URLs longas em códigos curtos e permite redirecionamento automático.

---

# 🚀 Demonstração

Cole uma URL no sistema → ele gera um link curto → ao acessar o link você é redirecionado automaticamente.

Exemplo:

https://seu-dominio.com/Ab12Xy

---

# 🛠️ Tecnologias utilizadas

- Python (Flask)
- SQLite
- Flask-CORS
- HTML5
- CSS3
- JavaScript (Fetch API)

---

# 📦 Como rodar localmente

## 1. Clonar o repositório
git clone https://github.com/Tuxyze/Encurtador-de-Link.git
cd Encurtador-de-Link

## 2. Criar ambiente virtual (opcional)
python -m venv venv

Ativar no Windows:
venv\Scripts\activate

Ativar no Linux/Mac:
source venv/bin/activate

## 3. Instalar dependências
pip install -r requirements.txt

## 4. Rodar o projeto
python app.py

## 5. Acessar no navegador
http://localhost:5000

---

# ⚙️ Como funciona

1. Usuário envia uma URL
2. Backend gera um código único
3. Código é salvo no SQLite
4. Acessando /<codigo> ocorre redirecionamento automático

---

# 📁 Estrutura do projeto

Encurtador-de-Link/
├── app.py
├── database.db
├── index.html
├── script.js
├── requirements.txt

---

# 🌐 API

## POST /shorten
Body:
{
  "url": "https://google.com"
}

Resposta:
{
  "code": "aB12xZ",
  "short_url": "http://localhost:5000/aB12xZ"
}

---

## GET /<code>
Redireciona para a URL original.

---

# ⚠️ Observações

- Banco SQLite local (database.db)
- Ideal para estudo e portfólio
- Para produção, usar banco externo (PostgreSQL/MySQL)
- Deploy pode ser feito em plataformas como Render

---

# 💡 Melhorias futuras

- Contador de cliques
- Histórico de URLs
- Login de usuários
- Expiração de links
- Dashboard

---

# 👨‍💻 Autor

Feito por Juan 
Projeto full stack para aprendizado e portfólio
