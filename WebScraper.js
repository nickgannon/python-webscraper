const axios = require('axios');
const cheerio = require('cheerio');

// Prompt the user for the URL to be scraped
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter the URL to be scraped: ", async function(url) {
  // Send an HTTP GET request to the URL
  try {
    const response = await axios.get(url);

    // Parse the HTML content of the page using Cheerio
    const $ = cheerio.load(response.data);

    // Find all the div elements
    const divElements = $("div");

    // Print the text content of the div elements
    divElements.each((index, element) => {
      console.log($(element).text());
    });
  } catch (error) {
    console.error("Error scraping the URL:", error);
  }

  rl.close();
});
