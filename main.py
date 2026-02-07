from fastapi import FastAPI

app = FastAPI()


# @app : Path operation decorator
# .get : Operation
# ('/'): Path

# Pydantic: Responsible for data validation
 
@app.get('/')
def index(): # Path operation function
    # return "Hey!"
    return {
        'data':'blog list'
    }



# Moved upwards
@app.get('/blog/unpublished/')
def unpublished():
    return {'data': 'All unpublished blogs'}


@app.get('/blog/{id}/') # Dynamic Routing
def show(id: int):
    # Fetch blog with id=id
    return {
        'data': id
    }
"""
Error: fastAPI reads the file line by line
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "unpublished"
    }
  ]
}"""


@app.get('/blog/{id}/comments/')
def comments(id: int):
    # fetch comments of blog with id=id
    return {'data': {'1', '2'}}

