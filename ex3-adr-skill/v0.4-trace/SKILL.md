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



## Проверка

Перед записью ADR проверь:

- Есть заголовок и `## Y-Statement`.
- Есть все шесть маркеров в правильном порядке.
- Y-Statement состоит из одного предложения.
- Нет выдуманных фактов.
- Каждый отсутствующий факт записан как `—`.
- Каждому `—` соответствует одна задача.
- Если `—` нет, секции задач нет.
- `чтобы` описывает цель, а `принимая` — цену, риск или ограничение, если эти данные есть в источнике.

Исправь найденные ошибки формы. Пропуски не являются ошибкой и не блокируют создание ADR.


## Trace

После создания ADR добавь запись в `trace.md` в корне проекта. Если файла нет, начни его с:

```markdown
# Y-Statement skill trace
```

Для каждого запуска добавь:

```markdown
## {ISO-8601} | y-statement | {ADR-NNNN}

### Source
{использованный источник}

### Reasoning
{максимально полный reasoning trace, доступный в используемом runtime}

### Mapping
- В контексте: PRESENT | MISSING
- сталкиваясь с: PRESENT | MISSING
- мы решили: PRESENT | MISSING
- и отвергли: PRESENT | MISSING
- чтобы: PRESENT | MISSING
- принимая: PRESENT | MISSING

### Validation
PASS | FIXED

### Output
{путь к ADR}
```

В `Reasoning` сохраняй максимально полный reasoning trace, который предоставляет используемая модель или runtime. Если внутренний reasoning недоступен, сохраняй максимально подробный доступный reasoning summary.
