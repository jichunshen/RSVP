from django.conf.urls import url
from . import views

app_name = 'event'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.question, name='question'),
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^(?P<event_id>[0-9]+)/add_text/$', views.add_text, name='add_text'),
    url(r'^(?P<event_id>[0-9]+)/plus_one/$', views.plus_one, name='plus_one'),
    url(r'^(?P<event_id>[0-9]+)/add_multiple/$', views.add_multiple, name='add_multiple'),
    url(r'^(?P<event_id>[0-9]+)/add_multiple/(?P<question_id>[0-9]+)/$', views.add_choice, name='add_choice'),
    url(r'^(?P<event_id>[0-9]+)/question_detail/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
    url(r'^(?P<event_id>[0-9]+)/multi_question_detail/(?P<question_id>[0-9]+)/$', views.multi_question_detail, name='multi_question_detail'),
    url(r'^(?P<event_id>[0-9]+)/answer_question/(?P<question_id>[0-9]+)/$', views.answer_question, name='answer_question'),
    url(r'^(?P<event_id>[0-9]+)/answer_multiple/(?P<question_id>[0-9]+)/$', views.answer_multiple, name='answer_multiple'),
    url(r'^(?P<event_id>[0-9]+)/question_detail/(?P<question_id>[0-9]+)/guest_modify/$', views.guest_modify, name='guest_modify'),
    url(r'^(?P<question_id>[0-9]+)/vendor_cansee/$', views.vendor_cansee, name='vendor_cansee'),
    url(r'^(?P<event_id>[0-9]+)/delete_event/$', views.delete, name='delete'),
    url(r'^(?P<event_id>[0-9]+)/add_user/$', views.add_user, name='add'),
    url(r'^(?P<event_id>[0-9]+)/accept_event/$', views.accept, name='accept'),
    url(r'^(?P<event_id>[0-9]+)/question_delete/(?P<question_id>[0-9]+)/$', views.question_delete, name='question_delete'),
    url(r'^(?P<event_id>[0-9]+)/question_edit/(?P<question_id>[0-9]+)/$', views.question_edit, name='question_edit'),
    url(r'^(?P<event_id>[0-9]+)/multiple_edit/(?P<question_id>[0-9]+)/$', views.multiple_edit, name='multiple_edit'),
    url(r'^(?P<event_id>[0-9]+)/edit_choice/(?P<question_id>[0-9]+)/(?P<choice_id>[0-9]+)/$', views.edit_choice, name='edit_choice'),
  
    #url(r'^(?P<album_id>[0-9]+)/create_question/$', views.create_question, name='create_question'),
    #url(r'^(?P<event_id>[0-9]+)/edit_question/(?P<question_id>[0-9]+)/$', views.edit_question, name='edit_question'),
    #url(r'^(?P<album_id>[0-9]+)/delete_event/$', views.delete_event, name='delete_event'),

]