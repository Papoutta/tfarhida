from flask_app import app

from flask_app.controllers import category_controller, user_controllers,profile_controller,create_event_controller

if __name__ == "__main__":
    app.run(debug=True)