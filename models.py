from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Users' favorite heroes
favorites_table = db.Table('favorites',
                           db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                           db.Column('hero_id', db.Integer, db.ForeignKey('heroes.id')))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    favorites = db.relationship('Hero', secondary='favorites_table')

    def __repr__(self):
        return f'<User {self.id} | {self.username}>'


class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    alignment = db.Column(db.String)
    race = db.Column(db.String)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    power = db.Column(db.Integer)
    durability = db.Column(db.Integer)
    combat = db.Column(db.Integer)
    speed = db.Column(db.Integer)


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///herotome'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()

    print('Connected to database, tables ready.')