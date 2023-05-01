# Recipe Sharing Platform API

The Recipe Sharing Platform API provides developers with a fast and easy way to build scalable recipe sharing applications without having to write excess code. With the recipe sharing API, users can upload or share their recipe, get recipe details, and search for recipes, among other features.

## Getting Started

To get started with our API, you will need to sign up for an account using the available API end point for sign up to get an API key. Once you have an API key, you can start making API requests to our endpoints.

## API Endpoints

The recipe sharing platform API provides the following endpoints:

- `localhost/recipes` - Returns a list of all recipes.
- `localhost/recipes/{id}` - Returns details for a specific recipe.
- `localhost/recipes/rating` - Searches for recipes by keyword or ingredients.
- `localhost/recipes/comments` - Returns a comment of all recipes.
- `localhost/recipes/search` - Returns recipes base on recipe name

Each endpoint supports both JSON and XML response formats.

## Authentication

Access to the API endpoint requires an API key, which should be included in the headers of each request. If you do not include a valid API key, you will receive a 401 Unauthorized error. The API endpoint for signing up and getting API key:

- `localhost/account/sign-up` - returns the API key/token for authentication

## Rate Limiting
 To prevent API abuse this API is rate-limited. As only authenticated user can perform operation on the endpoint, user can oly make
 10 request per minute

