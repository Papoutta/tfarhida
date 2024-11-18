from flask_app import app

<<<<<<< HEAD
from flask_app.controllers import category_controller, user_controllers,home_controller ,home_after_login_controller,profile_controller, informations_controller, user_profile_by_id, test_controller
=======
from flask_app.controllers import category_controller, user_controllers,profile_controller,create_event_controller
>>>>>>> 0008025980d1392cf1f4bd09da1e022494fd2cad

if __name__ == "__main__":
    app.run(debug=True)