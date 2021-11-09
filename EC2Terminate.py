import boto3,os

ec2 = boto3.client('ec2')

numTerminatedInstances = 0
files = os.listdir("instances")

for f in files:
    inst = open("instances/"+f, "r")
    instanceID = inst.read()
    inst.close()

    response = ec2.terminate_instances(
        InstanceIds=[
            instanceID,
        ]
    )

    os.remove("instances/" + f)
    numTerminatedInstances += 1
    print("Instance '%s' terminée" % instanceID)

print("%d instances 'ec2' ont été terminées" % numTerminatedInstances)

