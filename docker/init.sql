CREATE SCHEMA IF NOT EXISTS inside;

CREATE TABLE IF NOT EXISTS inside.users_surveys_responses_aux (
  id BIGINT PRIMARY KEY,
  origin VARCHAR(50),
  response_status_id INT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Início do código do sql

-- Final do código do arquivo sql

-- Simula datas aleatórias (para fins de teste do gráfico)
UPDATE inside.users_surveys_responses_aux
SET created_at = NOW() - (random() * interval '30 days');
