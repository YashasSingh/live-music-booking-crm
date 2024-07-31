from flask_restful import Resource, reqparse
from .models import Booking, db

class BookingResource(Resource):
    def get(self):
        bookings = Booking.query.all()
        return {'bookings': [str(booking) for booking in bookings]}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('artist', required=True)
        parser.add_argument('venue', required=True)
        parser.add_argument('date', required=True)
        parser.add_argument('stage', required=False)
        args = parser.parse_args()

        booking = Booking(artist=args['artist'], venue=args['venue'], date=args['date'], stage=args.get('stage'))
        db.session.add(booking)
        db.session.commit()

        return {'message': 'Booking created', 'booking': str(booking)}, 201

def initialize_routes(api):
    api.add_resource(BookingResource, '/api/bookings')
