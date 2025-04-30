# 📝 Private Diary

Персональный веб-дневник, разработанный на Django.  
Позволяет пользователю вести личные записи, фильтровать их по дате, редактировать и удалять. Сайт адаптирован для комфортной работы с ПК и мобильных устройств.

---

## 🚀 Функционал

- Регистрация и авторизация пользователей
- Создание, редактирование и удаление записей
- Поддержка Markdown для форматирования текста
- Фильтрация записей по дате публикации
- Личный профиль с возможностью смены аватара
- Защита пользовательских данных — каждый видит только свои записи
- Подключена социальная авторизация (Google и др.)

---

## 🧠 Используемые технологии

- **Backend:** Django 5.2, Django REST Framework
- **Frontend:** Bootstrap 4, HTML5, CSS3
- **Аутентификация:** Django Auth + social-auth
- **База данных:** SQLite (можно легко заменить на PostgreSQL/MySQL)
- **Другое:** crispy-forms, django-filter

---

## 📦 Установка (локально)

```bash
git clone https://github.com/hellaraze/private-diary.git
cd private-diary
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver# dyary0django
