#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const movieUrl = `${API_URL}/films/${movieId}/`;

  request(movieUrl, (err, res, body) => {
    if (err) {
      return console.error(err);
    }

    const charactersURLs = JSON.parse(body).characters;
    const characterPromises = charactersURLs.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (charErr, charRes, charBody) => {
          if (charErr) {
            reject(charErr);
          } else {
            resolve(JSON.parse(charBody).name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(allErr => console.error(allErr));
  });
} else {
  console.log('Usage: ./script_name.js <Movie ID>');
}
