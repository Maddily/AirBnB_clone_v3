# AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School/ALX that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains FileStorage class that handles JSON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects
* `def get(self, cls, id)` - Retrieves an object
* `def count(self, cls=None)` - Returns the number of objects in storage matching the given class. If no class is passed, it returns the count of all objects in storage

#### `/models/engine` directory contains DBStorage class that interacts with the database:
[db_storage.py](models/engine/db_storage.py)
* `def get(self, cls, id)` - Retrieves an object
* `def count(self, cls=None)` - Returns the number of objects in storage 

#### `/api`  directory serves as the root of the API implementation, organizing different versions and functionalities.

#### `/api/v1` directory specifically represents version 1 of the API, facilitating backward compatibility and version management.
[app.py](/api/v1/app.py)
* `def teardown_storage(exception)` - Ends the current storage session 
* `def not_found_error(error)` - Return a JSON response with status code 404
* A `CORS` instance allowing '/*' for '0.0.0.0' to enable the web client to access the data.

#### `/api/v1/views`  directory contains modules defining endpoints for handling HTTP requests related to specific resources, such as users, places, and amenities.
  
#### `/api/v1/views/` directory contains new files:

[places.py](/api/v1/views/places.py) - contains routes for Place objects
* `def get_places(city_id)` - Retrieves a list of all place objects of a city
* `def get_place(place_id)` - Retrieves a place object
* `def delete_place(place_id)` - Deletes a place object
* `def create_place(city_id)` - Creates a place object
* `def update_place(place_id)` - Updates a place object

[places_amenities.py](/api/v1/views/places_amenities.py) - contains routes for linking Places and Amenities
* `def get_place_amenities(place_id)` - Retrieves the list of all Amenity objects of a Place
* `def delete_place_amenity(place_id, amenity_id)` - Deletes an Amenity object from a Place
* `def link_place_amenity(place_id, amenity_id)` - Links an Amenity object to a Place

[places_reviews.py](/api/v1/views/places_reviews.py) - contains routes for linking Places and Reviews
* `def get_all_reviews(place_id)` - Retrieves the list of all Review objects of a Place
* `def get_a_review(review_id)` - Retrieves a Review object.
* `def delete_a_review(review_id)` - Deletes a Review object
* `def create_a_review(place_id)` - Creates a Review
* `def update_a_review(review_id)` - Updates a review
 
[users.py](/api/v1/views/users.py) - contains routes for User objects
* `def get_all_users()` - Retrieves the list of all User objects
* `def get_a_user_using_id(user_id)` - Retrieves a user object
* `def delete_a_user(user_id)` - Deletes a User object
* `def create_a_user()` - Creates a User
* `def update_a_user(user_id)` - Updates a User object

[amenities.py](/api/v1/views/amenities.py) - contains routes for Amenity objects
* `def get_amenities()` - Retrieves a list of all amenity objects
* `def get_amenity(amenity_id)` - Retrieves an amenity object
* `def delete_amenity(amenity_id)` - Deletes an amenity object
* `def create_amenity()` - Creates an amenity object
* `def update_amenity(amenity_id)` - Updates an amenity object

[cities.py](/api/v1/views/cities.py) - contains routes for City objects
* `def get_cities_of_a_state(state_id)` - Retrieves the list of all City objects of a State
* `def get_a_city_using_id(city_id)` - Retrieves a city object
* `def delete_a_city(city_id)` - Deletes a City object 
* `def create_a_city(state_id)` - Creates a City
* `def update_a_city(city_id)` - Updates a City object

[states.py](/api/v1/views/states.py) - contains routes for State objects
* `def get_states()` - Retrieves a list of all State objects
* `def get_state(state_id)` - Retrieves a State object
* `def delete_state(state_id)` - Deletes a State object
* `def create_state()` - Creates a State object
* `def update_state(state_id)` - Updates a State object 

[index.py](/api/v1/views/index.py) - contains routes for index
* `def get_status()` - Returns a Json response indicating the status
* `def get_stats()` - Retrieves the count of existing objects by type

* [/api/__init__.py](/api/__init__.py) - Initializes the API package
* [/api/v1/__init__.py](/api/v1/__init__.py) - Initializes the v1 API package
* [/api/v1/views/__init__.py](/api/v1/views/__init__.py) - Initializes the views package for v1 of the API


## Test files

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects
* `def test_to_dict_exclude_password(self)` - Test that to_dict() excludes password when include_password=False

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_amenity(self)` - Test that models/amenity.py conforms to PEP8
* `def test_pep8_conformance_test_amenity(self)` - Test that tests/test_models/test_amenity.py conforms to PEP8
* `def test_amenity_module_docstring(self)` - Test for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Test for the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Test for the city.py module docstring
* `def test_city_class_docstring(self)` - Test for the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring
* `def test_get(self)` - Tests if get method retrieves objects correctly
* `def test_count_cls(self)` - Tests if count method correctly counts objects of a specific class
* `def test_count_all(self)` - Tests if count method correctly counts all objects
* `def test_save_password_hashed(self)` - Test that save method saves hashed password to file

[test_db_storage.py](tests/test_models/test_db_storage.py) - Contains the TestDBStorage class:
* `def test_get(self)` - Tests if get method retrieves objects correctly
* `def test_count_cls(self)` - Tests if count method correctly counts objects of a specific class
* `def test_count_all(self)` - Tests if count method correctly counts all objects

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_place(self)` - Test that models/place.py conforms to PEP8.
* `def test_pep8_conformance_test_place(self)` - Test that tests/test_models/test_place.py conforms to PEP8.
* `def test_place_module_docstring(self)` - Test for the place.py module docstring
* `def test_place_class_docstring(self)` - Test for the Place class docstring

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_review(self)` - Test that models/review.py conforms to PEP8
* `def test_pep8_conformance_test_review(self)` - Test that tests/test_models/test_review.py conforms to PEP8
* `def test_review_module_docstring(self)` - Test for the review.py module docstring
* `def test_review_class_docstring(self)` - Test for the Review class docstring

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_state(self)` - Test that models/state.py conforms to PEP8
* `def test_pep8_conformance_test_state(self)` - Test that tests/test_models/test_state.py conforms to PEP8
* `def test_state_module_docstring(self)` - Test for the state.py module docstring
* `def test_state_class_docstring(self)` - Test for the State class docstring

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8
* `def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_user_module_docstring(self)` - Test for the user.py module docstring
* `def test_user_class_docstring(self)` - Test for the User class docstring
* `def test_password_hashing(self)` - Test that the password is correctly hashed to MD5

[/test_v1/test_app.py](tests/test_api/test_v1/test_app.py) - Contains `TestApp` class:
* `def test_cors_configuration(self)` - Tests CORS configuration
* `def test_blueprint_registration(self)` - Tests blueprint registration
* `def test_error_handling(self)` - Tests error handling
* `def test_environment_variables(self)` - Tests environment variables
* `def test_doc(self)` - Tests module docstring existence
* `def test_function_doc(self)` - Tests function docstring existence (for all functions)
* `def test_pep8(self)` - Tests if module follows PEP8 style
* `def test_executable(self)` - Tests if the file is executable

[/test_views/test_states.py](tests/test_api/test_v1/test_views/test_states.py) - Contains `TestStates` class:
* `def test_doc(self)` - Tests module docstring existence
* `def test_function_doc(self)` - Tests function docstring existence (for all functions)
* `def test_pep8(self)` - Tests if module follows PEP8 style
* `def test_executable(self)` - Tests if the file is executable
* `def test_get_state(self)` - Tests GET request
* `def test_delete_state(self)` - Tests DELETE request
* `def test_create_state(self)` - Tests POST request
* `def test_update_state(self)` - Tests PUT request

[/test_views/test_amenities.py](tests/test_api/test_v1/test_views/test_amenities.py) - Contains `TestAmenities` class:
* `def test_doc(self)` - Tests module docstring existence
* `def test_function_doc(self)` - Tests function docstring existence (for all functions)
* `def test_pep8(self)` - Tests if module follows PEP8 style
* `def test_executable(self)` - Tests if the file is executable
* `def test_get_amenities(self)` - Tests GET request
* `def test_delete_amenity(self)` - Tests DELETE request
* `def test_create_amenity(self)` - Tests POST request
* `def test_update_amenity(self)` - Tests PUT request

[/test_views/test_places.py](tests/test_api/test_v1/test_views/test_places.py) - Contains `Testplaces` class:
* `def test_doc(self)` - Tests module docstring existence
* `def test_function_doc(self)` - Tests function docstring existence (for all functions)
* `def test_pep8(self)` - Tests if module follows PEP8 style
* `def test_executable(self)` - Tests if the file is executable
* `def test_get_place(self)` - Tests GET request
* `def test_delete_place(self)` - Tests DELETE request
* `def test_update_place(self)` - Tests PUT request

[/test_views/test_index.py](tests/test_api/test_v1/test_views/test_index.py) - Contains `TestIndex` class:
* `def test_doc(self)` - Tests module docstring existence
* `def test_function_doc(self)` - Tests function docstring existence (for all functions)
* `def test_pep8(self)` - Tests if module follows PEP8 style
* `def test_executable(self)` - Tests if the file is executable

[/test_views/test_cities.py](tests/test_api/test_v1/test_views/test_cities.py) - Contains `TestCityAPI`
* `def setUp(self)` - Prep function
* `def tearDown(self)` - Clean up function
* `def test_get_cities_by_state(self)` - Tests the retrival of all cities of a state
* `def test_get_city(self)` - Tests the retrival of a city
* `def test_delete_city(self)` - Tests the Deletion of a city
* ` def test_create_city(self)` - Tests the Creation of a city within a state
* `def test_update_city(self)` - Tests the updating of a state and city

[/test_views/test_user.py](tests/test_api/test_v1/test_views/test_user.py)
* `def test_get_all_users(self)` - Tests the retrival of all user
* `def test_create_user(self)` - Tests the creation of user
* `def test_create_user_missing_fields(self)` - tests the creating of a user with missing fields
* `def test_update_user(self)` - Tests the normal updating of user
* `def test_update_user_invalid_fields(self)` - Tests the updating of invalid fields

[/test_views/test_places_amenities.py](tests/test_api/test_v1/test_views/test_places_amenities.py)
* `def test_get_place_amenities(self)` - Test GET /api/v1/places/<place_id>/amenities
* `def test_delete_place_amenity(self)` - Test DELETE /api/v1/places/<place_id>/amenities/<amenity_id>
* `def test_link_place_amenity(self)` - Test POST /api/v1/places/<place_id>/amenities/<amenity_id>

[/test_views/test_places_reviews.py](tests/test_api/test_v1/test_views/test_places_reviews.py)
* `def test_get_all_reviews(self)` - Tests the retieval of all review of a place
* `def test_get_review(self)` - Tests the retrieval of a review 
* `def test_delete_review(self)` - Tests the deletion of a review
* `def test_create_review(self)` - Tests the creation of a review
* `def test_update_review(self)` - Tests the updating of a review

## Examples of use
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Bugs
No known bugs at this time. 

## Authors
Alexa Orrico - <a href="https://github.com/alexaorrico">Github</a> / <a href="https://twitter.com/alexa_orrico">Twitter</a><br>
Jennifer Huang - <a href="https://github.com/jhuang10123">Github</a> / <a href="https://twitter.com/earthtojhuang">Twitter</a><br>
Mayada Saeed - <a href="https://github.com/Maddily">Github</a> / <a href="https://www.linkedin.com/in/mayadase/">LinkedIn</a><br>
Sibongile Nhlema - <a href="https://github.com/Sibongile-Nhlema">Github</a> / <a href="https://www.linkedin.com/in/sibongile-nhlema/">LinkedIn</a><br>

Second part of Airbnb: Joann Vuong
## License
Public Domain. No copy write protection.
