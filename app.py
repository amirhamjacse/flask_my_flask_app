# from flask import Flask, render_template
# from flask.views import MethodView
# from models import db, User
# app = Flask(__name__)
# from config import Config
# from flask_admin import Admin
# from flask_migrate import Migrate
# from flask_admin.contrib.sqla import ModelView

# migrate = Migrate(app, db)

# # @app.route('/')
# # def home():
# #     return render_template('index.html')
# #     # return "Hello this is my first flask app"

# # if __name__ == '__main__':
# #     app.run(debug=True)
# # Initialize Flask-Admin
# admin = Admin(app, name='My Admin', template_mode='bootstrap3')
# admin.add_view(ModelView(User, db.session))

# app = Flask(__name__)

# # Define a class-based view
# class HomePage(MethodView):
#     def get(self):
#         return render_template('index.html')

# class AboutPage(MethodView):
#     def get(self):
#         return render_template('about.html')

# # Register the views
# app.add_url_rule('/', view_func=HomePage.as_view('home'))
# app.add_url_rule('/about', view_func=AboutPage.as_view('about'))


# app = Flask(__name__)
# app.config.from_object(Config)

# db.init_app(app)
# migrate = Migrate(app, db)  # Initialize Flask-Migrate


# if __name__ == '__main__':
#     with app.app_context():
#         # Create the database
#         db.create_all()  # This will create all tables defined by your models
#     app.run(debug=True)


from flask import Flask, render_template
from flask.views import MethodView
from models import db, User  # Make sure these imports are correct
from config import Config
from flask_admin import Admin
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Initialize Flask-Admin
admin = Admin(app, name='My Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

# Define a class-based view for the home page
class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

# Define a class-based view for the about page
class AboutPage(MethodView):
    def get(self):
        return render_template('about.html')

# Register the views
app.add_url_rule('/', view_func=HomePage.as_view('home'))
app.add_url_rule('/about', view_func=AboutPage.as_view('about'))

if __name__ == '__main__':
    with app.app_context():
        # Create the database and tables if they don't exist
        db.create_all()  # This will create all tables defined by your models
    app.run(debug=True)
