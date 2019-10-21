# Genius Plaza Backend Test 

This project contains my API design for the Genius Plaza Test. The GeniusPlaza project contains an app called recipes which contains the models requried for the API. In this case we have models for: Users, Steps, Ingredients, and Recipes. 

# API

The current API implements the following methods: 

- ## Get all recipes available in the database. 
    * Use ` GET http://localhost:8000/recipes/` and include the necessary information for a new recipe in json. 

- ## Create a new recipe. 
    * Use ` POST http://localhost:8000/recipes/` and include the necessary information for a new recipe in json. 

- ## Get recipes by a particular user. 
    * Use ` GET http://localhost:8000/recipes/user/<user_id>` and include the necessary information for a new recipe in json. 

- ## Update a particular recipe. 
    * Use ` PUT http://localhost:8000/recipes/<recipe_id>` and include the necessary information for a new recipe in json. 

- ## Delete a particular recipe. 
    * Use ` DELETE http://localhost:8000/recipes/<recipe_id>` and include the necessary information for a new recipe in json. 

# Input Validation

Input validation is done by djangorestframework

# Requirements and Dependencies

use  `pip install -r requirements.txt`