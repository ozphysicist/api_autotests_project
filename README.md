# REST API Testing Framework

## Описание
Фреймворк для тестирования REST API https://api.hh.ru

### Эндпоинты:
- /areas
- /employers

## Использованные технологии: 
python==3.9
allure-pytest==2.13.2
asserts==0.12.0
pydantic==2.4.2
pytest==7.4.4
requests==2.28.2
urllib3==1.26.18

## Запуск автотестов

1. Клонировать репозиторий и перейти в него в командной строке:

```git clone <cсылка на репозиторий github>```

```cd pytest_autotest_project```

2. Cоздать и активировать виртуальное окружение:
```python3 -m venv venv```
- macOS/Linux: ```source venv/bin/activate```
- Wndows: ```source venv/Scripts/activate```

3. Установить зависимости requirements.txt:
- Windows: pip install -r requirements.txt
- MacOS: pip3 install -r requirements.txt

4. Запуск тестов:
- все тесты: ```pytest```
- запуск тестов в конкретном файле: ```pytest tests/test_area.py```
- запуск тестов и создание allure отчета
```pytest --alluredir=./allure-results```
```allure serve allure-results```

## Структура проекта
```
├── base # Директория, содержащие описание базовых классов проекта
    ├──api_client.py # Файл с описание базового api клиента
    ├──base_steps.py # Файл с описание базового класса создание степов
├── services # Директория, содержащая описание тестируемых сервисов
    ├──area # Сервис стран. Директория содержит фикстуры, датаклассы, степы и вспомогательные функции
    ├──employers # Сервис работодателй. Директория содержит фикстуры, датаклассы, степы и вспомогательные функции
├── tests          # Директория с тестовыми кейсами
├── requirements.txt     # Файл с зависимостями проекта
└── vars    # Папка для хранения общих переменных (данных), используемых в проекте
```




