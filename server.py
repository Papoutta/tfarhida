from flask_app import app

from flask_app.controllers import category_controller, user_controllers,home_controller ,home_after_login_controller,profile_controller, informations_controller, user_profile_by_id, test_controller

if __name__ == "__main__":
    app.run(debug=True)