from Models.action import Action

def create_action(session, action_type, destination, rule_id):
    new_action = Action(action_type=action_type, destination=destination, rule_id=rule_id)
    session.add(new_action)
    session.commit()
    return new_action

def get_action(session, action_id):
    return session.query(Action).filter_by(id=action_id).first()

def get_actions_by_rule(session, rule_id):
    return session.query(Action).filter_by(rule_id=rule_id).all()

def update_action(session, action_id, action_type=None, destination=None, rule_id=None):
    action = session.query(Action).filter_by(id=action_id).first()
    if action_type:
        action.action_type = action_type
    if destination:
        action.destination = destination
    if rule_id:
        action.rule_id = rule_id
    session.commit()
    return action

def delete_action(session, action_id):
    action = session.query(Action).filter_by(id=action_id).first()
    if action:
        session.delete(action)
        session.commit()
        return True
    return False
