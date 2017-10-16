"""Defines URL patterns for learninglogs"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^home/$', views.index, name='index'), # Three args: 1 - regular expression. r tells python to interpret the
                                                # following string as a raw string, and the quotes show where it begins and
                                                # ends. The caret tells Python to look for the beginning of the string, and the
                                                # dollar sign means look for the end of the string. EG, this expression tells python
                                                # to look for a URL with a string of nothing.
                                                # 2 - which view funtion to call.
                                                # 3 - the name if the urlpattern for future reference
    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    # detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), # the second part of the expression /(?P<topic_id>\d+)/
                                                                    # matches an integer between two forwards slashes and stores
                                                                    # it in topic_id. The parentheses surrounding it stores the
                                                                    # value from the URL; the ?P<topic_id> stores that value
                                                                    # in topic_id; finally, the \d+ expression matches any number of
                                                                    # digits that appear between the forwards slashes. Critically, when
                                                                    # Django finds a URL matching this structure, it calls topic() and
                                                                    # passes topic_id as an argument, along with the original request.
    # page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # page for adding a new entry to a topic
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry, name='edit_entry'),
]
