terraform {
  backend "s3" {
    bucket         = "mykhaylo-terraform-state"
    key            = "global/s3/terraform/.tfstate"
    region         = "us-east-1"
    dynamodb_table = "s3-md-tf-table"

  }
}
