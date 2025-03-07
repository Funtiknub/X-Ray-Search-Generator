# X-Ray Search Generator

Инструмент для создания сложных поисковых запросов с использованием техники X-Ray поиска Google. Программа помогает формировать эффективные поисковые запросы для поиска работников, вакансий, проектов на GitHub и профилей на LinkedIn.

## Установка и запуск

1. Убедитесь, что установлен Python 3.x
2. Скачайте файл `xray_search.py`
3. Запустите в терминале:

```bash
python x-ray_search.py
```

или:

```bash
py x-ray_search.py
```

## Руководство по использованию

При запуске программы вы увидите главное меню:

=== X-Ray Search Generator ===

1. Создать поисковый запрос
2. Поиск работников/вакансий
3. Специальный поиск по GitHub
4. Специальный поиск по LinkedIn
5. Информация о операторах
6. Выход

## Основные возможности

1. Создание поисковых запросов
2. Поиск работников/вакансий
3. Специальный поиск по GitHub
4. Специальный поиск по LinkedIn
5. Справочная информация по операторам

## Подробное руководство

### 1. Создание поисковых запросов

Базовый поиск с возможностью добавления различных операторов.

**Пример использования:**

1. Выберите "1. Создать поисковый запрос"
2. Введите "python developer"
3. Выберите "1. Добавить ограничение по сайту"
4. Введите "github.com"
5. Выберите "2. Добавить параметр URL"
6. Введите "projects"
7. Выберите "5. Завершить и показать результат"

Результат:
```bash
site:github.com/ inurl:projects python developer
```

### 2. Поиск работников/вакансий

Специализированный поиск по сайтам с вакансиями и резюме. Доступны следующие категории сайтов:

#### Работные сайты:
- hh.ru
- superjob.ru
- rabota.ru
- zarplata.ru
- career.habr.com
- job.ru
- trudvsem.ru
- avito.ru
- indeed.com

#### Профессиональные сети:
- linkedin.com
- ru.linkedin.com
- vk.com/resume
- facebook.com/jobs
- moikrug.ru
- github.com

#### Фриланс площадки:
- freelance.ru
- fl.ru
- freelancehunt.com
- kwork.ru
- weblancer.net

#### Специализированные IT:
- career.habr.com
- stackoverflow.com/jobs
- djinni.co
- getmatch.ru
- hexlet.io/jobs
- geeklink.io
- github.io

**Пример поиска вакансий:**

1. Выберите "2. Поиск работников/вакансий"
2. Выберите "2. Поиск вакансий"
3. Введите должность на русском: "Python разработчик"
4. Введите должность на английском: "Python Developer"
5. Выберите категории сайтов: 1,4 (Работные сайты и Специализированные IT)
6. Выберите город: Москва
7. Добавьте уровень: middle

Результат:
```bash
site:hh.ru OR site:superjob.ru OR site:career.habr.com OR site:geeklink.io Python разработчик OR Python Developer Москва middle
```

### 3. Специальный поиск по GitHub

Позволяет искать на GitHub с исключением служебных страниц.

**Пример поиска:**

1. Выберите "3. Специальный поиск по GitHub"
2. Выберите "1. Чистый поиск"
3. Введите: python api

Результат:
```bash
site:github.com/ python api -inurl:topics|issues|projects|exchange|repositories|trending
```

### 4. Специальный поиск по LinkedIn

Варианты поиска на LinkedIn:
- Поиск OpenToWork профилей
- Поиск вакансий
- Поиск профилей людей
- Поиск в постах
- Поиск компаний

**Пример поиска OpenToWork профилей:**

1. Выберите "4. Специальный поиск по LinkedIn"
2. Выберите "1. Поиск людей открытых к работе"
3. Введите: java developer

Результат:
```bash
site:linkedin.com/ inurl:opentowork-activity java developer
```

**Пример поиска в постах:**

1. Выберите "4. Специальный поиск по LinkedIn"
2. Выберите "4. Поиск в постах"
3. Введите: резюме java

Результат:
```bash
site:linkedin.com/posts резюме java
```

## Операторы поиска и их использование

Основные операторы:

| Оператор | Описание | Пример |
|----------|----------|--------|
| `site:` | Поиск на конкретном сайте | `site:github.com python` |
| `inurl:` | Поиск в URL страницы | `site:linkedin.com/ inurl:opentowork` |
| `intitle:` | Поиск в заголовке | `intitle:python developer` |
| `filetype:` | Поиск по типу файла | `filetype:pdf python tutorial` |
| `-` | Исключение слова/фразы | `python -django` |
| `OR` или `\|` | Логическое ИЛИ | `python OR java developer` |

## Примеры готовых запросов

### 1. Поиск резюме Java разработчиков в Москве:
```bash
site:hh.ru OR site:linkedin.com Java Developer OR Java разработчик Москва senior
```

### 2. Поиск Python проектов на GitHub:
```bash
site:github.com/ machine learning inurl:python -inurl:issues
```

### 3. Поиск DevOps специалистов на LinkedIn:
```bash
site:linkedin.com/ inurl:opentowork-activity DevOps Engineer
```

### 4. Поиск 1C разработчиков:
```bash
site:hh.ru OR site:superjob.ru 1C разработчик OR 1C программист Москва
```

### 5. Поиск стажировок:
```bash
site:hh.ru OR site:career.habr.com стажер OR стажировка OR intern OR internship python
```

## Рекомендации по эффективному использованию

1. Используйте русские и английские варианты ключевых слов
2. Комбинируйте разные сайты через оператор OR
3. При поиске на LinkedIn добавляйте `inurl:opentowork-activity`
4. Для GitHub исключайте служебные разделы через `-inurl:`
5. Указывайте город и уровень специалиста для точности
6. Используйте операторы `site:` и `inurl:` для конкретных разделов сайтов

## Ограничения и особенности

1. Google может ограничивать слишком сложные запросы
2. Некоторые сайты могут блокировать автоматизированный поиск
3. Результаты могут различаться в зависимости от региона
4. Учитывайте правила использования сайтов при поиске

## Лицензия

MIT License