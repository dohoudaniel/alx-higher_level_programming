#!/usr/bin/node
const request = require('request');
// Declare variables
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
// Sending the HTTPS GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
