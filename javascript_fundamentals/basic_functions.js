// ----- Basic Functions -----
function sayHello() {
	console.log("Hello, Mischa!");
}

// Calling function
sayHello();

// ----- Function Parameters -----
function deployToRegion(region) {
	console.log("Deploying to region: " + region);
}

// Calling Function with Parameters
deployToRegion("us-east-1");


// ----- Exercise -----

function configureService(serviceName, tier) {
	console.log("Configuring " + serviceName + " service with tier: " + tier);
}

configureService("Bedrock", "Flex Tier");
configureService("CloudTrail", "Insights Events");



