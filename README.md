# Country Capital API

## Overview

Country Capital API is a Python Flask API that returns the name of a country when a capital city is provided.

The API is served using Uvicorn.

## API Endpoint

The API is available as a microservice endpoint:

https://example.com/country-capital/<query-params>

The endpoint can be used by other projects in the organization to consume the Country Capital API.

## How It Works

1. Provide a capital city as a query parameter.
2. The API processes the given capital city.
3. The API returns the corresponding country name.

## Technologies Used

- Python
- Flask
- Uvicorn

## Repository

country-capital-api

## Usage

The microservice endpoint can be consumed by any project in the organization that needs to find the country corresponding to a capital city.

Endpoint:

https://example.com/country-capital/<query-params>