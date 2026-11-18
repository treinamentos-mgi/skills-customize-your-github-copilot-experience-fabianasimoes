# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para administrar um catálogo de livros usando FastAPI. Você praticará métodos HTTP, rotas, validação de dados com modelos e respostas de erro, mantendo os dados em memória.

## 📝 Tarefas

### 🛠️ Criar a aplicação e consultar livros

#### Descrição
Instale as dependências, execute o código inicial e implemente rotas para consultar todos os livros e buscar um livro pelo identificador.

Para iniciar a aplicação, use:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI que possa ser iniciada com Uvicorn.
- Implementar `GET /books` para retornar a lista de livros.
- Implementar `GET /books/{book_id}` para retornar um livro pelo identificador.
- Retornar o status HTTP `404` quando o identificador não existir.

### 🛠️ Adicionar e atualizar livros

#### Descrição
Use o modelo `BookInput` do código inicial para validar os dados enviados pelo cliente e implemente as operações de criação e atualização.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para adicionar um livro com título e autor.
- Gerar um identificador para cada livro criado e retornar o livro criado com status HTTP `201`.
- Implementar `PUT /books/{book_id}` para substituir o título e o autor de um livro existente.
- Retornar status HTTP `404` ao tentar atualizar um identificador inexistente.
- Rejeitar dados que não correspondam ao modelo de entrada.

### 🛠️ Remover livros e testar a API

#### Descrição
Implemente a remoção de livros e teste as rotas pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /books/{book_id}` para remover um livro existente.
- Retornar status HTTP `204` ao remover um livro com sucesso.
- Retornar status HTTP `404` ao tentar remover um identificador inexistente.
- Permitir testar as operações e consultar seus parâmetros e respostas em `http://127.0.0.1:8000/docs`.
