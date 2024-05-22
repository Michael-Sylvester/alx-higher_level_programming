#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Check if the URL is provided
if (!url) {
    console.error('Please provide a URL as the first argument.');
    process.exit(1);
}

// Make a GET request to the provided URL
request.get(url, (error, response, body) => {
    if (error) {
        // Print the error if there is one
        console.error(error);
    } else {
        // Print the status code
        console.log(`code: ${response.statusCode}`);
    }
});
