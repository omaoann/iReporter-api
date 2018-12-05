
from app import create_app

app = create_app(config_name="development")

@app.route('/')
def landing_page():
    
    return "Welcome to iReporter.\n\
      A place to report all corruption cases\n\
      and incidents that require interventions"

if __name__ =='__main__':
    app.run(debug=True)
