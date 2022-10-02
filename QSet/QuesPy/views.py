from django.shortcuts import render
from matplotlib.style import context
from QuesPy.models import Question,file_upload
from QuesPy.forms import MyFileUploadForm
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
        image_op1 = request.POST.get('image_op1')
        image_op2 = request.POST.get('image_op2')
        image_op3 = request.POST.get('image_op3')
        image_op4 = request.POST.get('image_op4')

        c_form = MyFileUploadForm(request.POST,request.FILES)
        if c_form.is_valid():
            files1 = c_form.cleaned_data['image_q']
            files2 = c_form.cleaned_data['image_op1']
            files3 = c_form.cleaned_data['image_op2']
            files4 = c_form.cleaned_data['image_op3']
            files5 = c_form.cleaned_data['image_op4']
            file_upload(qnfile = files1).save()
            file_upload(op1file = files2).save()
            file_upload(op2file = files3).save()
            file_upload(op3file = files4).save()
            file_upload(op4file = files5).save()

        question = Question(source = source, status=status,topic=topic,body_q=body_q,image_q=image_q,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4,image_of_quetionop1=image_op1,image_of_quetionop2=image_op2,image_of_quetionop3=image_op3,image_of_quetionop4=image_op4,)
        if (source!="" or status!=""):
            question.save()
    context = {
        'form': MyFileUploadForm()
    }
    return render(request,'uploadq.html',context)