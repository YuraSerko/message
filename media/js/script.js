// js



var Messages = function () {};

Messages.show_single=function (message_id){	
	location.href = '/show_single/' + message_id +'/';}



Messages.show_comments=function (button_obj, message_id){
	Messages.hide_comments(button_obj, message_id);
	$.ajax({
		url: '/show_comments/'+message_id+'/',
		cache: false,
		async: true,
		success: function(html){
			//add block
			
			if ($(button_obj).parent().next().hasClass('comment_form')) {
				$(button_obj).parent().parent().next().after(html);
			}
			else{
				$(button_obj).parent().parent().after(html);
			}
			
			//rebuild button
			$(button_obj).text(' Скрыть коменнтарии ');
			$(button_obj).attr('onclick', 'Messages.hide_comments(this, '+message_id+')');
		}  
	});
}

Messages.hide_comments=function (button_obj, message_id){
	m_bl = $(button_obj).parent().parent().parent();
	$(m_bl).find('.comment').remove();
	//rebuild button
	$(button_obj).text(' Показать комментарии ');
	$(button_obj).attr('onclick', 'Messages.show_comments(this, '+message_id+')');
}



Messages.show_comment_form = function (button_obj, message_id) {
	$(button_obj).text("Отменить");
	$(button_obj).attr("onclick", "Messages.remove_comment_form(this, "+message_id+")");
	//$(button_obj).parent().after('<div class ="comment_form" style = "border: 1px solid blue; width:400px; height:50px"><div class ="input_com"><input></input><div class="but_confirm"><button onclick="add_comment(this)">confirm</button></div></div></div>');
	paste_html = '<div class ="comment_form" style = ""><div class ="input_com"><input></input><div class="but_confirm" style="text-align: center;"><button onclick="Messages.add_comment(this,' + message_id.toString()+')">Подтвердить</button></div></div></div>'
	$(button_obj).parent().after(paste_html);
}




Messages.remove_comment_form = function (button_obj, message_id){
	$(button_obj).text("Добавить комментарий");
	$(button_obj).attr("onclick", "Messages.show_comment_form(this, "+message_id+")");
	$(button_obj).parent().next().remove();
}



//ajax add comment
Messages.add_comment = function (confirm_button, message_id){
	
	//hide comment form 
	text = $(confirm_button).parent().parent().find('input').val();
	parent = $(confirm_button).parent().parent().parent().parent();
	button_cancel = $(parent).find('.button_block').find('button:first');
	
	//
	cur_url = location.href;
	if (cur_url.indexOf('show_single') !=-1)
		{
		cur_url_splitted = cur_url.split('/');
		t=cur_url_splitted[cur_url_splitted.length-2];
		var show_single = t;	
		}
	else {var show_single=false;}
	
	$.ajax({
		url: '/add_comment/'+message_id+'/',
		cache: false,
		async: true,
		type: 'POST',
		data: {show_single:show_single, text:text}, 
		success: function(html){
			//add comment to html
			$(parent).after(html);
			$(button_cancel).text("Добавить комментарий");
			$(button_cancel).attr("onclick", "Messages.show_comment_form(this, "+message_id+")");
			//remove block form
			$(confirm_button).parent().parent().parent().remove();
			
		}  
	});
}