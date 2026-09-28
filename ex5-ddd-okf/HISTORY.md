# Сценарий создания LLM Wiki

Вымышленный пример. Время указано для Москвы (UTC+03:00). На каждом шаге создаётся одна содержательная страница; индексы и журналы заводятся при открытии соответствующего каталога и затем обновляются.

| Шаг | Дата и время (MSK) | Созданная страница | Что добавлено и какие служебные файлы изменены |
|---:|---|---|---|
| 1 | 2026-09-27 09:10 | `shop-wiki/context-map.md` | Создана карта контекстов; заведены корневые index.md и log.md. Изменены: корневые index.md, log.md. |
| 2 | 2026-09-27 11:25 | `shop-wiki/ordering/context.md` | Описан Ordering; заведены ordering/index.md и ordering/log.md. Изменены: ordering/index.md, ordering/log.md, корневой log.md. |
| 3 | 2026-09-27 14:40 | `shop-wiki/ordering/customer.md` | Определён покупатель в языке Ordering. Изменены: ordering/index.md, ordering/log.md, корневой log.md. |
| 4 | 2026-09-27 17:05 | `shop-wiki/ordering/order.md` | Описаны корень, операции и инварианты заказа. Изменены: ordering/index.md, ordering/log.md, корневой log.md. |
| 5 | 2026-09-28 09:20 | `shop-wiki/billing/context.md` | Описан Billing; заведены billing/index.md и billing/log.md. Изменены: billing/index.md, billing/log.md, корневой log.md. |
| 6 | 2026-09-28 11:45 | `shop-wiki/billing/payer.md` | Определён плательщик в языке Billing. Изменены: billing/index.md, billing/log.md, корневой log.md. |
| 7 | 2026-09-28 15:10 | `shop-wiki/billing/invoice.md` | Описаны корень, операции и инварианты счёта. Изменены: billing/index.md, billing/log.md, корневой log.md. |
| 8 | 2026-09-28 15:30 | `raw/shop-story.md` | Creation: Добавлена единая исходная история модели и проектные допущения. Запись в корневом журнале. |
| 9 | 2026-09-28 15:40 | `shop-wiki/ordering/context.md` | Update: Заполнен canvas контекста Ordering; обновлён ordering/index.md. Запись в корневом журнале и журнале ordering. |
| 10 | 2026-09-28 15:50 | `shop-wiki/ordering/order.md` | Update: Заполнен canvas Order; добавлены состояния, команды, события и оценки; обновлён ordering/index.md. Запись в корневом журнале и журнале ordering. |
| 11 | 2026-09-28 16:00 | `shop-wiki/billing/context.md` | Update: Заполнен canvas контекста Billing; обновлён billing/index.md. Запись в корневом журнале и журнале billing. |
| 12 | 2026-09-28 16:10 | `shop-wiki/billing/invoice.md` | Update: Заполнен canvas Invoice; уточнена уникальность счёта и обработка повторов; обновлён billing/index.md. Запись в корневом журнале и журнале billing. |
| 13 | 2026-09-28 16:20 | `shop-wiki/context-map.md` | Update: Согласованы контракт OrderConfirmed, ACL Billing и граница внутренних событий. Запись в корневом журнале. |

Шаги 1–7 создают исходные статьи. Шаги 8–13 продолжают вымышленный сценарий: исходный рассказ и обновление по одной содержательной странице за шаг. Индексы и журналы обновляются как служебные файлы. Метки времени и актор process:fictional-canvas-workshop моделируют рабочую сессию, а не реальную проверку. `verified` не заявлен.
