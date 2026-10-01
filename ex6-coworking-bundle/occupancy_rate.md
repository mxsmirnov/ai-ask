---
type: Metric
title: Загруженность коворкинга (Occupancy Rate)
description: Процент занятых столов от общего фонда.
status: stable
---

# Расчет загруженности

При запросах вида *"Какая сейчас загрузка?"* ИИ должен использовать этот шаблон:

```sql
SELECT 
  (COUNT(DISTINCT b.desk_id) * 100.0) / (SELECT COUNT(*) FROM desks) AS current_occupancy_percentage
FROM 
  bookings b
WHERE 
  b.started_at <= CURRENT_TIMESTAMP 
  AND (b.ended_at IS NULL OR b.ended_at >= CURRENT_TIMESTAMP);
```
