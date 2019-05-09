from app import db


<<<<<<< HEAD
class Ireporter(db.Model):
    __tablename__ = 'irecords'
=======
class Ireporter2(db.Model):
    """This class represents the Ireporter2 table."""

    __tablename__ = 'records'
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, name):
        """initialize with name."""
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
<<<<<<< HEAD
        return Ireporter.query.all()
=======
        return Ireporter2.query.all()
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
<<<<<<< HEAD
        return "<Ireporter: {}>".format(self.name)
=======
        return "<Ireporter2: {}>".format(self.name)
>>>>>>> 8faf1f06d2757cd848f7a089ad5d166810f65d09
