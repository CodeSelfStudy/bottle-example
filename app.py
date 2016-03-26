from bottle import route, run, template

@route('/')
def index():
    title = 'Saluton, Mondo'
    body = '''
    <p>This is the body.</p>
    <p>Some more text.</p>
    '''
    return template('templates/index', title=title, body=body)

run(host='localhost', port=8080, debug=True)
