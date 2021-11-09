#! /bin/sh

# Rendre le fichier exécutable:   $ sudo chmod 774 dockerInstall.sh
# Pour installer Docker exécuter: $ ./dockerInstall.sh

sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

# Ajout du groupe docker à l'utilisateur
sudo usermod -aG docker $USER
newgrp docker
groups

# Instanciation d'un container apache avec forwarding de port
docker run --name apacheApp -p 80:80 -d httpd
