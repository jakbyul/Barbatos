from django.shortcuts import render

from django.http import HttpResponse

from django.db import connection

# Create your views here.

def my_view(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT seq, `name` , DATEDIFF(NOW(), pickup_at) AS days, link,count FROM took order by days desc "
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        books = []
        for data in datas:
            row = {'seq': data[0],
                   'name': data[1],
                   'pick': data[2],
                   'link': data[3],
                   'new': data[4]}

            books.append(row)

    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    return render(request, 'myapp/index.html',{"books":books})

def my_html(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def dbtest(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT seq, `name` , DATEDIFF(NOW(), pickup_at) AS days FROM took order by days desc "
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        books = []
        for data in datas:
            row = {'seq': data[0],
                   'name': data[1],
                   'pick': data[2]}

            books.append(row)

    except:
        connection.rollback()
        print("Failed selecting in BookListView")


    return render(request, 'myapp/dbtest.html',{"books":books})
