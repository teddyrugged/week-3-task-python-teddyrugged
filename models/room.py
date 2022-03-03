from model import Model
from hotel import Hotel


class Room(Model):
    _id = None
    hotel_id = None
    price = None
    capacity = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes

        instance = cls()

        # Add your implementation here ...
        instance._id = record['_id']
        instance.hotel_id = record['hotel_id']
        instance.price = record['price']
        instance.capacity = record['capacity']

        return instance

    def hotel(self, db):
        # Requirements:
        hotel_data = db.hotels.select(_id=self.hotel_id)
        if not hotel_data:
            return None
        else:
            return Hotel.create(hotel_data[0])
        #   - Select hotels from the database that has the hotel_id set on this model as self.hotel_id
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Hotel model instance by calling the model's create method with the first record in the query
        #   results

        # Remove the pass statement below and add your implementation there ...

