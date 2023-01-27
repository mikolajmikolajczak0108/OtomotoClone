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
        context = {'recent_offers': recent_offers, 'offers': filter_cars(), 'brands': get_brands()}
        return render(request, 'MainPage/index.html', context)

def filter_cars():
    with connection.cursor() as cursor:
        cursor.execute('SELECT brand_name FROM "Cars"."get_cars_by_filter"()')
        brands = cursor.fetchall()
        cursor.execute('SELECT model_name FROM "Cars"."get_cars_by_filter"()')
        models = cursor.fetchall()
        cursor.execute('SELECT generation_year FROM "Cars"."get_cars_by_filter"()')
        generation_years = cursor.fetchall()
        cursor.execute('SELECT price_netto FROM "Cars"."get_cars_by_filter"()')
        prices_netto = cursor.fetchall()
        cursor.execute('SELECT mileage FROM "Cars"."get_cars_by_filter"()')
        mileage = cursor.fetchall()
        cursor.execute('SELECT is_garaged FROM "Cars"."get_cars_by_filter"()')
        is_garaged = cursor.fetchall()
        cursor.execute('SELECT is_damaged FROM "Cars"."get_cars_by_filter"()')
        is_damaged = cursor.fetchall()
        cursor.execute('SELECT is_after_accident FROM "Cars"."get_cars_by_filter"()')
        is_after_accident = cursor.fetchall()
        cursor.execute('SELECT is_cruise_control FROM "Cars"."get_cars_by_filter"()')
        is_cruise_control = cursor.fetchall()
        cursor.execute('SELECT is_usb_port FROM "Cars"."get_cars_by_filter"()')
        is_usb_port = cursor.fetchall()
        cursor.execute('SELECT is_abs FROM "Cars"."get_cars_by_filter"()')
        is_abs = cursor.fetchall()
        cursor.execute('SELECT is_bluetooth FROM "Cars"."get_cars_by_filter"()')
        is_bluetooth = cursor.fetchall()
        cursor.execute('SELECT is_gps FROM "Cars"."get_cars_by_filter"()')
        is_gps = cursor.fetchall()
        cursor.execute('SELECT air_conditioning_type FROM "Cars"."get_cars_by_filter"()')
        air_conditioning_types = cursor.fetchall()
        cursor.execute('SELECT roof_type_id FROM "Cars"."get_cars_by_filter"()')
        roof_types = cursor.fetchall()
        cursor.execute('SELECT upholstery_id FROM "Cars"."get_cars_by_filter"()')
        upholsteries = cursor.fetchall()
        offers = {}
        for i in range(len(brands)):
            offers["offer" + str(i+1)] = [brands[i][0], models[i][0], generation_years[i][0],prices_netto[i][0], mileage[i][0], is_garaged[i][0], is_damaged[i][0], is_after_accident[i][0], is_cruise_control[i][0], is_usb_port[i][0], is_abs[i][0], is_bluetooth[i][0], is_gps[i][0], air_conditioning_types[i][0], roof_types[i][0], upholsteries[i][0]]
    return offers

def get_brands():
    with connection.cursor() as cursor:
        cursor.execute('SELECT brand FROM "Cars"."brands"')
        brands = cursor.fetchall()
    return brands