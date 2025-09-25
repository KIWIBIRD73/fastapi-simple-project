# 🚀 Быстрый старт с FastAPI

Этот гайд поможет шаг за шагом настроить окружение и запустить первое приложение на **FastAPI**

---

## 📌 Установка VS Code

1. Скачайте [Visual Studio Code](https://code.visualstudio.com/).
2. Установите его.

---

## 📌 Установка Python

### macOS

1. Скачайте последнюю версию Python с [официального сайта](https://www.python.org/downloads/).
2. Установите его (обычно автоматически ставится в `/usr/local/bin/python3`).
3. Проверьте установку в `terminal.app (терминал.app)`:

   ```bash
   python3 --version
   ```

### Windows

1. Скачайте установщик Python с [официального сайта](https://www.python.org/downloads/windows/).
2. При установке обязательно отметьте галочку **"Add Python to PATH"**.
3. Проверьте установку в `Power Shell`, тот который с синей иконкой:

   ```powershell
   python --version
   ```

---

## 📌 Установка расширений VS Code

В VS Code откройте вкладку **Extensions** (или нажмите `Ctrl+Shift+X` / `Cmd+Shift+X`) и установите:

* **[Python (Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)**
* **[Python Environment Manager](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-python-envs)**
* **[autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)**
* **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)**

---

## 📌 Создание проекта

1. Создайте папку на рабочем столе:

2. Откройте её в VS Code:

   * В VS Code → **File** → **Open Folder** → выберите созданную папку.

---

## 📌 Создание виртуального окружения

### macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### Или через установленное расширение
- Нажать сочетание клавиш `Ctrl+Shift+P` / `Cmd+Shift+P`
- Написать в появившейся строке `>Python: Create Environment...`
- Выбрать появившуюся команду
- Продолжить шаги с предложенным выбором
- Открыть консоль `` Alt+` `` / `` Ctrl+` `` или в панели **Terminal** → **New terminal**

После активации в начале командной строки вы увидите `(venv)`.

---

## 📌 Установка FastAPI и Uvicorn

В активированном окружении установите нужные пакеты:

```bash
pip install fastapi uvicorn
```

---

## 📌 Пример приложения

Создайте файл `main.py` в папке проекта и вставьте код:

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_hello():
    return {"message": "Hello from FastApi!"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
```

---

## 📌 Запуск приложения

* В терминале выполните:

  ```bash
  python -m main
  ```

* (Дополнительно) Если основной фаил для запуска приложения находится в другой папке, например:

  ```bash
  └── 📁api-python
      └── 📁src
          ├── main.py
      └── README.md
  ```

  То нужно указывать путь следующим образом:

  ```bash
  python -m src.main
  ```

  Также необходимо указать и нужный путь для `uvicorn` в `src/main.py` файле
  ```py
  if __name__ == '__main__':
    """
    Для запуска через uvicorn необходимо указать путь до основного объекта приложения FastApi

    src - папка, в котрой лежит main фаил
    main - имя файла (main.py)
    app - объект приложения FastApi()

    Путь до файла указывать через точку, путь до объекта FastApi() указывать через двоеточие
    """
    uvicorn.run('src.main:app', reload=True)
  ```


---

## 📌 Проверка работы

После запуска вы увидите сообщение вида:

```
Uvicorn running on http://127.0.0.1:8000
```

Откройте в браузере:

* [http://127.0.0.1:8000](http://127.0.0.1:8000) → ваше приложение
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → Swagger UI (документация)
* [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) → альтернативная документация

---

## 🎉 Поздравляем!

Вы успешно создали и запустили своё первое приложение на **FastAPI**!

---

## 🔄 Повторный запуск проекта

При следующем открытии проекта в VS Code, нужно учесть несколько моментов.

---

### 📌 Зафиксируйте зависимости и версию Python

Чтобы проект всегда запускался одинаково:

1. Сохраните зависимости:

   ```bash
   pip freeze > requirements.txt
   ```

2. При необходимости укажите версию Python в `.python-version` или просто запишите её в `README.md`. Узнать версию python можно через команду:
    ```
    python --version
    ```
    PЗапишите вывод из консоли в фаил `.python-version`, например `Python 3.11.13`

3. В будущем можно восстановить окружение:

   ```bash
   pip install -r requirements.txt
   ```

---

### 📌 Сценарий 1. `.venv` не удалён

Если папка `.venv` осталась:

1. Активируйте виртуальное окружение:

   * macOS / Linux:

     ```bash
     source venv/bin/activate
     ```
   * Windows (PowerShell):

     ```powershell
     .\venv\Scripts\activate
     ```

2. Убедитесь, что в терминале появилось `(venv)` в начале строки.

3. Запустите приложение. [Перейти к разделку "📌 Запуск приложения"](#-запуск-приложения)

---

### 📌 Сценарий 2. `.venv` был удалён

Если папка окружения потерялась или была удалена:

1. Создайте новое окружение. [Перейти к разделу "📌 Создание виртуального окружения"](#-создание-виртуального-окружения)

2. Установите зависимости из `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Запустите приложение снова. [Перейти к разделку "📌 Запуск приложения"](#-запуск-приложения)

---

### 📌 Рекомендации

* Если VS Code не подхватывает `venv`, нажмите **Ctrl+Shift+P** → **Python: Select Interpreter** и выберите интерпретатор из папки `venv`.
* Всегда фиксируйте зависимости в `requirements.txt` перед тем как удалять или переносить окружение.


## 🔗 Полезные ссылки
* [Конфигурация VS Code для работы с Python](https://www.youtube.com/watch?v=D2cwvpJSBX4)
* [Объяснение базовых концептов Python](https://www.youtube.com/watch?v=Gx5qb1uHss4)
* [Запуск проекта через Poetry](https://python-poetry.org/docs/cli/#run)
* [Пакетный менеджер Poetry](https://python-poetry.org)
* [Про Poetry](https://www.youtube.com/watch?v=Ji2XDxmXSOM)