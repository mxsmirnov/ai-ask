---
type: Table
title: Таблица бронирований (bookings)
description: Хранит сессии аренды столов резидентами.
status: stable
joins:
  - target: desks
    on: bookings.desk_id = desks.id
---

# Схема таблицы `bookings`

* `id` (INT, Primary Key) — номер брони.
* `desk_id` (INT, Foreign Key) — номер стола из таблицы `desks`.
* `started_at` (TIMESTAMP) — начало аренды.
* `ended_at` (TIMESTAMP) — конец аренды (если `NULL` — стол занят прямо сейчас).
