import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

interface MyBucketProps {
	bucketName: string;
	versioned: boolean;
	encryption: s3.BucketEncryption;
}

export class CdkWeek10Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    
    const bucketProps: MyBucketProps = {
	    bucketName: 'Mischa-S3-Bucket-SS-CDK- ' + this.account,
	    versioned: true,
	    encryption: s3.BucketEncryption.S3_MANNAGED,
    }
  }
}
