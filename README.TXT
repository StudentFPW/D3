------------------------------------------------------------------------------------------------------------------------

В этом задании я создал для статей и новостей отдельные страницы = /news/, /articles/.

------------------------------------------------------------------------------------------------------------------------

D3\NewsPortal\news\urls.py
Создать новую страницу с адресом /news/, на которой должен выводиться список всех новостей. +

------------------------------------------------------------------------------------------------------------------------

D3\NewsPortal\templates\flatpages\articles.html
D3\NewsPortal\templates\flatpages\news.html
Вывести все статьи в виде заголовка, даты публикации и первых 20 символов текста. +

------------------------------------------------------------------------------------------------------------------------

D3\NewsPortal\news\views.py
Новости должны выводиться в порядке от более свежей к самой старой. +

------------------------------------------------------------------------------------------------------------------------

D3\NewsPortal\news\urls.py
Сделать отдельную страницу для полной информации о статье /news/<id новости>. +

------------------------------------------------------------------------------------------------------------------------

D3\NewsPortal\templates\flatpages\article.html
D3\NewsPortal\templates\flatpages\new.html
На этой странице должна быть вся информация о статье. Название, текст и дата загрузки в формате день.месяц.год. +

------------------------------------------------------------------------------------------------------------------------

D3\NewsPortal\news\templatetags\custom_filter3.py
Написать собственный фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*». +

Текст/(фильтр censor) можно проверить на этой странице:
http://127.0.0.1:8000/news/3

------------------------------------------------------------------------------------------------------------------------

D3\NewsPortal\templates\flatpages\index.html
Все новые страницы должны использовать шаблон default.html как основу. +

Я взял название index.html в место default.html ↑

------------------------------------------------------------------------------------------------------------------------