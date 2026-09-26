# Тестирование изменений навыка

Для сравнения версий используй один и тот же `v1.0-final/evals/evals.json` и отдельную LLM-сессию.

## Prompt

```text
Оцени указанную версию Agent Skill как LLM-as-a-judge.

Прочитай её SKILL.md и все файлы, на которые он ссылается, затем v1.0-final/evals/evals.json.
Не изменяй тестируемые файлы.

Для каждого case:
1. Создай минимальный конкретный fixture из input.
2. Выполни тестируемый skill на fixture.
3. Проверь каждый assertion по фактическому результату.
4. Поставь PASS, FAIL или NOT_VERIFIABLE и приведи evidence.

Не ставь PASS только потому, что правило написано в SKILL.md.
Не исправляй результат после выполнения ради прохождения eval.

Создай в каталоге тестируемой версии файл eval-report.md со структурой:

# Evaluation Report
## Summary
## Case: {name}
### Fixture
### Result
### Assertions
### Case result
## Regressions and failure modes
## Conclusion

Case = PASS, только если все assertions получили PASS.
Case = FAIL, если хотя бы один assertion получил FAIL.
Иначе при наличии непроверяемого assertion case = NOT_VERIFIABLE.
```
