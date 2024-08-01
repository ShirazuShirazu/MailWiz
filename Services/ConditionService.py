from Models.rule import Rule
from main import getSession
from Models.condition import Condition

def create_condition(session, field, predicate, value, rule_id):
    new_condition = Condition(field=field, predicate=predicate, value=value, rule_id=rule_id)
    session.add(new_condition)
    session.commit()
    return new_condition

def read_condition(session, condition_id):
    return session.query(Condition).filter_by(id=condition_id).first()

def read_conditions_for_rule(session, rule_id):
    return session.query(Condition).filter_by(rule_id=rule_id).all()

def update_condition(session, condition_id, field=None, predicate=None, value=None, rule_id=None):
    condition = session.query(Condition).filter_by(id=condition_id).first()
    if condition:
        if field:
            condition.field = field
        if predicate:
            condition.predicate = predicate
        if value:
            condition.value = value
        if rule_id:
            condition.rule_id = rule_id
        session.commit()
        return condition
    return None

def delete_condition(session, condition_id):
    condition = session.query(Condition).filter_by(id=condition_id).first()
    if condition:
        session.delete(condition)
        session.commit()
        return True
    return False

def list_conditions(session):
    return session.query(Condition).all()

if __name__ == '__main__':
    session = getSession()

    conditions = read_conditions_for_rule(session, 1)
    # [<Condition(field=From, predicate=equals, value=mohamedshiraz101@gmail.com, rule_id=1)>,
    # <Condition(field=Subject, predicate=contains, value=Test, rule_id=1)>]
    print(conditions)
