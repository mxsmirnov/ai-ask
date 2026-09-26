---
name: y-statement
description: Documents architecture decisions as Y-Statement ADRs (Architecture Decision Records). Use when the user asks for ADR, architecture decision record, Y-statement, y-statement, архитектурное решение, запись решения, why we chose X and rejected Y, or to capture context, forces, decision, rejected alternatives, goal, and trade-offs in one sentence
---

# Y-Statement ADR

Пиши Architecture Decision Record в формате Y-Statement: одно предложение из шести частей по шаблону. Не добавляй секции Status, Context, Consequences и прочее — только заголовок и Y-Statement.

## Порядок работы

1. Выдели из источника шесть частей Y-Statement.
2. Если данных для части нет, поставь `—`. Ничего не выдумывай.
3. Сформируй ADR.
4. Если есть прочерки, после Y-Statement добавь `## Задачи на доработку` с одной задачей на каждый прочерк.
5. Если прочерков нет, секцию задач не добавляй.

## Формат

```markdown
# ADR-NNNN: {title}

## Y-Statement

`В контексте` {контекст или —}, `сталкиваясь с` {проблема или —}, `мы решили` {решение или —} `и отвергли` {альтернативы или —}, `чтобы` {цель или —}, `принимая` {компромисс или —}.
```

При пропусках добавь:

```markdown
## Задачи на доработку

- [ ] Уточнить {часть}: {каких данных не хватает}.
```

## Правила

- Y-Statement — одно предложение.
- Порядок маркеров фиксирован.
- Используй только сведения из источника.
- Каждый пропуск обозначай `—`.
- Каждому `—` соответствует одна задача.
- При полном Y-Statement секции задач нет.
- Не добавляй Status, Context и Consequences.
