# Manual flask_tutorial

## Web Server Interface Connection

cd flask_tutorial

source bin/activate

python index.py

## Curls to prove GET and POST methods opening other CLI window

- curl 127.0.0.1:5000

- output

{
  "about": "Hello World!"
}


- curl 127.0.0.1:5000/multi/10 ( use any numeric value at the end of route)

- output

{
  "result": 100
}


- curl 127.0.0.1:5000 -H 'Content-Type: application/json' -d '{"name": "Orlando", "age": 37}'

- output

{
  "you sent": {
    "age": 37,
    "name": "Orlando"
  }
}

# Close the connection

deactivate
