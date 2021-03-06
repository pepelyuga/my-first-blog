""" blog.urls
Создай новый пустой файл blog/urls.py. Отлично! Добавь в него следующие две строки:

blog/urls.py
from django.conf.urls import url
from . import views
Так мы импортировали функцию url Django и все views (представления)
из приложения blog (у нас их пока нет, но через минуту они появятся!)

После этого мы можем добавить наш первый URL-шаблон:

blog/urls.py
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
Как ты можешь заметить, мы связали view под именем post_list с URL-адресом ^$.
Это регулярное выражение будет соответствовать ^ (началу) и следующему $ (концу),
т.е. пустой строке. Это правильно, потому что для обработчиков URL в Django
'http://127.0.0.1:8000/' не является частью URL. Этот шаблон скажет Django,
что views.post_list — это правильное направление для запроса к твоему веб-сайту по
адресу 'http://127.0.0.1:8000/'.

Последняя часть name='post_list' — это имя URL, которое будет использовано,
чтобы идентифицировать его. Оно может быть таким же, как имя представления
(англ. view), а может и чем-то совершенно другим. Мы будем использовать именованные
URL позднее в проекте, поэтому важно указывать их имена уже сейчас.
Мы также должны попытаться сохранить имена URL-адресов уникальными и легко
запоминающимися.

Если сейчас ты попытаешься открыть страницу http://127.0.0.1:8000/ в браузере,
то увидишь сообщение о том, что веб-страница недоступна.
Это произошло потому, что сервер (помнишь, как мы набирали runserver?)
перестал обрабатывать запросы. Чтобы понять почему, открой окно своей командной строки.

Ошибка

В твоей командной строке появилось сообщение об ошибке,
но не беспокойся — оно, на самом деле, довольно полезно.

Ты можешь прочесть, что не существует атрибута с именем 'postlist' — _
no attribute 'post_list'. Это название представления, которое Django пытается найти
и использовать, но мы же его ещё не создали. В данный момент раздел /admin/ тоже
не будет работать. Не беспокойся, мы этим займёмся."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]