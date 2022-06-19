# Ordering Pizza App

> Best ordering pizza app!

## Table of contents

- [General info](#general-information)
- [Demo](#demo)
- [Technologies](#technologies-used)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [ToDo/Bugs](#todo-bugs)
- [Contact](#contact)

## General Information

Ordering Pizza App is a django based web application. App provide user registration and authentication, after login you can place you order for your favorite pizza, check your cart items and checkout info. Restaurant manager will be able to view orders and manage queues. Database is using PostgreSQL that is hosted on ElephantSQL service.

## Demo

Use default admin user.
**login: admin**
**password: root**

## Technologies Used

- Python 3.8
- Django 4.0.4
- crispy-bootstrap5 0.6
- django-crispy-forms 1.14.0

## Screenshots

-

## Setup

1. Create directory for an app.
```sh
mdkir OrderPizza
```
2. Open up terminal within directory.
```sh
cd OrderPizza
```
3. Git clone repository: 
```sh
git clone https://github.com/Tomz899/OrderPizza.git
```

4. In project directory use docker command to build, start and attach containers for service.
```sh
docker-compose up
```
5. Open browser and type:
```sh
localhost:8000
```

## ToDo Bugs

- **{todo}** Use django sessions for orders and cart items.

## Contact

Created by [@me](mailto:tomek.nowak@aol.pl) - if you have any questions, just contact me!
