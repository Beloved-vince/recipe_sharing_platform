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


## Endpoint Parameters and Error Handling
The recipe sharing API endpoint parameters to be passed in the request URL and header

- #  For Authentication

- POST /account/sign-up
    - Returns a token for sign-up user
###### parameters accepted
| Key | Type | Description |
| --- | ---- | ----------- |
| `username` | string | [required] unique usename of the requested user|
| `password` | string | [required]. password must contain atleast 8 character with alphabet numeric and symbols|
| `firstname` | string | [required] User first name. |
| `lastname` | string | [required]. User last name. |
| `email` | email/string | [required]unique email address. |


- GET /recipes
    - Returns a list of all recipes
    
[
  {
    "id": "123456789",
    "author": "John Smith",
    "name": "Spaghetti Bolognese",
    "ingredients": [
      {
        "name": "spaghetti",
        "quantity": "200g"
      },
      {
        "name": "ground beef",
        "quantity": "500g"
      },
      {
        "name": "tomato sauce",
        "quantity": "400g"
      }
    ],
    "preparation_steps": "1. Cook spaghetti according to package instructions. \n2. Brown ground beef in a pan. \n3. Add tomato sauce to the beef and let it simmer for 10 minutes. \n4. Serve the beef sauce over the cooked spaghetti.",
    "cooking_time": "30 minutes",
    "nutrition_info": {
      "calories": "500",
      "fat": "25g",
      "protein": "30g",
      "carbohydrates": "40g"
    }
  },
  {
    "id": "987654321",
    "author": "Jane Doe",
    "name": "Chicken Curry",
    "ingredients": [
      {
        "name": "chicken breast",
        "quantity": "500g"
      },
      {
        "name": "curry powder",
        "quantity": "2 tbsp"
      },
      {
        "name": "coconut milk",
        "quantity": "400ml"
      }
    ],
    "preparation_steps": "1. Cut the chicken into small pieces. \n2. Fry the chicken in a pan. \n3. Add the curry powder and fry for 1 minute. \n4. Add the coconut milk and let it simmer for 20 minutes. \n5. Serve with rice.",
    "cooking_time": "35 minutes",
    "nutrition_info": {
      "calories": "600",
      "fat": "35g",
      "protein": "40g",
      "carbohydrates": "30g"
    }
  }
]```
    Tags: json, recipe, ingredients, nutrition, cooking_time, preparation_steps
# 
- POST /recipes
    - Create a new recipe and add it to the existing recipes and return list of all recipes 

