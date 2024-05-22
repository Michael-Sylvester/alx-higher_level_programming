#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
    console.error('Please provide a movie ID as the first argument.');
    process.exit(1);
}

// Define the URL for the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the provided URL
request.get(url, (error, response, body) => {
    if (error) {
        // Print the error if there is one
        console.error(error);
    } else {
        // Parse the JSON response body
        const data = JSON.parse(body);
        // Check if the response contains a title
        if (data.title) {
            // Print the movie title
            console.log(data.title);
        } else {
            // Print an error message if the title is not found
            console.error('Movie not found');
        }
    }
});
