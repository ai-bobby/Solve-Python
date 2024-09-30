# def tag_html(func):
#     def inner(*args):
#         return '<!DOCTYPE html>' +'\n' + "<html> "+'\n' + text +'\n' + "</html>"
#     return inner


# def tag_head(func):
#     def inner(*args):
#         return '\n' + "<head> "+'\n' + func(*args) +'\n' + "</head>"
#     return inner


# def tag_title(func):
#     def inner(*args):
#         return "<title>" + func(*args) + "</title>"
#     return inner


# @tag_html
# @tag_head
# @tag_title

# def Text(text):
#     return text
# '''
# # <!DOCTYPE html>
# <html>
# <head>
# <title>Page Title</title>
# </head>
# </html>
# '''
# text = 'Babak'
# # text = "<title>" + text + "</title>"
# # text += '\n' + "<head> "+'\n' + text +'\n' + "</head>"

# print(Text(text))

# text_one = open("text_one.html",'w')
# text_one.write(Text(text))

# ----------------------------------------------------------------------------------------
# def addGl(func):
#     def inner(*args):
#         return "<u>"+func(*args)+"</u>"
#     return inner


# def addSq(func):
#     def inner(*args):
#         return "<i>"+func(*args)+"</i>"
#     return inner

# def addStar(func):
#     def inner(*args):
#         return "<b>"+func(*args)+"</b>"
#     return inner

# @addGl
# @addSq
# @addStar
# def getText(str1):
#     return str1

# h=getText("mehdi")
# f1=open("page1.html","w")
# f1.write(getText("mehdi"))
# f1.close()