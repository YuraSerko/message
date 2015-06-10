from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf import settings
from messages.views import MessageTape, ShowSingle, ShowComments, AddMessage, AddComment


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'messages_tape.views.home', name='home'),
    # url(r'^messages_tape/', include('messages_tape.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
   
)


urlpatterns += patterns('messages.views',
    #url(r'^$', 'messages_tape', name = 'message_tape' ),
    url(r'^$', MessageTape.as_view()),
    #url(r'^show_single/(?P<message_id>\d+)/$', 'show_single', name='show_single'),
    url(r'^show_single/(?P<message_id>\d+)/$', ShowSingle.as_view()),
    #url(r'^show_comments/(?P<message_id>\d+)/$', 'show_comments', name = 'show_comments'),
    url(r'^show_comments/(?P<message_id>\d+)/$', ShowComments.as_view()),
    #url(r'^add_comment/(?P<message_id>\d+)/$', 'add_comment', name = 'add_comment'),
    url(r'^add_comment/(?P<message_id>\d+)$', AddComment.as_view()),
    #url(r'^add_message/$', 'add_message', name='add_message'),
    url(r'^add_message/$', AddMessage.as_view(success_url='/')),
)