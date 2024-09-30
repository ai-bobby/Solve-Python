text ='''
For several generations, stories from Africa have traditionally been passed down 
by word of mouth. Often, after a hard day's work, the adults would gather the children 
together by moonlight, around a village fire and tell stories. This was traditionally called 
'Tales by Moonlight'. Usually, the stories are meant to prepare young people for life, and so
 each story taught a lesson or moral. 
'''

serch = lambda text,sentens : text[text.find(sentens) -25 : text.find(sentens) + 25] if sentens in text else -1

print(serch(text,'adults'))

print(round(2554.2131,-1))