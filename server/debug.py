#!/usr/bin/env python3

from app import app
from models import db, Author, Post



if __name__ == '__main__':
    
    with app.app_context():
        # a1 = Author(
        #     name = "Ronald Johnsons",
        #     phone_number = "111111111100"
        # )
        # p1 = Post(
        #     title = "Top Test",
        #     content = "anjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnssanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnssanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnssanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnssanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnssanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnsanjfispfdjnss",
        #     category = "Fiction",
        #     summary = "1"
        # )
        author3 = Author(name="Jane Author", phone_number="123456789!")
        db.session.add(author3)
        db.session.commit()
        # import ipdb;  ipdb.set_trace()
