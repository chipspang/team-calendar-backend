import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'team-calendar-secret-key-2024'
CORS(app)

# Database configuration - Railway-optimized
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Event model - simplified for Railway
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, default='')
    date = db.Column(db.String(10), nullable=False)  # Store as string to avoid timezone issues
    start_time = db.Column(db.String(8), default='09:00')  # Store as string HH:MM
    end_time = db.Column(db.String(8), default='10:00')    # Store as string HH:MM
    user_name = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String(50), default='blue')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'user_name': self.user_name,
            'color': self.color,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# Create tables - Railway-safe
try:
    with app.app_context():
        db.create_all()
        print("Database tables created successfully")
except Exception as e:
    print(f"Database creation error: {e}")

# Health check endpoint
@app.route('/')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Team Calendar API is running on Railway',
        'version': '2.0'
    })

# Get all events
@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        events = Event.query.all()
        return jsonify([event.to_dict() for event in events])
    except Exception as e:
        print(f"Error getting events: {e}")
        return jsonify({'error': 'Failed to fetch events'}), 500

# Create new event
@app.route('/api/events', methods=['POST'])
def create_event():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or not data.get('title') or not data.get('date') or not data.get('user_name'):
            return jsonify({'error': 'Missing required fields: title, date, user_name'}), 400
        
        # Create event with safe defaults
        event = Event(
            title=str(data['title'])[:255],  # Limit title length
            description=str(data.get('description', ''))[:1000],  # Limit description
            date=str(data['date']),  # Store as string (YYYY-MM-DD)
            start_time=str(data.get('start_time', '09:00')),
            end_time=str(data.get('end_time', '10:00')),
            user_name=str(data['user_name'])[:255],
            color=str(data.get('color', 'blue'))
        )
        
        db.session.add(event)
        db.session.commit()
        
        print(f"Event created: {event.title} on {event.date}")
        return jsonify(event.to_dict()), 201
        
    except Exception as e:
        print(f"Error creating event: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to create event'}), 500

# Update event
@app.route('/api/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({'error': 'Event not found'}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Update fields safely
        if 'title' in data:
            event.title = str(data['title'])[:255]
        if 'description' in data:
            event.description = str(data['description'])[:1000]
        if 'date' in data:
            event.date = str(data['date'])
        if 'start_time' in data:
            event.start_time = str(data['start_time'])
        if 'end_time' in data:
            event.end_time = str(data['end_time'])
        if 'user_name' in data:
            event.user_name = str(data['user_name'])[:255]
        if 'color' in data:
            event.color = str(data['color'])
        
        db.session.commit()
        print(f"Event updated: {event.title}")
        return jsonify(event.to_dict())
        
    except Exception as e:
        print(f"Error updating event: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to update event'}), 500

# Delete event
@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({'error': 'Event not found'}), 404
        
        db.session.delete(event)
        db.session.commit()
        
        print(f"Event deleted: {event_id}")
        return jsonify({'message': 'Event deleted successfully'})
        
    except Exception as e:
        print(f"Error deleting event: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to delete event'}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Railway-compatible startup
if __name__ == '__main__':
    # Get port from Railway environment variable
    port = int(os.environ.get('PORT', 5000))
    
    print(f"Starting Team Calendar API on port {port}")
    print("Environment: Railway Production")
    
    # Railway requires host='0.0.0.0' and debug=False
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,  # Never use debug=True on Railway
        threaded=True  # Handle multiple requests
    )

