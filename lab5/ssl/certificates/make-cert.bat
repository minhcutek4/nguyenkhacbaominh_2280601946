openssl req -new -x509 -newkey rsa:2048 -nodes -keyout sever-key.key -out 
server-cert.crt -days 365 -config sever-cert.cnf 