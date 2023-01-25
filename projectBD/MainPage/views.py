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



def filter(request):
    brand_name = request.GET.get('brand_name', None)
    model_name = request.GET.get('model_name', None)
    generation_year = request.GET.get('generation_year', None)
    price_netto = request.GET.get('price_netto', None)
    mileage = request.GET.get('mileage', None)
    is_garaged = request.GET.get('is_garaged', None)
    is_damaged = request.GET.get('is_damaged', None)
    is_after_accident = request.GET.get('is_after_accident', None)
    is_electric_seats = request.GET.get('is_electric_seats', None)
    is_cruise_control = request.GET.get('is_cruise_control', None)
    is_usb_port = request.GET.get('is_usb_port', None)
    is_abs = request.GET.get('is_abs', None)
    is_bluetooth = request.GET.get('is_bluetooth', None)
    is_gps = request.GET.get('is_gps', None)
    air_conditioning_type = request.GET.get('air_conditioning_type', None)
    roof_type_id = request.GET.get('roof_type_id', None)
    upholstery_id = request.GET.get('upholstery_id', None)
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM get_cars_by_filter(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [brand_name, model_name, generation_year, price_netto, mileage, is_garaged, is_damaged, is_after_accident,
             is_electric_seats, is_cruise_control, is_usb_port, is_abs, is_bluetooth, is_gps, air_conditioning_type,
             roof_type_id, upholstery_id])
        filtered_offers = cursor.fetchall()
        context = {'filtered_cars': filtered_offers}
        return JsonResponse(context)

def get_filter_options(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT DISTINCT brand FROM "Cars".brands ORDER BY brand')
        brands = cursor.fetchall()
        cursor.execute('SELECT DISTINCT model FROM "Cars".models ORDER BY model')
        models = cursor.fetchall()
        cursor.execute('SELECT DISTINCT generation_year FROM "Cars".offers ORDER BY generation_year')
        generation_years = cursor.fetchall()
        cursor.execute('SELECT DISTINCT price_netto FROM "Cars".offers ORDER BY price_netto')
        prices_netto = cursor.fetchall()
        cursor.execute('SELECT DISTINCT mileage FROM "Cars".offers ORDER BY mileage')
        mileages = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_garaged FROM "Cars".offers ORDER BY is_garaged')
        is_garaged = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_damaged FROM "Cars".offers ORDER BY is_damaged')
        is_damaged = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_after_accident FROM "Cars".offers ORDER BY is_after_accident')
        is_after_accident = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_electric_seats FROM "Cars".offers ORDER BY is_electric_seats')
        is_electric_seats = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_cruise_control FROM "Cars".offers ORDER BY is_cruise_control')
        is_cruise_control = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_usb_port FROM "Cars".offers ORDER BY is_usb_port')
        is_usb_port = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_abs FROM "Cars".offers ORDER BY is_abs')
        is_abs = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_bluetooth FROM "Cars".offers ORDER BY is_bluetooth')
        is_bluetooth = cursor.fetchall()
        cursor.execute('SELECT DISTINCT is_gps FROM "Cars".offers ORDER BY is_gps')
        is_gps = cursor.fetchall()
        cursor.execute('SELECT DISTINCT air_conditioning_type FROM "Cars".offers ORDER BY air_conditioning_type')
        air_conditioning_type = cursor.fetchall()
        cursor.execute('SELECT DISTINCT roof_type_id FROM "Cars".offers ORDER BY roof_type_id ASC')
        roof_types = cursor.fetchall()
        cursor.execute('SELECT DISTINCT upholstery_id FROM "Cars".offers ORDER BY upholstery_id ASC')
        upholsteries = cursor.fetchall()
        context = {'filtered_cars': filtered_cars, 'brands': brands, 'models': models, 'generations': generation_years, 'prices_netto':prices_netto,
                   'mileages': mileages, 'is_garaged': is_garaged, 'is_damaged': is_damaged,
                   'is_after_accident': is_after_accident, 'is_electric_seats': is_electric_seats,
                   'is_cruise_control': is_cruise_control, 'is_usb_port': is_usb_port, 'is_abs': is_abs,
                   'is_bluetooth': is_bluetooth, 'is_gps': is_gps, 'air_conditioning_type': air_conditioning_type,
                   'roof_types': roof_types, 'upholsteries': upholsteries}
        return render(request, 'MainPage/index.html', context)
