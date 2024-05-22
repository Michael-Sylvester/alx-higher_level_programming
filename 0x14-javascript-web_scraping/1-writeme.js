#!/usr/bin/node

// Import the 'fs' module to interact with the file system
const fs = require('fs');

// Get the file path and string to write from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both the file path and content are provided
if (!filePath || !content) {
    console.error('Please provide both a file path and a string to write.');
    process.exit(1);
}

// Write the content to the file in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
        // Print the error object if there is an error
        console.error(err);
    } else {
        // Log a success message
        console.log('Content written successfully!');
    }
});