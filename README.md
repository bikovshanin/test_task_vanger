# Test Task - Fake Nasa


### Используемые технологии:

[![Python](https://img.shields.io/badge/Python-3.9-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3111/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/3.2/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=#4479A1)](https://dev.mysql.com/doc/refman/8.0/en/)
[![Botstrap5](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=Bootstrap&logoColor=white)](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

### Для запуска:

1. **Установка:** Клонируйте репозиторий на свой компьютер.
2. **Docker Compose:** Перейдите в директорию проекта и выполните:

```bash
docker compose up --build
```
3. Admin Panel: Для доступа к панели администратора создайте суперпользователя командой:

```bash
docker compose exec web python fake_nasa/manage.py createsuperuser
```
4. **Доступ к вебсайту:** После завершения настройки среды Docker Compose пройдите по ссылке:

    http://127.0.0.1/
