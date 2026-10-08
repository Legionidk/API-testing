# Установка

```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest tests
```

# Результаты

`1 failed, 7 passed`

### Ошибки

`test_query()` в `tests/test_get_posts.py` - ошибка из-за (как мне кажется) некорректной обработки query-параметров самой API. [В документации описано](https://dummyjson.com/docs/posts#posts-search), что через `?q={something}` можно искать посты по ключевому слову, но по факту, он возвращает как посты с этим словом, так и рандомные посты, которые под поиск попадать не должны.
