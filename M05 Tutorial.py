'''Microsoft Windows [Version 10.0.22631.3085]
(c) Microsoft Corporation. All rights reserved.

C:\Users\johns>cd djangogirls

C:\Users\johns\djangogirls>myvenv\Scripts\activate

(myvenv) C:\Users\johns\djangogirls>python manage.py shell
C:\Users\johns\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe: can't open file 'C:\\Users\\johns\\djangogirls\\manage.py': [Errno 2] No such file or directory

(myvenv) C:\Users\johns\djangogirls>~/djangogirls$ python manage.py shell
'~' is not recognized as an internal or external command,
operable program or batch file.

(myvenv) C:\Users\johns\djangogirls>/djangogirls$ python manage.py shell
'/djangogirls$' is not recognized as an internal or external command,
operable program or batch file.

(myvenv) C:\Users\johns\djangogirls>/djangogirls python manage.py shell
'/djangogirls' is not recognized as an internal or external command,
operable program or batch file.

(myvenv) C:\Users\johns\djangogirls>cd Scripts
The system cannot find the path specified.

(myvenv) C:\Users\johns\djangogirls>cd myvenv

(myvenv) C:\Users\johns\djangogirls\myvenv>cd Scripts

(myvenv) C:\Users\johns\djangogirls\myvenv\Scripts> python manage.py shell
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)'''

>>> from blog.models import Post
>>> Post.objects.all()
<QuerySet []>
>>> from django.contrib.auth.models import User
>>>  User.objects.all()
  File "<console>", line 1
    User.objects.all()
IndentationError: unexpected indent
>>> User.objects.all()
<QuerySet [<User: johns>]>
>>> me = User.objects.get(username='ola')
'''Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\johns\djangogirls\myvenv\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\johns\djangogirls\myvenv\Lib\site-packages\django\db\models\query.py", line 649, in get
    raise self.model.DoesNotExist(
django.contrib.auth.models.User.DoesNotExist: User matching query does not exist.
>>> Post.objects.create(author=me, title='Sample title', text='Test')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'me' is not defined'''

>>> me = User.objects.get(username='johns')
>>> Post.objects.create(author=me, title='Sample title', text='Test')
<Post: Sample title>
>>> Post.objects.all()
<QuerySet [<Post: Sample title>]>
>>> Post.objects.create(author=me, title='Example Title', text='Test')
<Post: Example Title>
>>> Post.objects.all()
<QuerySet [<Post: Sample title>, <Post: Example Title>]>
>>> Post.objects.filter(author=me)
<QuerySet [<Post: Sample title>, <Post: Example Title>]>
>>> Post.objects.filter(title__contains='title')
<QuerySet [<Post: Sample title>, <Post: Example Title>]>
>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet []>
>>> post = Post.objects.get(title="Sample title")
>>> post.publish()
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: Sample title>]>
>>> Post.objects.order_by('created_date')
<QuerySet [<Post: Sample title>, <Post: Example Title>]>
>>> Post.objects.order_by('-created_date')
<QuerySet [<Post: Example Title>, <Post: Sample title>]>
>>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
<QuerySet [<Post: Sample title>]>
>>> http://127.0.0.1:8000/