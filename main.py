from robinhwang import create_app
from waitress import serve

app = create_app()

if __name__ == '__main__':
    #app.run(debug=True)
    serve(app, host='0.0.0.0', port=5000, url_scheme='https')