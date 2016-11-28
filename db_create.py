from blog import db
from models import BlogPost

# create the database and tables
db.create_all()

# insert
db.session.add(BlogPost('alchemyTitle', 'alchemyDescription'))
db.session.add(BlogPost('Great', 'Even greater'))

# commit changes
db.session.commit()