from django.shortcuts import render

def home(request):
    ownerName = 'JaiVin'
    subLists = ['python', 'springboot', 'Angular', 'DevOps']
    return render(request, 'index.html', {'name': ownerName, 'subjects': subLists})

def about(request):
    ownerNative = 'TamilNadu'
    exp = 8
    return render(request, 'about.html', {'place': ownerNative, 'experience': exp})

def contact(request):
    ownerContact = '2054024325'
    return render(request, 'contact.html', {'phone': ownerContact})

def contactprocess(request):
    # read data from html form
    studName = request.GET.get('studentName')
    studEmail = request.GET.get('studentEmail')
    # send name & email to notification.html
    return render(request, 'notification.html', {'name': studName, 'email': studEmail})