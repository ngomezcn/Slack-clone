These files must go in the folder "/etc/systemd/system/"

- daphne.service
- gunicorn.service
- gunicorn.socket

Those servies are called are used by Nginx to pass HTTP and WebSocket connections to Django.

The spacechat-init file should go to the folder "/etc/init.d/" is used to activate Redis and Daphne when starting the server.