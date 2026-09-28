---
type: Domain Concept
title: Плательщик в Billing
description: Сторона, обязанная оплатить счёт.
tags: [billing, payer]
status: stable
generated:
  by: human:example-author
  at: 2026-09-28T11:45:00+03:00
---

# Определение

Плательщик — сторона, на которую выставлен [счёт](/billing/invoice.md). Billing хранит её идентификатор и реквизиты, необходимые для оплаты.

# Связь контекстов

При создании счёта плательщик может быть определён из данных [покупателя Ordering](/ordering/customer.md), но совпадение не гарантируется. Правило сопоставления указано на [карте контекстов](/context-map.md).
