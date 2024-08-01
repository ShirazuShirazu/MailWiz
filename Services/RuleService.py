from Models.rule import Rule
from main import getSession


def create_rule(session, cond_match_type, name):
    new_rule = Rule(cond_match_type=cond_match_type, name=name)
    session.add(new_rule)
    session.commit()
    return new_rule

def read_rule(session, rule_id):
    return session.query(Rule).filter_by(id=rule_id).first()

def update_rule(session, rule_id, cond_match_type=None, name=None):
    rule = session.query(Rule).filter_by(id=rule_id).first()
    if rule:
        if cond_match_type:
            rule.cond_match_type = cond_match_type
        if name:
            rule.name = name
        session.commit()
        return rule
    return None

def delete_rule(session, rule_id):
    rule = session.query(Rule).filter_by(id=rule_id).first()
    if rule:
        session.delete(rule)
        session.commit()
        return True
    return False

def list_rules(session):
    return session.query(Rule).all()

if __name__ == '__main__':
    session = getSession()

    new_rule = create_rule(session, 'AND', 'Sample Rule')
    print(f"Created Rule: {new_rule}")
