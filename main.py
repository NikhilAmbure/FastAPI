from fastapi import FastAPI

app = FastAPI()


# @app : Path operation decorator
# .get : Operation
# ('/'): Path

@app.get('/')
def index(): # Path operation function
    # return "Hey!"
    return {
        'data': {
            'name': "Nikhil"
        }
    }


@app.get('/about')
def about():
    return {
        'data':'about page'
    }
