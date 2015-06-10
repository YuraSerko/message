from django.db import models
from django.db.models import F


class Messages(models.Model):
    id = models.AutoField(primary_key = True, blank=True)
    
    text = models.CharField(max_length=1000)
    
    date = models.DateTimeField(auto_now_add=True)
    
    lft = models.IntegerField()
    
    rgt = models.IntegerField()
    
    level = models.IntegerField()
    
    message = models.IntegerField(blank=True, null=True, )
    
    tree = models.IntegerField(blank=True, null=True)
    
    class Meta:
        unique_together = (("lft", "rgt", 'level'),)
    
    @staticmethod
    def create_new_message(m_id, text):
        if m_id != 0:
            #find parent
            parent_mes_obj = Messages.objects.get(id=m_id)
            #updates
            right_key =  parent_mes_obj.rgt
            left_key = parent_mes_obj.lft #
            left=left_key+1 #
            right=left+1#
            Messages.objects.filter(tree=parent_mes_obj.tree, lft__lt=parent_mes_obj.rgt, rgt__gte=parent_mes_obj.rgt, lft__lt=parent_mes_obj.rgt, ).update(rgt=F('rgt') + 2)
            
            #update uzli za roditelskim uzlom
            Messages.objects.filter(tree=parent_mes_obj.tree, lft__gte=left, rgt__gte=right, lft__gte=left,).update(lft=F('lft') + 2, rgt=F('rgt') + 2)
            
            #find message
            if parent_mes_obj.message == None:
                mes_obj = Messages.objects.get(id=parent_mes_obj.id)
            else:
                mes_obj = Messages.objects.get(id=parent_mes_obj.message)            
            
        else:
            left = 1
            right = 2
        #level
        c_level = 1 if m_id == 0 else parent_mes_obj.level + 1

        ms= Messages(
                               text=text,
                               lft=left,
                               rgt=right,
                               level=c_level,
                               message = mes_obj.id if m_id !=0 else None,
                             
                     )
        ms.save()
        if m_id == 0:
            ms.tree = ms.id
        else:
            ms.tree = parent_mes_obj.tree
        ms.save()
        return ms
        
#==========================================
from django.db.models.query import QuerySet
class MessageQuerySet(QuerySet):
    def single_filter(self, parent):
        return self.filter(tree=parent.tree, lft__gte=parent.lft, rgt__lte=parent.rgt,)
    
class LeftTreeManager(models.Manager):
    def get_queryset(self):
        return MessageQuerySet(self.model, using=self._db)
        #return super(LeftTreeManager, self).get_query_set().order_by('lft')

    def single_filter(self, parent):
        return self.get_queryset().single_filter(parent).order_by('lft')

    def show_comments_filter(self, parent):
        return self.get_queryset().single_filter(parent).exclude(id=parent.id).order_by('lft')


    
class MessagesLft(Messages):
    objects = models.Manager()
    lft_objects = LeftTreeManager() 
    class Meta:
        proxy = True
        


    