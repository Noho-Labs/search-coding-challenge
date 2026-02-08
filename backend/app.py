from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable tracking modifications for performance
db = SQLAlchemy(app)

# Define a model (e.g., User)
class Cities(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    country = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(), nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<City {self.name}>'


@app.route('/')
def index():
    return "Flask with MySQL is set up!"

@app.route('/cities_count')
def cities_count():
    cities = Cities.query.all()
    return {"count": len(cities)}

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
