from flask_app import app

from flask_app.controllers import category_controller, user_controllers,profile_controller,top_event_controllers, informations_controller, user_profile_by_id, test_controller,create_event_controller,like_controllers

if __name__ == "__main__":
    app.run(debug=True)