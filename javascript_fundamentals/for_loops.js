// ----- For loops -----

let regions = ["us-east-1", "us-west-1", "eu-west-1", "ap-southeast-1"];

for (let i=0; i<regions.length; i++) {
	console.log("Deploying to region: " + regions[i]);
}

// ----- Exercise -----
// Array of cloud services

let cloudServices = ["ELB", "CloudFront", "Bedrock", "NAT Gateway"]

for (let i=0; i<cloudServices.length; i++) {
	console.log("Configuring AWS " + cloudServices[i] + " Service")
}


