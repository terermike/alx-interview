#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const id = process.argv[2];

async function starwars (id) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let x = 0; x < characters.length; x++) {
    const url = characters[x];
    let character = await (await request(url)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}
starwars(id);
