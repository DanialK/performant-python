from flask_app import app
import bjoern

if __name__ == "__main__":
    # app.run()
    bjoern.run(app, host='0.0.0.0', port=8080)