#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
    console.error('Please provide the API URL as the first argument.');
    process.exit(1);
}

// Define the character ID for Wedge Antilles
const wedgeAntillesId = '18';

// Make a GET request to the provided API URL
request.get(apiUrl, (error, response, body) => {
    if (error) {
        // Print the error if there is one
        console.error(error);
    } else {
        // Parse the JSON response body
        const data = JSON.parse(body);
        const films = data.results;
        let count = 0;

        // Iterate over the list of films
        for (const film of films) {
            // Check if the character ID is in the film's characters list
            if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
                count++;
            }
        }

        // Print the count of films where Wedge Antilles is present
        console.log(count);
    }
});
