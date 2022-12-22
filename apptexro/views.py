from django.shortcuts import redirect, render
from .models import Blockinfoaboutcollege, Infodirector, Virtualtour, Ourpartners, Usefullinks, Ourprojects, \
    SiteDopmodels, Currentinfo
from apptecsupport.models import Technicalsupport
from appnewbecome.models import Addnews, Addimgnews
from appanelInformationAboutVET.models import Addurlvet
from appmain.models import Addurlmain
from appentrant.models import Addurlentrant
from appstudent.models import Addurlstudent
from appgraduate.models import Addurlgraduate
from appteacher.models import Addurlteacher
import re
from django.http import JsonResponse, HttpResponse
import json


def mainHome(request):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)

    try:
        _INFDirector = Infodirector.objects.get(id=1)
    except Infodirector.DoesNotExist:
        # запрос не соответствует ни одному элементу.
        _INFDirector = None
    try:
        _VIRTour = Virtualtour.objects.get(id=1)
    except Virtualtour.DoesNotExist:
        # запрос не соответствует ни одному элементу.
        _VIRTour = None

    _OURPartners = Ourpartners.objects.all()
    _USFullinks = Usefullinks.objects.all()
    _OURrojects = Ourprojects.objects.all()
    _CURinfo = Currentinfo.objects.all()

    slav_news = {}
    a = 0
    for dtanew in Addnews.objects.order_by('-date_time')[:3]:
        a += 1
        slav_news.update({a: [dtanew.title,
                              dtanew.preview.url, dtanew.date_time, dtanew.id]})

    if 'to_send_vopr' in request.POST:
        form_name = request.POST['nameuserplz']
        if not str(form_name) in ['Crytotix']:
            form_email = request.POST['emailuserplz']
            form_messages = request.POST['messagesuserplz']
            try:
                Technicalsupport.objects.create(
                    name=form_name, email=form_email, messages=form_messages)
            except:
                pass

        return redirect('/')

    data = {

        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,
        'Marquee': _BICollege.marquee,

        'INFDirector': _INFDirector,

        'VIRTour': _VIRTour,

        'OURrojects': _OURrojects,
        'OURPartners': _OURPartners,
        'USFullinks': _USFullinks,
        'CURinfo': _CURinfo,

        'SlavNews': slav_news,

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),

    }
    return render(request, 'apptexro/main.html', data)


def NewSpisok(request):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    _ADDNews = Addnews.objects.all().order_by('-date_time')
    slav_news = {}

    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'SlavNews': slav_news,

        'ADDNews': _ADDNews,
        'URL': 'main',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),

    }
    return render(request, 'apptexro/newsall.html', data)


def NewSite(request, idnew):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    try:
        _ADDNews = Addnews.objects.get(id=idnew)
        _ADDNewsImg = Addimgnews.objects.filter(idnews=idnew)
    except:
        _ADDNews = "К сожалению, страница, которую вы ищите, не существует! #404"
        _ADDNewsImg = None

    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'ADDNews': _ADDNews,
        'ADDIMGNews': _ADDNewsImg,
        'URL': 'main',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),

    }
    return render(request, 'apptexro/new.html', data)


def InfPOO(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    try:
        _ADDurl = Addurlvet.objects.get(name_link=slug)
    except:
        _ADDurl = None
    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'CNTBase': _ADDurl,
        'TitleSite': 'Сведения о ПОО',
        'URL': 'sveden',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
    }
    return render(request, 'apptexro/infoBase.html', data)


def DrivDiric(request):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)

    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        # 'CNTBase': _ADDurl,
        'TitleSite': 'Схема проезда',
        'URL': 'd-site',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
    }
    return render(request, 'apptexro/DrivingDirections.html', data)


def Main(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    try:
        _ADDurl = Addurlmain.objects.get(name_link=slug)
    except:
        _ADDurl = None
    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'CNTBase': _ADDurl,
        'TitleSite': 'Главная',
        'URL': 'main',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
    }
    return render(request, 'apptexro/infoBase.html', data)


def Entrant(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    data_specialty_statistics = {
        '25.02.06 Производство и обслуживание авиационной техники': 0,
        '25.02.08 Эксплуатация беспилотных авиационных систем': 0,
        '15.02.14 Оснащение средствами автоматизации технологических процессов и производств (по отраслям)': 0,
        '09.02.07 Информационные системы и программирование': 0,
        '09.02.06 Сетевое и системное администрирование': 0,
        '38.02.03 Операционная деятельность в логистике': 0,
        '38.02.01 Экономика и бухгалтерский учет (по отраслям)': 0,
        '35.02.15 Кинология': 0,
        '23.01.17 Мастер по ремонту и обслуживанию автомобилей': 0,
        '15.01.35 Мастер слесарных работ': 0,
        '09.01.03 Мастер по обработке цифровой информации': 0,
        '09.01.02 Наладчик компьютерных сетей': 0,
    }
    try:
        _ADDurl = Addurlentrant.objects.get(name_link=slug)
    except:
        _ADDurl = None
    if request.path == '/entrant/rejting-abiturientov':
        with open('/home/user/website_phtex/phptex/apptexro/data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for ispecialty_statistics in data_specialty_statistics:
            for ikispecialty_statistics in data:
                if ispecialty_statistics == ikispecialty_statistics['specialization']:
                    data_specialty_statistics[ispecialty_statistics] += 1

    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'CNTBase': _ADDurl,
        'TitleSite': 'Абитуриенту',
        'URL': 'entrant',

        'DataCountRejting': data_specialty_statistics,

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
    }
    return render(request, 'apptexro/infoBase.html', data)


def Student(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)

    try:
        _ADDurl = Addurlstudent.objects.get(name_link=slug)
    except:
        _ADDurl = None
    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'CNTBase': _ADDurl,
        'TitleSite': 'Студенту',
        'URL': 'student',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
    }
    return render(request, 'apptexro/infoBase.html', data)


def Graduate(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    try:
        _ADDurl = Addurlgraduate.objects.get(name_link=slug)
    except:
        _ADDurl = None
    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'CNTBase': _ADDurl,
        'TitleSite': 'Выпускнику',
        'URL': 'graduate',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
    }
    return render(request, 'apptexro/infoBase.html', data)


def Teacher(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    try:
        _ADDurl = Addurlteacher.objects.get(name_link=slug)
    except:
        _ADDurl = None
    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'CNTBase': _ADDurl,
        'TitleSite': 'Педагогу',
        'URL': 'teacher',

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
    }
    return render(request, 'apptexro/infoBase.html', data)


def FindElement(request):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    if 'form_find' in request.POST:
        result_blk1 = []
        result_blk2 = []
        result_blk3 = []
        result_blk4 = []
        result_blk5 = []
        result_blk6 = []
        result_blk7 = []
        rzfind = request.POST['findtext']

        for inews in Addnews.objects.all():
            title_new = str(fr"{inews.title}")
            if re.search(str(rzfind).lower(), title_new.lower()):
                result_blk1.append(inews)
        for iurl_vet in Addurlvet.objects.all():
            title_vet = str(fr"{iurl_vet.name_page}")
            if re.search(str(rzfind).lower(), title_vet.lower()):
                result_blk2.append(iurl_vet)
        for iurl_main in Addurlmain.objects.all():
            title_main = str(fr"{iurl_main.name_page}")
            if re.search(str(rzfind).lower(), title_main.lower()):
                result_blk3.append(iurl_main)
        for iurl_entrant in Addurlentrant.objects.all():
            title_entrant = str(fr"{iurl_entrant.name_page}")
            if re.search(str(rzfind).lower(), title_entrant.lower()):
                result_blk4.append(iurl_entrant)
        for iurl_student in Addurlstudent.objects.all():
            title_std = str(fr"{iurl_student.name_page}")
            if re.search(str(rzfind).lower(), title_std.lower()):
                result_blk5.append(iurl_student)
        for iurl_graduate in Addurlgraduate.objects.all():
            title_graduate = str(fr"{iurl_graduate.name_page}")
            if re.search(str(rzfind).lower(), title_graduate.lower()):
                result_blk6.append(iurl_graduate)

        for iurl_teacher in Addurlteacher.objects.all():
            title_teache = str(fr"{iurl_teacher.name_page}")
            if re.search(str(rzfind).lower(), title_teache.lower()):
                result_blk7.append(iurl_teacher)

        data = {
            'LogoImg': _BICollege.logo_img.url,
            'TitleCollege': _BICollege.title_college,
            'Address': _BICollege.address,
            'PhoneOne': _BICollege.phone_one,
            'PhoneTwo': _BICollege.phone_two,
            'Email': _BICollege.email,
            'LinkVk': _BICollege.link_vk,
            'LinkInstagram': _BICollege.link_instagram,
            'LinkFacebook': _BICollege.link_facebook,
            'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
            'LinkYouTube': _BICollege.link_youtube,
            'EndHeaderColg': _BICollege.end_header_colg,

            'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
            'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
            'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
            'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
            'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
            'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),

            'RB1': result_blk1,
            'RB2': result_blk2,
            'RB3': result_blk3,
            'RB4': result_blk4,
            'RB5': result_blk5,
            'RB6': result_blk6,
            'RB7': result_blk7,
            'STtext': rzfind
        }
        return render(request, 'apptexro/findelentindex.html', data)


def DopSite(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)
    try:
        _ADDurl = SiteDopmodels.objects.get(name_link=slug)
    except:
        _ADDurl = None
    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),

        'CNTBase': _ADDurl,
        'TitleSite': 'Дополнительные страницы',
        'URL': 'd-site',
    }
    return render(request, 'apptexro/infoBase.html', data)


def MenuPanel(request, slug):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)

    if slug == 'sveden':
        _ADDurl = Addurlvet.objects.all().order_by('id')
        _TTle = 'СВЕДЕНИЯ О ПОО'
        _SLUrl = slug
    elif slug == 'main':
        _ADDurl = Addurlmain.objects.all().order_by('id')
        _TTle = 'ГЛАВНАЯ'
        _SLUrl = slug
    elif slug == 'entrant':
        _ADDurl = Addurlentrant.objects.all().order_by('id')
        _TTle = 'АБИТУРИЕНТУ'
        _SLUrl = slug
    elif slug == 'student':
        _ADDurl = Addurlstudent.objects.all().order_by('id')
        _TTle = 'СТУДЕНТУ'
        _SLUrl = slug
    elif slug == 'graduate':
        _ADDurl = Addurlgraduate.objects.all().order_by('id')
        _TTle = 'ВЫПУСКНИКУ'
        _SLUrl = slug
    elif slug == 'teacher':
        _ADDurl = Addurlteacher.objects.all().order_by('id')
        _TTle = 'ПЕДАГОГУ'
        _SLUrl = slug
    elif slug == 'd-site':
        _ADDurl = SiteDopmodels.objects.all().order_by('id')
        _TTle = 'Дополнительные страницы'
        _SLUrl = slug
    else:
        _TTle = None
        _ADDurl = None
        _SLUrl = None

    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),

        'CNTBase': _ADDurl,
        'TitleSite': _TTle,
        'URL': _SLUrl,
    }
    return render(request, 'apptexro/menupanel.html', data)


def CardInfoSite(request):
    _BICollege = Blockinfoaboutcollege.objects.get(id=1)

    data = {
        'LogoImg': _BICollege.logo_img.url,
        'TitleCollege': _BICollege.title_college,
        'Address': _BICollege.address,
        'PhoneOne': _BICollege.phone_one,
        'PhoneTwo': _BICollege.phone_two,
        'Email': _BICollege.email,
        'LinkVk': _BICollege.link_vk,
        'LinkInstagram': _BICollege.link_instagram,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkFacebook': _BICollege.link_facebook,
        'LinkOdnoklassniki': _BICollege.link_odnoklassniki,
        'LinkYouTube': _BICollege.link_youtube,
        'EndHeaderColg': _BICollege.end_header_colg,

        'PanelSite_block1': Addurlvet.objects.all().order_by('id'),
        'PanelSite_block2': Addurlmain.objects.all().order_by('id'),
        'PanelSite_block3': Addurlentrant.objects.all().order_by('id'),
        'PanelSite_block4': Addurlstudent.objects.all().order_by('id'),
        'PanelSite_block5': Addurlgraduate.objects.all().order_by('id'),
        'PanelSite_block6': Addurlteacher.objects.all().order_by('id'),
        'PanelSite_block7': SiteDopmodels.objects.all().order_by('id'),

        'TitleSite': 'Карта сайта',
    }
    return render(request, 'apptexro/CardInfo.html', data)


def PostJson(request):
    filter_student_data_commerce = []
    filter_student_data_budget = []
    if request.method == 'POST':
        data_list = {
            '250206': '25.02.06 Производство и обслуживание авиационной техники',
            '250208': '25.02.08 Эксплуатация беспилотных авиационных систем',
            '150214': '15.02.14 Оснащение средствами автоматизации технологических процессов и производств (по отраслям)',
            '090207': '09.02.07 Информационные системы и программирование',
            '090206': '09.02.06 Сетевое и системное администрирование',
            '380203': '38.02.03 Операционная деятельность в логистике',
            '380201': '38.02.01 Экономика и бухгалтерский учет (по отраслям)',
            '350215': '35.02.15 Кинология',
            '230117': '23.01.17 Мастер по ремонту и обслуживанию автомобилей',
            '150135': '15.01.35 Мастер слесарных работ',
            '090103': '09.01.03 Мастер по обработке цифровой информации',
            '090102': '09.01.02 Наладчик компьютерных сетей',
        }
        with open('/home/user/website_phtex/phptex/apptexro/data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        data_specialization = request.POST['dataspec']

        for dict_data in data:
            if dict_data['specialization'] == str(data_list[data_specialization]):
                if dict_data['type_of_financing'] == 'Коммерция':
                    filter_student_data_commerce.append(dict_data)
                if dict_data['type_of_financing'] == 'Бюджет':
                    filter_student_data_budget.append(dict_data)
        tp_num_b = ''
        if str(data_specialization) in ['250206', '250208', '150214', '150135', '090102']:
            tp_num_b = '1'
        elif str(data_specialization) in ['380201', '350215']:
            tp_num_b = '0'
        elif str(data_specialization) in ['090207', '090206', '380203', '230117', '090103']:
            tp_num_b = '2'
        data = {
            'SpectionDataCommerce': filter_student_data_commerce,
            'SpectionDataBudget': filter_student_data_budget,
            'TP': tp_num_b,
            'NameSpc': str(data_list[data_specialization]),
        }
        return JsonResponse(data, safe=False)