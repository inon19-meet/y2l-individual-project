from model import Base, User, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_User(username, password):
    user_object = User(name=username,
     password=password)
    session.add(user_object)
    session.commit()

def query_all_users():
    users = session.query(
    	User).all()
    return users

def query_user_by_name(username):
	name = session.query(
		User).filter_by(name=username).first()
	return name

def query_by_name_and_password(username, password):
    return session.query(User).filter_by(name = username, password = password).first()

def delete_user_by_id(user_id):
    post = session.query(User).filter_by(id_table=user_id).delete()
    session.commit()

def query_user_by_id(user_id):
    user = session.query(
        User).filter_by(id_table=user_id).first()
    return user

def delete_all_users():
    session.query(User).delete()

def add_Post(post_string):
    post_object = Post(post_string=post_string)
    session.add(post_object)
    session.commit()

def query_all_posts():
    posts = session.query(
        Post).all()
    return posts

def query_post_by_id(post_id):
    post = session.query(Post).filter_by(id_table=post_id).first()
    return post

def delete_all_posts():
    session.query(Post).delete()
    session.commit

def delete_post_by_id(post_id):
    post = session.query(Post).filter_by(id_table=post_id).delete()
    session.commit()