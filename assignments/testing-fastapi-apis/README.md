# 📘 Atividade: Testando APIs com FastAPI e Pytest

## 🎯 Objetivo

Escreva testes automatizados para uma API REST com FastAPI usando Pytest e TestClient. Você praticará como verificar respostas, códigos HTTP, validação de dados e tratamento de erros sem iniciar um servidor web.

## 📝 Tarefas

### 🛠️ Preparar o ambiente e executar o teste inicial

#### Descrição
Instale as dependências e execute o teste de exemplo fornecido em `test_api.py` para conhecer o TestClient e a fixture que restaura os dados antes de cada teste.

Use os comandos:

```bash
python -m pip install fastapi uvicorn httpx2 pytest
pytest -q
```

#### Requisitos
O programa concluído deve:

- Executar o teste inicial sem iniciar o servidor com Uvicorn.
- Usar `TestClient` para enviar uma requisição à aplicação FastAPI.
- Confirmar que `GET /books` retorna status HTTP `200` e uma lista com os livros iniciais.
- Manter o estado dos dados isolado entre testes usando a fixture fornecida.

### 🛠️ Testar operações bem-sucedidas

#### Descrição
Adicione testes para consultar um livro, criar um livro e atualizar um livro existente. Faça as requisições com o TestClient e verifique as respostas retornadas pela API.

#### Requisitos
O programa concluído deve:

- Testar `GET /books/{book_id}` e confirmar os dados do livro encontrado.
- Testar `POST /books` com título e autor e confirmar o status HTTP `201` e o livro criado.
- Testar `PUT /books/{book_id}` e confirmar que os dados do livro foram atualizados.
- Verificar os códigos HTTP e os campos importantes dos corpos de resposta.

### 🛠️ Testar validação, erros e remoção

#### Descrição
Complete a suíte testando entradas inválidas, identificadores inexistentes e a remoção de livros. Execute todos os testes em conjunto e confira que cada um pode ser repetido de forma independente.

#### Requisitos
O programa concluído deve:

- Confirmar que um corpo de requisição sem os campos obrigatórios é rejeitado com status HTTP `422`.
- Confirmar que consultar, atualizar ou remover um identificador inexistente retorna status HTTP `404`.
- Testar `DELETE /books/{book_id}` e confirmar status HTTP `204` e que o livro não pode mais ser consultado.
- Executar a suíte completa com `pytest -q` sem falhas.
