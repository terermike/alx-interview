#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

function fetchCharacterData(characterList, index) {
  if (index === characterList.length) {
    return;
  }

  const characterUrl = characterList[index];
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      fetchCharacterData(characterList, index + 1);
    }
  });
}

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    const characterList = filmData.characters;
    fetchCharacterData(characterList, 0);
  }
});
