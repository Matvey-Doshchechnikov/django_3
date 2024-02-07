# Проект содержит в себе функции для исправления некоторых полей в базе данных электронного дневника

# Установка и использование функций

Введите в терминал команду для установки зависимостей

`Pip install requirements.txt`

Для использования функций в Django Shell введите команду 

`python manage.py shell`

# Функция исправления плохих оценок 

Чтобы исправить оценки ученика выполните данную команду

`fix_marks("ФИ0 ученика")`

# Функция удаления замечаний

`remove_chastisements("ФИ0 ученика")`

# Функция создания похвалы 

`create_commendation("ФИ0 ученика", "Название предмета")`



Код написан в образовательных целях на платформе [Devman](https://dvmn.org/)