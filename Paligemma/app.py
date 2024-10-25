from flask import Flask
from routers import routers

app = Flask(__name__)
app.secret_key = "supersecretkey"

routers.init_app(app)

if __name__ == '__main__':
    app.run()
    # app.run(host='10.20.201.51', port=5000)
