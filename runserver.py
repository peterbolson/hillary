import os
from hillary import app

if __name__ == '__main__':
    if os.environ.get("FLASK_DEBUG") == 'True':
         app.debug = True
    app.run()
