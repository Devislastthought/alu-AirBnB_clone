# AirBnB clone - The console

## Description
First step of a full web application: the AirBnB clone. This project provides
a command interpreter (built with Python's `cmd` module) to manage AirBnB
objects, a `BaseModel` parent class, child classes (`User`, `State`, `City`,
`Amenity`, `Place`, `Review`) and a first storage engine (`FileStorage`) that
persists objects in a JSON file.

Flow: `Instance <-> dict <-> JSON string <-> file.json`

## Project structure
```
console.py                  command interpreter (entry point)
models/base_model.py        BaseModel (id, created_at, updated_at, save, to_dict)
models/user.py ... review.py  classes inheriting from BaseModel
models/engine/file_storage.py  FileStorage (JSON serialization)
tests/                      unittest suite
```

## Requirements
Ubuntu 20.04+, Python 3.8+, pycodestyle 2.7.*

## How to start
```
chmod +x console.py
./console.py                 # interactive mode
echo "help" | ./console.py   # non-interactive mode
```

## How to use
Commands: `quit`, `EOF`, `help`, `create`, `show`, `destroy`, `all`, `update`.

```
(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-...) {...}
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) all User
["[User] (49faff9a-...) {...}"]
(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
```
Usage: `update <class> <id> <attribute name> "<attribute value>"`

## Tests
```
python3 -m unittest discover tests
echo "python3 -m unittest discover tests" | bash
```
