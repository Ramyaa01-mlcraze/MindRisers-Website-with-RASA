from django.http import HttpResponse
from django.shortcuts import render
import razorpay
from .models import TeacherDetails, User,BookTutor
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
# Create your views here.
def chatbot(request):
    return render(request,"chatroom.html")
def student_dashboard(request):
    res=TeacherDetails.objects.all()
    return render(request,'student.html',{'res':res})
def teacher_dashboard(request):
    return render(request,'teacher.html')
def list_of_teachers(request,email):
    res=TeacherDetails.objects.all()
    for r in res:
        if(r.email==email):
            firstname=r.firstname
            lastname=r.lastname
            middlename=r.middlename
            qual=r.qual
            experience=r.experience
            pnumber=r.pnumber
            city=r.city
            state=r.state
            dept=r.dept
            Specialization=r.Specialization
            display_name=r.display_name
    return render(request,'profile-teacher.html',{'firstname':firstname,'lastname':lastname,'middlename':middlename,'email':email,'qual':qual,'display_name':display_name,'pnumber':pnumber,'experience':experience,'dept':dept,'city':city,'state':state,'Specialization':Specialization})
    return render(request,'list_of_teachers.html')
def homepage(request):
    currency = 'INR'
    amount = 20000 # Rs. 200
	# Create a Razorpay Ordercd coddes/
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request, 'payment.html', context=context)
def chatapplication(request):
    return render(request,'index.html')
def book_tutor(request):
    return render(request,'book_tutor.html')   
def booking_confirmation(request):
    topic=request.POST['topic']
    tutorname=request.POST['tutorname']
    studentname=request.POST['studentname']
    dateofthesession=request.POST['dateofthesession']
    starttime=request.POST['starttime']
    totalduration=request.POST['totalduration']
    email=request.POST['email']
    number=request.POST['email']
    expectation=request.POST['expectation']
    reg = BookTutor(topic=topic,tutorname=tutorname,studentname=studentname,dateofthesession=dateofthesession,starttime=starttime,totalduration=totalduration,email=email,number=number,expectation=expectation)
    reg.save()
    return render(request,'booking_confirmation.html')
def profile_student(request):
    email=request.session['useremail']
    res=User.objects.all()
    for r in res:
        if(r.email==email):
            firstname=r.firstname
            lastname=r.lastname
            middlename=r.middlename
            study=r.study
            YOP=r.YOP
            number=r.number
            CGPA=r.CGPA
            College=r.College
            City=r.City
            State=r.State
            branch=r.branch
            Interest=r.Interest
    return render(request,'profile-student.html',{'firstname':firstname,'lastname':lastname,'middlename':middlename,'email':email,'study':study,'YOP':YOP,'number':number,'CGPA':CGPA,'College':College,'City':City,'State':State,'branch':branch,'Interest':Interest})
def profile_teacher(request):
    email=request.session['useremail']
    res=TeacherDetails.objects.all()
    for r in res:
        if(r.email==email):
            firstname=r.firstname
            lastname=r.lastname
            middlename=r.middlename
            qual=r.qual
            experience=r.experience
            pnumber=r.pnumber
            city=r.city
            state=r.state
            dept=r.dept
            Specialization=r.Specialization
            display_name=r.display_name
    return render(request,'profile-teacher.html',{'firstname':firstname,'lastname':lastname,'middlename':middlename,'email':email,'qual':qual,'display_name':display_name,'pnumber':pnumber,'experience':experience,'dept':dept,'city':city,'state':state,'Specialization':Specialization})
def logincheck(request):
    username = request.POST['email']
    password = request.POST['password']
    role = request.POST['role']
    if(role=="Teacher"):
        res=TeacherDetails.objects.all()
        for r in res:
            if(r.email==username):
                if(r.password==password):
                    request.session['useremail']=username
                    return render(request,'teacher.html')
                else:
                    return HttpResponse("<h1>INVALID EMAIL AND PASSWORD</h1>")
    elif(role=="Student"):
        res=User.objects.all()
        for r in res:
            if(r.email==username):
                if(r.password==password):
                    request.session['useremail']=username
                    res=TeacherDetails.objects.all()
                    return render(request,'student.html',{'res':res})
                else:
                    return HttpResponse("<h1>INVALID EMAIL AND PASSWORD</h1>")
def register_student_db(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    middlename = request.POST['middlename']
    email = request.POST['email']
    password = request.POST['password']
    study = request.POST['study']
    YOP = request.POST['YOP']
    number = request.POST['number']
    CGPA = request.POST['CGPA']
    College = request.POST['College']
    City = request.POST['City']
    State = request.POST['State']
    branch = request.POST['branch']
    Interest = request.POST['Interest']
    reg = User(firstname = firstname,lastname=lastname,middlename =middlename,email=email,password=password,study=study,YOP=YOP,number=number,CGPA=CGPA,College=College,City=City,State=State,branch=branch,Interest=Interest)
    reg.save()
    request.session['useremail']=email
    return render(request,'student.html')
def register_teacher_db(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    middlename = request.POST['middlename']
    email = request.POST['email']
    password = request.POST['password']
    qual = request.POST['qual']
    pnumber = request.POST['pnumber']
    experience = request.POST['experience']
    city = request.POST['city']
    state = request.POST['state']
    dept = request.POST['dept']
    Specialization = request.POST['Specialization']
    display_name = request.POST['display_name']
    reg_teacher = TeacherDetails(firstname = firstname,lastname=lastname,middlename =middlename,email=email,password=password,qual=qual,pnumber=pnumber,experience=experience,city=city,state=state,dept=dept,Specialization=Specialization,display_name=display_name)
    reg_teacher.save()
    request.session['useremail']=email
    return render(request,'teacher.html')