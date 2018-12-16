
from flask import Flask, jsonify, make_response
from app import create_app

app = create_app(config_name="development")

@app.errorhandler(404)
def page_not_found(e):
    """error handler default method for error 404"""

    return make_response(
        jsonify(
            {"message": "Page not found.Kindly check"
            "whether your url is correct", "status": 404}
            ), 404
        )

@app.errorhandler(Exception)
def unhandled_exception(e):
    print(e)
    return make_response(
        jsonify(
            {
                "message": "Server error. "
                "Please contact the admin",
                "status": 500
            }
            ), 500
        )

@app.route('/')
def landing_page():
    
    return "Welcome to iReporter.\n\
      A place to report all corruption cases\n\
      and incidents that require interventions"

if __name__ =='__main__':
    app.run(debug=True)
