const util = require('util');
const request = util.promisify(require('request'));

const filmId = process.argv[2];

async function fetchStarWarsCharacters(id) {
  const filmEndpoint = 'https://swapi-api.hbtn.io/api/films/' + id;
  try {
    const filmResponse = await request(filmEndpoint);
    const filmData = JSON.parse(filmResponse.body);
    const characters = filmData.characters;

    for (let i = 0; i < characters.length; i++) {
      const characterEndpoint = characters[i];
      try {
        const characterResponse = await request(characterEndpoint);
        const characterData = JSON.parse(characterResponse.body);
        console.log(characterData.name);
      } catch (error) {
        console.error(error);
      }
    }
  } catch (error) {
    console.error(error);
  }
}

fetchStarWarsCharacters(filmId);
