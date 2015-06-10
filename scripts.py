# coding: utf-8

from messages.models import Messages
print Messages











# 1000 сообщений

i = 1

while i<1001:
    t = str(i)+ ' MY message'
    print t
    Messages.create_new_message(0, t)
    i+=1

#==============================================




#1000 комментариев к 1 (1000) сообщению
i=1000
while i < 2001:
    t = str(i)+ ' comment'
    Messages.create_new_message(i,t)
    i=i+1








 
