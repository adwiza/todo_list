from bottle import route, run, view

class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False


@route('/')
@view('index')
def index():
    tasks = [
        TodoItem('Прочитать книгу'),
        TodoItem('Учиться жонгшлировать 30 минут'),
        TodoItem('Помыть посуду'),
        TodoItem('Поесть'),
    ]

    return {'tasks': tasks}

###
run(host='localhost', port=8080)
