from models import Room, Hotel, Booking
from database import Database


class HotelSystem:
    def __init__(self, db):
        self.db = db

    def register_hotel(self, name):
        # Requirements:
        #   - Insert new hotel record into the database
        #   - Return a Hotel model instance by calling the model's create method with the query result

        # Remove the pass statement below and add your implementation there ...
        register_rec = self.db.bookings.insert(name=name)
        return register_rec

    def add_room(self, hotel_id, **params):
        # Requirements:
        #   - Insert new room record into the database
        #   - Return a Room model instance by calling the model's create method with the query result
        add_rec = self.db.bookings.insert(hotel_id=hotel_id, **params)

        # Remove the pass statement below and add your implementation there ...
        return add_rec

    def get_room(self, room_id):
        # Requirements:
        #   - Select a room with the room_id argument from the database
        #   - Return None if query results is empty
        #   - Otherwise,
        # - Return a Room model instance by calling the model's create method with the first record in the query
        # results

        # Remove the pass statement below and add your implementation there ...
        get_rec = self.db.bookings.select(room_id=room_id)
        return get_rec

    def book_room(self, room_id, **params):
        # Requirements:
        #   - Insert new booking record into the database
        #   - Return a Booking model by calling the model's create method instance with the query result
        book_rec = self.db.bookings.insert(room_id=room_id, **params)
        # Remove the pass statement below and add your implementation there ...
        return book_rec
