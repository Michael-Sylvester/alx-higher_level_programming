#!/usr/bin/node

// Import the required module
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
    console.error('Usage: node 6-completed_tasks.js <API URL>');
    process.exit(1);
}

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
    if (error) {
        // Print the error if there is one
        console.error('Error:', error);
        return;
    }

    // Parse the response body as JSON
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks by user ID
    const completedTasks = {};

    // Iterate through the tasks
    tasks.forEach(task => {
        if (task.completed) {
            // If the task is completed, increment the count for the user ID
            if (!completedTasks[task.userId]) {
                completedTasks[task.userId] = 0;
            }
            completedTasks[task.userId]++;
        }
    });

    // Print the result
    console.log(completedTasks);
});
