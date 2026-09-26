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

Используй `assets/adr-template.md` как точную структуру ADR.

- Не меняй структуру шаблона.
- Заполняй шаблон только сведениями из источника или `—`.
- Если есть пропуски, в `{tasks_section}` добавь `## Задачи на доработку` с одной задачей на каждый пропуск.
- Если пропусков нет, `{tasks_section}` оставь пустым.

## Правила

- Y-Statement — одно предложение.
- Порядок маркеров фиксирован.
- Используй только сведения из источника.
- Каждый пропуск обозначай `—`.
- Каждому `—` соответствует одна задача.
- При полном Y-Statement секции задач нет.
- Не добавляй Status, Context и Consequences.
