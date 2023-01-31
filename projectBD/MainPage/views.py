from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from datetime import datetime


def index(request):
    offset = request.GET.get('offset', 0)
    limit = request.GET.get('limit', 20)
    brand = request.GET.get('brand')
    production_years = range(1980, 2023)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM get_new_offers() OFFSET %s LIMIT %s', [offset, limit])
        recent_offers = cursor.fetchall()
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        # request is AJAX
        return JsonResponse({'recent_offers': recent_offers, 'models': get_brands_models(brand)['models'], },
                            safe=False)

    else:
        # request is not AJAX
        context = {'recent_offers': recent_offers, 'brands': get_brands_models(brand)['brands'],
                   'models': get_brands_models(brand)['models'], 'production_years': production_years,
                   'upholsteries': get_upholsteries(), 'air_conditioning_types': get_air(), 'roof_types': get_roof()}

        return render(request, 'MainPage/index.html', context)


def get_brands_models(brand):
    with connection.cursor() as cursor:
        cursor.execute('SELECT brand FROM "Cars"."brands"')
        brands = cursor.fetchall()
        cursor.execute(
            'SELECT model FROM "Cars"."models" INNER JOIN "Cars"."brands" ON "Cars"."models"."brand_id" = "Cars"."brands"."id" WHERE "Cars"."brands"."brand" = %s',
            (brand,))

        models = cursor.fetchall()
        models_brands = {'brands': brands, 'models': models}
    return models_brands


def get_upholsteries():
    with connection.cursor() as cursor:
        cursor.execute('SELECT name FROM "Cars"."upholstery"')
        upholstery = cursor.fetchall()
    return upholstery


def get_air():
    with connection.cursor() as cursor:
        cursor.execute('SELECT name FROM "Cars"."air_conditioning_type"')
        air = cursor.fetchall()
    return air


def get_roof():
    with connection.cursor() as cursor:
        cursor.execute('SELECT name FROM "Cars"."roof_type"')
        roof_type = cursor.fetchall()
    return roof_type

def filter_cars(request):
    # Get the arguments from the query parameters
    brand = request.GET.get('brand', '')
    model = request.GET.get('model', '')
    production_year = request.GET.get('production_year', '')
    price = request.GET.get('price', '')
    mileage = request.GET.get('mileage', '')
    is_garaged = request.GET.get('is_garaged', '')
    is_damaged = request.GET.get('is_damaged', '')
    is_after_accident = request.GET.get('is_after_accident', '')
    is_electric_seats = request.GET.get('is_electric_seats', '')
    is_cruise_control = request.GET.get('is_cruise_control', '')
    is_usb_port = request.GET.get('is_usb_port', '')
    is_abs = request.GET.get('is_abs', '')
    air_conditioning = request.GET.get('air_conditioning', '')
    roof_type = request.GET.get('roof_type', '')
    upholstery = request.GET.get('upholstery', '')
    air_types_id = ""
    roof_type_id = ""
    upholstery_id = ""
    cars = '"'+'Cars'+'"'
  #  breakpoint()
    if air_conditioning:
        with connection.cursor() as cursor:
            cursor.execute(f"Select id from {cars}.air_conditioning_type where name = '{air_conditioning}'")
            air_types_id = cursor.fetchall() #for getting id's to function instead of names that are returned from selects
    if roof_type:
        with connection.cursor() as cursor:
            cursor.execute(f"Select id from {cars}.roof_type where name = '{roof_type}'")
            roof_type_id = cursor.fetchall() #for getting id's to function instead of names that are returned from selects
    if upholstery:
        with connection.cursor() as cursor:
            cursor.execute(f"Select id from {cars}.upholstery where name = '{upholstery}'")
            upholstery_id = cursor.fetchall() #for getting id's to function instead of names that are returned from selects
    query_len = 0
    query = 'SELECT * FROM "Cars".get_cars_by_filter('
    query_len = len(query)
    query += f"brand_name2 => '{brand}' " if brand else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"model_name2 => '{model}' " if model else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"generation_year2 => '{production_year}' " if production_year else ""
    if query[-2:-1] == "'":
        query += f","
    # query += f"'{price}', " if price else ""
    # query += f"'{mileage}', " if mileage else ""
    query += f"is_garaged2 => '{is_garaged}' " if is_garaged == "True" else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"is_damaged2 => '{is_damaged}' " if is_damaged == "True" else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"is_after_accident2 => '{is_after_accident}' " if is_after_accident == "True" else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"is_electric_seats2 => '{is_electric_seats}' " if is_electric_seats == "True" else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"is_cruise_control2 => '{is_cruise_control}' " if is_cruise_control == "True" else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"is_usb_port2 => '{is_usb_port}' " if is_usb_port == "True" else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"is_abs2 => '{is_abs}' " if is_abs == "True" else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"air_conditioning_type2 => '{air_types_id[0][0]}' " if air_types_id else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"roof_type_id2 => '{roof_type_id[0][0]}' " if roof_type_id else ""
    if query[-2:-1] == "'":
        query += f","
    query += f"upholstery_id2 => '{upholstery_id[0][0]}'," if upholstery_id else ""
    if not len(query) == query_len:
        query = query[:-1]
    query += f") LIMIT 100"
    with connection.cursor() as cursor:
        cursor.execute(query)
        filtered_offers = cursor.fetchall()
    return JsonResponse({'filtered_offers': filtered_offers},
                        safe=False)

def filter_offers(request):

        return render(request, 'MainPage/filtered_offers.html')