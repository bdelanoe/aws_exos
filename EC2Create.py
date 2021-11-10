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
response = ec2.run_instances(
    ImageId='ami-0a49b025fffbbdac6', # ubuntu server 20.04 eu-central-1
    InstanceType='t2.micro',
    KeyName='kp-first',
    MaxCount=numInstances,
    MinCount=numInstances,
    SecurityGroupIds=['sg-0a178a3df63897f37',], # ID of sgFirst : ssh + http
    UserData=apacheScript,
    DryRun=False
)

# Récupération des identifiants des instances
instanceIDs = ''

for instance in response['Instances']:
    # print(instance['PublicIpAddress']) # KeyError: 'PublicIpAddress' => cette clé n'existe pas encore
    if instanceIDs == '':
        instanceIDs = instance['InstanceId']
    else:
        instanceIDs += '\n' + instance['InstanceId']

# Sauvegarde des identifiants des instances dans un fichier texte
with open("instanceIds.txt", "w") as f:
    f.write(instanceIDs)




