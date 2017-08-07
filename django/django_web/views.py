from django.shortcuts import render
from django_web.models import ArtiInfo
from django.core.paginator import Paginator

def index(request):
    limit = 10
    arti_info = ArtiInfo.objects.all()
    paginatior = Paginator(arti_info,limit)
    page = request.GET.get('page',1)
    loaded = paginatior.page(page)

    name_list = []
    for i in ArtiInfo.objects():
        name_list.append(i['use_name'])
        name_index = list(set(name_list))

    context = {
        'ArtiInfo':loaded,
        'counts':arti_info.count(),
        'count':len(name_index)
        # 'date':arti_info[0].date,
        # 'door_name':arti_info[0].door_name,
        # 'use_name':arti_info[0].use_name,
        # 'use_type':arti_info[0].use_type,
        # 'door_open':arti_info[0].door_open,
        # 'user_id':arti_info[0].user_id,
        # 'door_adress':arti_info[0].door_adress,
        # 'car_id':arti_info[0].car_id
    }
    return render(request,'index_item.html',context)

def chart(request):
    arti_info = ArtiInfo.objects.all()

    context = {
        "counts":arti_info.count,
        'counts_ls': arti_info.filter(use_name='娄尚').count,
        'counts_ln': arti_info.filter(use_name='李楠').count,
        'counts_lj': arti_info.filter(use_name='刘军').count,
        'counts_mj': arti_info.filter(use_name='孟佳').count,
        'counts_dt': arti_info.filter(use_name='党腾').count,
        'counts_zh': arti_info.filter(use_name='赵辉').count,
        'counts_xxm': arti_info.filter(use_name='徐晓梦').count,
        'counts_ysc': arti_info.filter(use_name='杨世成').count,
        'counts_wzc': arti_info.filter(use_name='汪志龙').count,
        'counts_szq': arti_info.filter(use_name='吴志强').count,
        'counts_wzy': arti_info.filter(use_name='吴之遥').count,
        'counts_lhy': arti_info.filter(use_name='刘海洋').count,
        'counts_zx': arti_info.filter(use_name='朱雪').count,
        'counts_zhz': arti_info.filter(use_name='甄重').count,

        'date':arti_info[0].date,
        'door_name':arti_info[0].door_name,
        'use_name':arti_info[0].use_name,
        'use_type':arti_info[0].use_type,
        'door_open':arti_info[0].door_open,
        'user_id':arti_info[0].user_id,
        'door_adress':arti_info[0].door_adress,
        'car_id':arti_info[0].car_id
    }
    return render(request,'index_chart.html',context)

def chart_someone(request):
    arti_info = ArtiInfo.objects.all()
    context = {

    }
    return render(request,'chart_someone.html',context)

def aboutus(request):
    context = {

    }
    return render(request,'about_us.html',context)

def location(request):
    context = {

    }
    return render(request,'location.html',context)

def other(request):
    context = {

    }
    return render(request,'other.html',context)

def other_menu(request):
    context = {

    }
    return render(request,'other_menu.html',context)
def china(request):
    arti_area = ArtiInfo.objects.all()
    context = {
        'citys_ln': arti_area.filter(use_name='北京').count,
        'citys_lj': arti_area.filter(use_name='河北').count,
        'citys_mj': arti_area.filter(use_name='河南').count,
        'citys_dt': arti_area.filter(use_name='安徽').count,
        'citys_zh': arti_area.filter(use_name='赵辉').count,
        'citys_xxm': arti_area.filter(use_name='徐晓梦').count,
        'citys_ysc': arti_area.filter(use_name='杨世成').count,
        'citys_wzc': arti_area.filter(use_name='汪志龙').count,
        'citys_szq': arti_area.filter(use_name='吴志强').count,
        'citys_wzy': arti_area.filter(use_name='吴之遥').count,
        'citys_lhy': arti_area.filter(use_name='刘海洋').count,

        'date': arti_area[0].date,
        'door_name': arti_area[0].door_name,
        'use_name': arti_area[0].use_name,
        'use_type': arti_area[0].use_type,
        'door_open': arti_area[0].door_open,
        'user_id': arti_area[0].user_id,
        'door_adress': arti_area[0].door_adress,
        'car_id': arti_area[0].car_id
    }
    return render(request,'china-map.html',context)

def chart1(request):
    arti_info = ArtiInfo.objects.all()
    context = {
        'counts': arti_info.count,
        'counts_ls': arti_info.filter(use_name='娄尚').count,
        'counts_ln': arti_info.filter(use_name='李楠').count,
        'counts_lj': arti_info.filter(use_name='刘军').count,
        'counts_mj': arti_info.filter(use_name='孟佳').count,
        'counts_dt': arti_info.filter(use_name='党腾').count,
        'counts_zh': arti_info.filter(use_name='赵辉').count,
        'counts_xxm': arti_info.filter(use_name='徐晓梦').count,
        'counts_ysc': arti_info.filter(use_name='杨世成').count,
        'counts_wzc': arti_info.filter(use_name='汪志龙').count,
        'counts_szq': arti_info.filter(use_name='吴志强').count,
        'counts_wzy': arti_info.filter(use_name='吴之遥').count,
        'counts_lhy': arti_info.filter(use_name='刘海洋').count,
        'counts_zx': arti_info.filter(use_name='朱雪').count,

        'date': arti_info[0].date,
        'door_name': arti_info[0].door_name,
        'use_name': arti_info[0].use_name,
        'use_type': arti_info[0].use_type,
        'door_open': arti_info[0].door_open,
        'user_id': arti_info[0].user_id,
        'door_adress': arti_info[0].door_adress,
        'car_id': arti_info[0].car_id
    }
    return render(request, 'index_chart1.html', context)


