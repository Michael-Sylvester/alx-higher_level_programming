#!/usr/bin/node

// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
    console.error('Please provide a file path as the first argument.');
    process.exit(1);
}

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        // Print the error object if there is an error
        console.error(err);
    } else {
        // Print the file content
        console.log(data);
    }
});
