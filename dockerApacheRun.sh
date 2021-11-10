#! /bin/sh

apt update
apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io -y

# Ajout du groupe docker à l'utilisateur
usermod -aG docker $USER
newgrp docker
groups

# Instanciation d'un container apache avec forwarding de port
docker run --name apacheApp -p 80:80 -d httpd:2.4-alpine
