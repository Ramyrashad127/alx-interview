# 0x06. Star Wars API

## Description
This project interacts with the external **Star Wars API (SWAPI)** using Node.js to retrieve and display character names from a specified Star Wars film in the exact sequence in which they appear in the film's character list.

## Requirements
- Node.js version `14.x`+
- Style guide: `semistandard`
- Dependencies: `request` module
- The first positional argument is the Movie ID (e.g., `3` for Return of the Jedi).

## Tasks

| File | Description |
| :--- | :--- |
| `0-starwars_characters.js` | Script that fetches film metadata from `https://swapi-api.alx-tools.com/api/films/:id` and recursively or asynchronously logs character names in original order. |

## Installation & Usage

```bash
$ npm install request
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
