from flask import Blueprint, jsonify, request
from datetime import datetime, date, time
from src.models.event import Event
from src.models.user import db

event_bp = Blueprint('event', __name__)

@event_bp.route('/events', methods=['GET'])
def get_events():
    # Get optional query parameters for filtering
    year = request.args.get('year', type=int)
    month = request.args.get('month', type=int)
    
    query = Event.query
    
    if year and month:
        # Filter events for specific month/year
        start_date = date(year, month, 1)
        if month == 12:
            end_date = date(year + 1, 1, 1)
        else:
            end_date = date(year, month + 1, 1)
        query = query.filter(Event.date >= start_date, Event.date < end_date)
    
    events = query.order_by(Event.date, Event.start_time).all()
    return jsonify([event.to_dict() for event in events])

@event_bp.route('/events', methods=['POST'])
def create_event():
    try:
        data = request.json
        
        # Parse date and time strings
        event_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        start_time = datetime.strptime(data['start_time'], '%H:%M').time()
        end_time = datetime.strptime(data['end_time'], '%H:%M').time()
        
        event = Event(
            title=data['title'],
            description=data.get('description', ''),
            date=event_date,
            start_time=start_time,
            end_time=end_time,
            created_by=data['created_by'],
            color=data.get('color', '#2563eb')
        )
        
        db.session.add(event)
        db.session.commit()
        return jsonify(event.to_dict()), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@event_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event.to_dict())

@event_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    try:
        event = Event.query.get_or_404(event_id)
        data = request.json
        
        if 'title' in data:
            event.title = data['title']
        if 'description' in data:
            event.description = data['description']
        if 'date' in data:
            event.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        if 'start_time' in data:
            event.start_time = datetime.strptime(data['start_time'], '%H:%M').time()
        if 'end_time' in data:
            event.end_time = datetime.strptime(data['end_time'], '%H:%M').time()
        if 'created_by' in data:
            event.created_by = data['created_by']
        if 'color' in data:
            event.color = data['color']
        
        event.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify(event.to_dict())
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@event_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return '', 204

