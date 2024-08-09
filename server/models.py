from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators
    @validates("name")
    def validate_name(self,key,value):
        all_auth =Author.query.all()
        auth_name = []
        for auth in all_auth:
            auth_name.append(auth.name)
        if value and value not in auth_name:
            return value
        else:
            raise ValueError("Not valid name")
    

    @validates("phone_number")
    def validates_phone(self,key,value):
        valid_num = ["1","2","3","4","5","6","7","8","9","0"]
        if len(value) == 10 and value.isdigit():
            return value
            for letter in value:
                if letter not in valid_num:
                    raise ValueError("Not valid phone number")
            return value
        else:
            raise ValueError("Not valid phone number")
        
    
    
            



    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates("content","summary")
    def validates_cs(self,key,value):
        if key == "content":
            if 250<=len(value):
                return value
        elif key == "summary":
            if len(value) <= 250:
                return value
        raise ValueError(f"Not valid {key}")
    
    @validates("category")
    def validate_cat(self,key,value):
        if value in ["Fiction","Non-Fiction"]:
            return value
        else:
            raise ValueError("Not valid category")
        
    @validates("title")
    def validate_title(self,key,value):
        clickbait_phrases = ["Won't Believe","Secret","Top","Guess"]
        for phrase in clickbait_phrases:
            if phrase in value:
                return value
        raise ValueError("Make it more clickbaitable")


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
