# Define the AWS account ID
account_id = "22042026"

# Define the project name
project_name = "cloud_project"

# Concatenate strings to form the S3 bucket name
bucket_name = account_id + '-' + project_name + "-bucket"

# Print the resulting bucket name
print(f"S3 Bucket Name: {bucket_name}")

# EXERCISE EC2 STRING CONCATENATION
# Environment name 
environment = 'prod'

# application name
application = 'spaceX'

# instance number
instance_number = "08"

# Concatenate
instance_name = environment + "-" + application + "-instance-" + instance_number

# Print
print("EC2 instance name: "+instance_name)

