from pulsar.schema import Record, String, Integer, Float, Boolean


class UserActions(Record):
    user_id = Integer()
    post_id = Integer()
    action = String()
    time = String()
    gender = Integer()
    age = Integer()
    country = String()
    city = String()
    os = String()
    source = String()
    exp_group = Integer()