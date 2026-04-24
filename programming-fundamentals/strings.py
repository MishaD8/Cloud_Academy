# Single quotes

single_quotes = 'This is an EC2'

# Double quotes

double_quotes = "This is an S3 bucket"

# Triple quotes for multi_line strings

multi_line = """
This is a Cloudformation template.
Which has multiple lines.
"""

print(single_quotes)
print(double_quotes)
print(multi_line)

#Exercise
#Create a single quoted string for an AWS region name 
aws_region = 'us-east-1'
#Create a double quoted string for an ec2 instance type 
ec2_instance_type = 'm6i.xlarge'
#Create a multi line string for a simple IAM policy
iam_policy = """
{
    "Version":"2012-10-17"
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3::example-bucket"
        }
    ]
}
"""

print(aws_region)
print(ec2_instance_type)
print(iam_policy)

