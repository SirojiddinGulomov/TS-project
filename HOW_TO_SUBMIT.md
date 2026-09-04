# Пошаговая сдача через GitHub

## Вариант без Git в терминале

1. Зайдите на https://github.com/
2. Нажмите **New repository**.
3. Repository name: `time-series-final-project`
4. Выберите **Public**.
5. Нажмите **Create repository**.
6. Распакуйте ZIP, который дал ChatGPT.
7. На странице пустого репозитория нажмите **uploading an existing file**.
8. Перетащите ВСЁ содержимое папки `timeseries-final-project`.
9. Commit message: `Final time series project`.
10. Нажмите **Commit changes**.

## Запуск

1. На GitHub откройте `notebooks/final_timeseries_project.ipynb`.
2. Нажмите **Open in Colab**, если кнопка доступна.  
   Если её нет: откройте https://colab.research.google.com/ → GitHub → вставьте URL репозитория.
3. Выполните **Runtime → Run all**.
4. После завершения: **File → Save a copy in GitHub**.
5. Выберите свой репозиторий и перезапишите notebook или сохраните обновлённую копию.

## Что отправить преподавателю

Основная ссылка:

`https://github.com/ВАШ_ЛОГИН/time-series-final-project`

Можно дополнительно отправить прямую ссылку на notebook.

## Перед отправкой

Убедитесь, что GitHub показывает:
- README;
- notebooks/final_timeseries_project.ipynb;
- src/pipeline.py;
- requirements.txt;
- источник датасета;
- outputs графиков и таблиц внутри notebook после Run all.
