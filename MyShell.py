import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings") #name of project, not app

import django
django.setup()

from learning_logs.models import Topic

topics = Topic.objects.all()

for topic in topics:
    print("Topic ID:", topic.id, "Topic:", topic)

t = Topic.objects.get(id=1) #get is like WHERE id=1
#print(t.text)
#print(t.date)

entries = t.entry_set.all() #access entries related to certain topic b/c there's an FK relationship, use lower case model_set.all

for entry in entries:
    print(entry)