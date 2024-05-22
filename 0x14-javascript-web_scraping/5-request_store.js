#!/usr/bin/node

// Import the required modules
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both URL and file path are provided
if (!url || !filePath) {
    console.error('Usage: node 5-request_store.js <URL> <file path>');
    process.exit(1);
}

// Make a GET request to the URL
request(url, (error, response, body) => {
    if (error) {
        // Print the error if there is one
        console.error('Error:', error);
        return;
    }

    // Write the response body to the specified file
    fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
            // Print the error if there is one
            console.error('Error writing to file:', err);
        }
    });
});
