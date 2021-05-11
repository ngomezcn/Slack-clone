Estos archivos deben ir en la carpeta " /etc/systemd/system/"


Comandos de ayuda:
sudo journalctl -u {service}.socket
sudo systemctl status {service}


Test if is working:
curl --unix-socket /run/{service}.sock localhost


Despues de un ajuste
sudo systemctl daemon-reload
sudo systemctl restart {service}







