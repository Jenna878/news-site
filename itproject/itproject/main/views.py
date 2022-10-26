from django.shortcuts import render


def index(request): 
    data = {
        'title': 'Главная страница',  
        'values':['Catwoman', 'Harly Quinn', ' Poison Ivy'],
        'obj': {
            'Joker':'Jared Leto',
          'Batman': 'Michael Keaton',
            'Deadshot': 'Will Smith'
        } 
    }
    return render(request, 'main/index.html', data)   

def about(request): 
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def contact_detail(request):
    return render(request, 'main/contact_detail.html')

def about_detail(request):
    return render(request, 'main/about_detail.html')
 
    
