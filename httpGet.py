import boto3,os
import requests as req

ec2 = boto3.client('ec2')

files = os.listdir("instances")

for f in files:
    inst = open("instances/"+f, "r")
    instanceID = inst.read()
    inst.close()
    
    # Demande de description de l'instance ec2 spécifiée
    response = ec2.describe_instances(
        InstanceIds=[instanceID],
    )

    # Récupération de l'IP publique
    # response {'Reservations': [ {'Instances': [ {'PublicIpAddress': 'string',} ] } ] }
    reservations = response.get("Reservations")
    instances = reservations[0].get("Instances")
    publicIP = instances[0].get("PublicIpAddress")
    # print(publicIP)

    httpGet = req.get("http://"+publicIP)
    if httpGet.status_code == 200:
        print("IP: %s Response: OK" % publicIP)
    else:
        print("L'instance %s ne répond pas" % instanceID)
    

