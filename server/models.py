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
    @validates('phone_number')
    def validate_phone(self,key,value):
        valid_int = ("0","1","2","3","4","5","6","7","8","9")
        if len(value) == 10:
            for i in value:
                if i not in valid_int:
                    raise ValueError("Please input a number")
            return value
        else:
            print(value)
            raise ValueError("Not a real phone number, needs to have 10 digits")
        
    @validates('name')
    def validate_name(self,key,value):
        all_authors = Author.query.all()
        if value:
            for author in all_authors:
                if author.name == value:
                    raise ValueError("Name already exists")
            return value
        else:
            raise ValueError("Please input a name")

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
    def validate_info(self,key,value):
        if (key=="content" and 250<=len(value)) or (key=="summary" and len(value)<=250):
            return value
        else:
            raise ValueError(f"{key} does not have the right length")

    @validates("category")
    def validate_category(self,key,value):
        valid_categories = ("Fiction","Non-Fiction")
        if value in valid_categories:
            return value
        else:
            raise ValueError("Not a valid category")

    @validates("title")
    def validate_title(self,key,value):
        clickbait = ("Won't Believe","Secret","Top","Guess")
        # Loop through clickbait words,
        for cb in clickbait:
            if cb in value:
                return value
        raise ValueError("Not clickbaity enough")
            
        # Check if they exist in value
        # Return value


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
