# Просто болтаем с моделью
## Запрос
```json
{
  "model": "gpt-4o",
  "messages": [
    { "role": "system", "content": "Ты — вежливый и лаконичный ИИ-ассистент." },
    { "role": "user", "content": "Привет! Какая погода в Москве?" },
    { "role": "assistant", "content": "Привет! У меня нет доступа к реальному времени без инструментов." },
    { "role": "user", "content": "Ой, извини. А в Питере какая?" }
  ]
}
```
## Ответ
```json
{ "role": "assistant", "content": "Для Санкт-Петербурга ситуация аналогичная — мне нужны актуальные данные." }
```
# Передаем запрос и описание инструмента
## Запрос
```json
{
  "model": "gpt-4o",
  "messages": [
    { "role": "system", "content": "Ты — лаконичный ассистент." },
    { "role": "user", "content": "Какая сейчас погода в Москве?" }
  ],
  "tools": [{
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Получить текущую погоду в городе",
      "parameters": {
        "type": "object",
        "properties": { "location": { "type": "string" } },
        "required": ["location"]
      }
    }
  }]
}
```
## Ответ
```json
{ 
  "role": "assistant", 
  "content": null, 
  "tool_calls": [{ 
    "id": "call_abc123", 
    "type": "function", 
    "function": { "name": "get_weather", "arguments": "{\"location\":\"Москва\"}" } 
  }] 
}
```

# Передаем результат вызова инструмента
## Запрос
```json
{
  "model": "gpt-4o",
  "messages": [
    { "role": "system", "content": "Ты — лаконичный ассистент." },
    { "role": "user", "content": "Какая сейчас погода в Москве?" },
    { 
      "role": "assistant", "content": null, 
      "tool_calls": [{ 
        "id": "call_abc123", "type": "function", 
        "function": { "name": "get_weather", "arguments": "{\"location\":\"Москва\"}" } 
      }] 
    },
    { "role": "tool", "tool_call_id": "call_abc123", "content": "{\"temp\":\"+18°C\",\"cond\":\"ясно\"}" }
  ]
}
```
## Ответ
```json
{ "role": "assistant", "content": "В Москве сейчас +18°C, ясно." }
```

# Диаграмма взаимодействия

```mermaid
sequenceDiagram
    autonumber
    participant U as Пользователь
    participant C as Клиент / приложение
    participant API as Chat Completions API (gpt-4o)
    participant T as Инструмент get_weather

    Note over U,API: Обычный чат без инструментов

    U->>C: Привет! Какая погода в Москве?
    C->>API: messages: [system, user]
    API-->>C: assistant: "У меня нет доступа к реальному времени без инструментов."
    C-->>U: Привет! У меня нет доступа к реальному времени без инструментов.

    U->>C: Ой, извини. А в Питере какая?
    C->>API: messages + предыдущий диалог
    API-->>C: assistant: "Для Санкт-Петербурга ситуация аналогичная — мне нужны актуальные данные."
    C-->>U: Для Санкт-Петербурга ситуация аналогичная — мне нужны актуальные данные.

    Note over U,T: Сценарий с вызовом инструмента

    U->>C: Какая сейчас погода в Москве?
    C->>API: messages + tools: [get_weather]
    API-->>C: assistant.content = null<br/>tool_calls: get_weather(location="Москва")
    C->>T: Вызов get_weather("Москва")
    T-->>C: результат: temp=+18°C, cond=ясно
    C->>API: messages + assistant.tool_calls + role=tool<br/>tool_call_id="call_abc123"
    API-->>C: assistant: "В Москве сейчас +18°C, ясно."
    C-->>U: В Москве сейчас +18°C, ясно.
```