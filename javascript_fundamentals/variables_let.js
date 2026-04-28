// Variables - let

let x = 5; //number
let y = 3.14; //number
let name = "Soleyman"; //string
let isValid = true; //boolean

// `const` - block-scoped, cannot be reassigned. Use it when the value never changes.
// `var` - old way, function-scoped, can be reassigned and re-declared. Avoid it in modern JS.


function deployResources(isProduction) {
	let region = 'us-east-1a'; // Default region for development
	if (isProduction) {
		let region = 'us-east-1b'; // Region for production
		console.log(`Deploying production resources in ${region}`);
		// Deploy production-specific resources here
	}
	console.log(`Setting up monitoring in ${region}`);
	// Set up monitoring here
}

deployResources(true); // Deploy for production
deployResources(false); // Deploy for development

