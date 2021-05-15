These files must go in the folder "/etc/systemd/system/"

- daphne.service
- gunicorn.service
- gunicorn.socket





Comandos de ayuda:
sudo journalctl -u {service}.socket
sudo systemctl status {service}




Despues de un ajuste
sudo systemctl daemon-reload
sudo systemctl restart {service}


# daphne

#! /bin/bash

service daphne start
#docker run -p 6379:6379 -d redis:latest
docker run -p 6379:6379 -d redis:6.2.3

exit 0


sudo chmod 755 /etc/init.d/daphne-init
sudo update-rc.d nt
 defaults




