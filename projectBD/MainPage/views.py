from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

def index(request):
    offset = request.GET.get('offset', 0)
    limit = request.GET.get('limit', 20)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM get_new_offers() OFFSET %s LIMIT %s', [offset, limit])
        recent_offers = cursor.fetchall()
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        # request is AJAX
        return JsonResponse(list(recent_offers), safe=False)
    else:
        # request is not AJAX
        context = {'recent_offers': recent_offers}
        return render(request, 'MainPage/index.html', context)



def search(request):
    search_term = request.GET.get('search_term', '')
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM get_cars_by_filter(%s, %s, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null, Null)', [search_term, search_term])
        search_results = cursor.fetchall()
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        # request is AJAX
        return JsonResponse(list(search_results), safe=False)
    else:
        # request is not AJAX
        context = {'search_results': search_results}
        return render(request, 'MainPage/index.html', context)
