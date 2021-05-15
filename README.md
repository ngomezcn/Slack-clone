# Django Channels realtime message app 
## Deployed on a Nginx production server with Daphne and Gunicorn over SSL


<img src="https://iconape.com/wp-content/png_logo_vector/nginx.png" align="right"
      width="150" height="150">

This project has been inspired by applications such as WhatsApp and Slack, the idea behind this project is to be able to create a minimum viable product of a real-time messaging web application using websockets technology, deployed in a real production environment.

* **Nginx** proxy pass to **Daphne ASGI** and **Gunicorn WSGI**.
* Using **Redis Channel** to manage all websockets layer
* Configured `/static/` folder on Nginx to serve all static files like **css, javascript, images**.
* All conections **HTTP and WebSockets** are working over **TLS/SSL**.
* Using **csrf token** on login page to avoid middleware attacks.
* **Wrapped WebSocket** connection over the module AuthMiddlewareStack.
* Using a pretty GUI to help user to interact with app. 
* You can also manage all chats from **Django Administrator panel**
* Using **JSON** files to make messages perisent in **sqlite database**

## Some screenshots of the app

### Login page 
<img src="./images/login_screen.jpg">

### Home page 
<img src="./images/dashboard_screen.jpg">

### Example chat page 
<img src="./images/chat_example.jpg">

## To do ideas
* Add support for multiple languages or at least for the most common ones
* Add an complex sistem of levels and permissions
* Add support to send images and videos
* Detect if an user is already logged from another device
* Encrypt messages in the database 
* Also encrypt all messages while they are being processed on the server
* Add private chats between users

Im not going to following developing and maintain this project anymore, if you wanna use it be some purpose be free to dot it.


## Libraries and documentation used 
* [Django](https://www.djangoproject.com/) and
  [Django Channels](https://channels.readthedocs.io/en/stable/).
* [Nginx conf](https://www.nginx.com/)
* [Gunicorn repo](https://github.com/benoitc/gunicorn)
* [Redis](https://pypi.org/project/channels-redis/) 
* [Ddaphne](https://github.com/django/daphne) 
* [Digital Ocean](https://github.com/postcss/postcss/commit/)
* and a lot more ...