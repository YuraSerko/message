# Create your views here.
from messages.models import Messages, MessagesLft
from messages.forms import New_message_form
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

  

class MessageTape(TemplateView):
    template_name = 'message_tape.html'
    def get_context_data(self, **kwargs):
        context = super(MessageTape, self).get_context_data(**kwargs)
        ms_objs = Messages.objects.filter(message__isnull=True).order_by('-date').values('id', 'date', 'text') 
        context['ms_objs'] = ms_objs
        return context


class ShowSingle(TemplateView):
    template_name = 'show_single.html'
    def get_context_data(self, **kwargs):
        context = super(ShowSingle, self).get_context_data(**kwargs)
        parent = Messages.objects.get(id=kwargs['message_id'])
        context['first_mes_level'] = parent.level
        context['mes_objs'] = MessagesLft.lft_objects.single_filter(parent).values('id','level', 'text', 'date')
        return context




class ShowComments(TemplateView): 
    template_name = 'show_comments.html'
    def get_context_data(self, **kwargs):
        context = super(ShowComments, self).get_context_data(**kwargs)
        parent = Messages.objects.get(id=kwargs['message_id'])
        context['first_mes_level'] = parent.level
        context['mes_objs'] = MessagesLft.lft_objects.show_comments_filter(parent).values('id','level', 'text', 'date')
        return context


    
class AddComment(TemplateView):
    template_name = 'show_comments.html'
    def post(self, request, **kwargs):
        kwargs['show_single'] = request.POST.get("show_single")
        kwargs['text'] = request.POST.get('text')     
    def get_context_data(self, **kwargs):
        context = super(AddComment, self).get_context_data(**kwargs)
        message_obj = Messages.create_new_message(kwargs['message_id'], kwargs['text'])
        context['message_obj'] = [message_obj]
        if kwargs['show_single'] =='false':
            context['show_single'] = False    
        else:
            parent = Messages.objects.get(id= int(kwargs['show_single']))
            context['show_single'] = parent.level
        return context



class AddMessage(FormView):
    template_name = 'add_message.html'
    form_class = New_message_form
    def form_valid(self, form):
        text = form.cleaned_data['text']
        Messages.create_new_message(0,text)
        return super(AddMessage, self).form_valid(form)
        
    