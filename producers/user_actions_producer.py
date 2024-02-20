import time
import datetime
from faker import Faker
from wonderwords import RandomWord
from connectors import client, user_actions_producer
from services.data2psql import insert_into_db

try:
    fake = Faker()
    rw = RandomWord()
    while True:
        new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        country = rw.word(include_parts_of_speech=["nouns"])
        city = rw.word(include_parts_of_speech=["nouns"])
        price = fake.random_int(min=10, max=10000)
        gender = fake.random_element(elements=(1, 0))
        user_id = fake.random_int(min=1, max=10000)
        age = fake.random_int(min=10, max=50)
        post_id = fake.random_int(min=10, max=10000)
        action = fake.random_element(elements=("view", "like"))
        os = fake.random_element(elements=("Android", "IOS"))
        source = fake.random_element(elements=("organic", "ads"))
        exp_group = fake.random_int(min=0, max=4)
        time_created = str(new_date)

        data = {
            "user_id": user_id,
            "post_id": post_id,
            "action": action,
            "time": new_date,
            "gender": gender,
            "age": age,
            "country": country,
            "city": city,
            "os": os,
            "source": source,
            "exp_group": exp_group
        }
        insert_into_db('user_actions_2', data)
        print(data)
        time.sleep(5)
except KeyboardInterrupt:
    print("Stop")

finally:
    user_actions_producer.close()
    client.close()
