from django.db import models
from mongoengine import  *

class ArtiInfo(Document):
    date = StringField()
    door_name = StringField()
    use_name = StringField()
    use_type = StringField()
    door_open = StringField()
    user_id = StringField()
    door_adress = StringField()
    car_id=StringField()
    meta ={'collection':'Info'}

# class ArtiInfo(Document):
#     date = StringField()
#     door_name = StringField()
#     use_name = StringField()
#     use_type = StringField()
#     door_open = StringField()
#     user_id = StringField()
#     door_adress = StringField()
#     car_id=StringField()
#     meta ={'collection':'infoinfo'}
# for i  in ArtiInfo.objects:
#     print(i.use_name)

# name_list = []
# for i in ArtiInfo.objects():
#     name_list.append(i['use_name'])
#     name_index = list(set(name_list))




