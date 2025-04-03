# Ilumeo - Desafio

## 🔍 Visão Geral
Este projeto resolve o desafio proposto pela Ilumeo, focando na **evolução temporal da taxa de conversão por canal** com base em dados massivos de campanhas de envio (email, WhatsApp, push, etc).

> ⭐ O desafio inclui backend otimizado, frontend interativo e ambiente dockerizado para execução.

---

## 📄 Tecnologias Utilizadas

| Camada      | Tecnologia        |
|-------------|-------------------|
| Backend     | FastAPI (Python)  |
| Banco de Dados | PostgreSQL     |
| Frontend    | React + Vite      |
| Gráfico     | Recharts          |
| API Client  | Axios             |
| Testes API  | Pytest            |
| Docker      | Compose + Dockerfiles |

---

🚀 Como Rodar o Projeto

🛠️ Backend + Banco via Docker

Clone o repositório e entre na pasta:

git clone <repo>
cd ilumeo-desafio

⚠️ IMPORTANTE SOBRE O init.sql:

O arquivo original fornecido pela Ilumeo contém milhões de registros e possui mais de 300MB. Por isso, ele não está versionado no repositório.

Antes de subir os containers, adicione manualmente todos os INSERTs fornecidos no desafio dentro do arquivo docker/init.sql, na linha indicada entre os comentários:

-- Início do código do sql
  (Cole todos os INSERTs aqui)
-- Final do código do arquivo sql

Suba os containers:

docker-compose up --build

Acesse a API em:

http://localhost:8000/docs

💾 Importante: todo o conteúdo do banco de dados fornecido pela Ilumeo está no arquivo docker/init.sql. Ele é executado automaticamente ao subir o banco via Docker.

### 🚀 Frontend (fora do Docker)

1. Entre na pasta do frontend:
   ```bash
   cd ilumeo-dashboard
   npm install
   npm run dev
   ```

2. Acesse no navegador:
   - [http://localhost:5173](http://localhost:5173)

> Obs: O frontend comunica com a API em `localhost:8000`. Certifique-se que a API está rodando.

---

## 💡 Como Rodar os Testes da API

1. Ative o ambiente virtual:
   ```bash
   .\venv\Scripts\Activate
   ```

2. Execute os testes definindo variáveis:
   ```bash
   $env:DB_NAME="ilumeo_db"; $env:DB_USER="ilumeo"; $env:DB_PASS="ilumeo123"; $env:DB_HOST="localhost"; $env:DB_PORT="5432"; pytest
   ```

> Todos os testes estão em `backend/tests/test_api.py`

---

## 📊 Funcionalidades

- [x] Rota `/conversao/` retorna a taxa de conversão por dia e canal
- [x] Filtros por canal, data inicial e final
- [x] Dashboard com gráfico de linhas interativo
- [x] Testes automatizados com pytest
- [x] Banco com mais de 3.8 milhões de registros populado via SQL

---

## 🔧 Estrutura das Pastas

```
ilumeo-desafio/
├── backend/
│   ├── main.py
│   ├── routers/
│   │   └── conversao.py
│   ├── tests/
│   │   └── test_api.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── venv/
├── docker/
│   └── init.sql
├── ilumeo-dashboard/
│   ├── src/components/ConversionChart.jsx
│   ├── App.jsx
│   └── ...
└── docker-compose.yml
```

---

## 📈 Otimizações e Decisões

- Utilização de **filtros SQL dinâmicos** no backend (WHERE 1=1 + params)
- Conversão apenas quando `response_status_id = 6` (Visualizou)
- Banco populado em `init.sql`, indexado
- Frontend fora do Docker para manter performance no dev

---

## 📅 Autor

Desenvolvido para o desafio Ilumeo por [Gabriel Carvalho].

