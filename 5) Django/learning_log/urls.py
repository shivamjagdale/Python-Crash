from django.urls import path 

from . import views 

app_name = "learning_log"

urlpatterns = [path("", views.index, name="index"),

               # Here we have list of topics 
               path("topics/", views.topics, name="topics"),

               # Here we have Topic and Entries 
               path("topics/<int:topic_id>", views.topic, name="topic"),

               # Form for Topic
               path("new_topic/", views.new_topic, name="new_topic"),

               # Form for Entry
               path("new_entry/<int:topic_id>", views.new_entry, name="new_entry"),

               # Page for editing entry
               path("edit_entry/<int:entry_id>", views.edit_entry, name="edit_entry")

               ]