# https://aws.amazon.com/fr/sdk-for-python/

import boto3

ec2 = boto3.client('ec2')

numInstances = int(input("Saisir le nombre d'instances 'ec2' souhaité : "))
# numInstances = 1
i = 0

f = open("dockerApacheRun.sh", "r") # Ouverture fichier en lecture seule
apacheScript = f.read()             # lecture du fichier et stockage de son contenu
f.close()                           # libération du fichier
# print(apacheScript)

# Instanciations des VMs
while i < numInstances:
    response = ec2.run_instances(
        ImageId='ami-0a49b025fffbbdac6',
        InstanceType='t2.micro',
        KeyName='kp-first',
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=['sg-0a178a3df63897f37',], # ID of sgFirst
        UserData=apacheScript
    )
    
    # print(response)
    
    # Récupération de l'ID et de l'IP publique
    instances = response.get("Instances")
    instanceID = instances[0].get("InstanceId")
    # publicIP = instances[0].get("PublicIpAddress")
    # print(instances)
    print(instanceID)
    # print(publicIP)
    # L'adresse IP publique est vide lors du présent retour
    # => récupération de l'IP publique dans le script de requêtes http
    
    # Sauvegarde de l'ID
    f = open("instances/instance"+str(i)+".txt", "w")   # Ouverture fichier en écriture /!\ écrasement si le fichier est déjà présent
    instanceOutput = f.write(instanceID)                # Sauvegarde de l'ID
    f.close()                                           # libération du fichier
    
    i+=1

