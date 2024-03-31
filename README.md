# Template processor

Скрипт позволяет получить итоговый файл из подготовленных шаблонов с использованием входных данных в формате JSON.

## Installation
**Copy a project**
```
$ git clone git@github.com:Dddarknight/template-processor.git
$ cd template-processor
$ python -m venv venv
$ source venv/bin/activate
$ poetry install
```

## Usage
**Launch a script**
```
$ python -m src.main JSON_DATASET_FILE_NAME
```

Можно проверить работу скрипта на основании шаблона датасета:

```
$ python -m src.main tests/fixtures/example.json
```

## Tests
```
$ pytest
```