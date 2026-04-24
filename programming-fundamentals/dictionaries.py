# Dictionaries
# - Store and retrieve information
# - Key and Values

# EC2

ec2_instance = {
        "InstanceId": "i-8899april",
        "InstanceType": "c5d.large",
        "State": "running",
        "PublicIpAddress": "203.0.111.2"
}

instance_id = ec2_instance["InstanceId"]
print(f"this is a {instance_id} instance")

public_ip = ec2_instance.get("PublicIpAddress", "No Public IP address is here")
print(f"the instances public ip is: {public_ip}")

# Adding a new key-value pair
ec2_instance["AvailabilityZone"] = "us-east-1"
ec2_instance["State"] = "stopped"

print(ec2_instance)

# Using pop()
rm_instance_type = ec2_instance.pop("InstanceType")

print(f"removed instance type: {rm_instance_type}")
print(ec2_instance)

# Using Del
del ec2_instance["AvailabilityZone"]
print(ec2_instance)

