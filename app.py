#Entry poiint for the Site
from flask import Flask
from views import views #from app views, import variable views

app = Flask(__name__)
# Will set the main url as http://127.0.0.1:8000
app.register_blueprint(views, url_prefix="/toolkit") 


if __name__ == '__main__':
    app.run(debug=True, port=8000) 
    #debug = True, detects/allows changes 
    # to be made without re running the application