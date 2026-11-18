---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Arquivos Markdown de Tarefas

Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../assignment-template.md).
- A tarefa deve ser criada como um arquivo `README.md`
- Não remova ou pule seções obrigatórias do template.

## 2. Orientação das Seções

Use a mesma estrutura e os mesmos cabeçalhos do template, incluindo os ícones emoji. Como o template está em português, não use os cabeçalhos em inglês.

- `# 📘 Atividade: [Título da Atividade]` — Use um título curto e descritivo, adequado ao conteúdo.
- `## 🎯 Objetivo` — Escreva uma breve descrição do que o aluno aprenderá ou construirá.
- `## 📝 Tarefas` — Para cada tarefa, use `### 🛠️ [Título da Tarefa]` e inclua as subseções:
   - `#### Descrição` — Explique claramente o que o aluno deve fazer.
   - `#### Requisitos` — Liste com marcadores os resultados ou funcionalidades esperados. Seja específico e mensurável.

Inclua exemplos de entrada, saída ou uso em blocos de código quando ajudarem a esclarecer os requisitos. Mantenha a linguagem clara e amigável para os alunos.

Não inclua seções extras a menos que explicitamente especificado.