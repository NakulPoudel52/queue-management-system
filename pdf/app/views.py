from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Form,Hospital,Doctor,Time
from datetime import datetime,timedelta,time

def index(request):
    return render(request,"app/index.html")

def home(request):
	if not request.user.is_authenticated:
		return render(request, 'app/home.html')
	
	return render(request, 'ALogin/ahome.html')

def signup(request):
    return render(request, 'app/Signup.html')

def contact(request):
    return render(request, 'app/contact.html')


def hospital(request):
    return render(request, 'app/hospitals.html')


def bank(request):
    return render(request, 'app/bank.html')

def feed(request):
	a = Hospital.objects.all()
	b= Doctor.objects.all()
	context={"hospital":a,"doctor":b}
	return render(request, 'ALogin/ahome.html',context)



def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("feed"))
    else:
        return render(request, "app/home.html")

def logout_view(request):
    logout(request)
    return render(request, "app/home.html")

def dfrm_view(request):
	return render(request,"ALogin/dfrm.html")







def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	
	}
id=1
hname=""
dname=""
now=datetime(year=2020,month=6,day=6,hour=10,minute=00)

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		
		global id		
		global hname,dname,time,now
		f = Form.objects.get(pk=id)
		print(hname)
		print(f.contact)
		print(f.name)
		b =Time.objects.last()
		now = b.time
		now =now + timedelta(minutes=15)
		a = Time(time=now)
		a.save()
		data = {
		"company": f.name,
		"address": "Kathmandu",
		"country": "Nepal",
		"hospital": hname,
		"num":id,
		"doctor":dname,
		"time":now,
		


		"phone": f.contact,
		"email": f.email,
		"website": "hospital.com",
		}
		


		pdf = render_to_pdf('app/pdf_template.html',data)	
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('app/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response




def index1(request):
	if request.method=="POST":
		name = request.POST["name"]
		email = request.POST["email"]
		contact = request.POST["contact"]
		
		print(name)
		cno=int(contact)
		pk1 = int(request.POST["hospital"])
		pk2 = int(request.POST["doctor"])
		f = Hospital.objects.get(pk=pk1)
		g = Doctor.objects.get(pk=pk2)
		x = Form.objects.create(name=name,email=email,contact=contact,hname=f,dname=g)
		#x.h_name.add(f)
		x.save()
		global id
		id=int(x.id)
		print(x.id)
		global hname,dname
		hname=x.hname.hospital_name
		dname=x.dname.doctor_name
		
	context = {"name":name}
	return render(request, 'app/index1.html', context)
	#return HttpResponseRedirect(reverse("dfrm"))