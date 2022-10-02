import re
from django.shortcuts import render
from QuesPy.models import Question

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'sign-up.html')

def uploadq(request):
    if (request.method=="POST"):
        source = request.POST.get("source")
        status = request.POST.get('status')
        topic = request.POST.get('topic')
        body_q = request.POST.get('body_q')
        image_q = request.POST.get('image_q')
        opt1 = request.POST.get('opt1')
        opt2 = request.POST.get('opt2')
        opt3 = request.POST.get('opt3')
        opt4 = request.POST.get('opt4')
        image_of_quetionop1 = request.POST.get('image_of_quetionop1')
        image_of_quetionop2 = request.POST.get('image_of_quetionop2')
        image_of_quetionop3 = request.POST.get('image_of_quetionop3')
        image_of_quetionop4 = request.POST.get('image_of_quetionop4')
        question = Question(source = source, status=status,topic=topic,body_q=body_q,image_q=image_q,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,image_of_quetionop1=image_of_quetionop1,image_of_quetionop2=image_of_quetionop2,image_of_quetionop3=image_of_quetionop3,image_of_quetionop4=image_of_quetionop4,)
        if (source!="" or status!=""):
            question.save()
    return render(request,'uploadq.html')