# Bắt đầu phần Import
# Import các module cần thiết
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from formtools.wizard.views import SessionWizardView
from bs4 import BeautifulSoup

# Import các model và form cần thiết
from .models import PersonalInfo, VaccineInfo, User, Relative, RelativeVaccineInfo
from .forms import UserProfileInfo, vaccine, UserForm, RelativeInfo, RelativeVaccine
from .filters import FilterBar, NameFilter, RelativeNameFilter
# Kết thúc Import


# Trang chủ
def index(request):
    return render(request, 'index.html')

# Trang đăng ký
def register(request):
    return render(request, 'regist.html')

# Trang xóa form
def delete(request):
    return render(request, 'functions/delete_form.html')

# Đăng xuất người dùng
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Trang đặc biệt yêu cầu đăng nhập
@login_required
def special(request):
    return HttpResponse("Bạn đã đăng nhập")

# Class Wizard liên hệ
class ContactWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return render(self.request, 'relatives.html', {
        'form_data': [form.cleaned_data for form in form_list]
        })

# Bắt đầu lưu Vaccine Form
@method_decorator(login_required, name='dispatch')
class multiStepForm(SessionWizardView):
    template_name = 'functions/relatives.html'
    form_list = [RelativeInfo, RelativeVaccine]
    success_url = reverse_lazy('done')

    def done(self, form_list, **kwargs):
        user = self.request.user  # Người dùng hiện tại
        relative_info = Relative.objects.create(
        user=user,
        Role=form_list[0].cleaned_data['Role'],
        Relative_name=form_list[0].cleaned_data['Relative_name'],
        Ngày_sinh=form_list[0].cleaned_data['Ngày_sinh'],
        Tuoi=form_list[0].cleaned_data['Tuoi'],
        )
        vaccine_info = RelativeVaccineInfo.objects.create(
        user=user,
        relative_info=relative_info,  # Associate RelativeInfo with RelativeVaccineInfo
        Tên_Vaccine=form_list[1].cleaned_data['Tên_Vaccine'],
        Ngày_tiêm=form_list[1].cleaned_data['Ngày_tiêm'],
        Nơi_tiêm=form_list[1].cleaned_data['Nơi_tiêm'],
        Sức_khỏe_trước_khi_tiêm=form_list[1].cleaned_data['Sức_khỏe_trước_khi_tiêm'],
        Sức_khỏe_sau_khi_tiêm=form_list[1].cleaned_data['Sức_khỏe_sau_khi_tiêm'],
        Liều_lượng=form_list[1].cleaned_data['Liều_lượng'],
        Ghi_chú=form_list[1].cleaned_data['Ghi_chú'],
        )

        # Chuyển dữ liệu đã lưu đến trang Form_saved
        context = {
            'relative_info': relative_info,
            'vaccine_info': vaccine_info
        }
        return redirect(Form_saved)
# Kết thúc lưu Vaccine Form

def medical_news(request):
    url = 'https://suckhoedoisong.vn/'
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_articles = soup.find_all('div', class_='list-item')

    articles = []
    for article in news_articles:
        title = article.find('h3').text
        summary = article.find('p').text
        link = article.find('a')['href']
        articles.append({
            'title': title,
            'summary': summary,
            'link': link
        })

    context = {
        'articles': articles
    }

    return render(request, 'functions/hostlist.html', context)

@login_required(login_url='/login')
def self_view(request):
    if request.method == 'POST':
        form = vaccine(request.POST)
        if form.is_valid():
            vaccine_info = form.save(commit=False)
            vaccine_info.user = request.user
            personal_info = PersonalInfo.objects.get(user=request.user)
            vaccine_info.personal_info = personal_info
            vaccine_info.save()
            return redirect(Form_saved)
    else:
        form = vaccine()
    return render(request, 'functions/self.html', {'form': form})
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfo(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user  # Đăng ký người dùng cho Profile
            profile.save()
            
            registered = True 
        else: 
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()
    return render(request, 'registrations/regist.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})
    
def form_list(request):
    forms = PersonalInfo.objects.all()

    search = request.GET.get('search')
    if search:
        forms = forms.filter(name__icontains=search)

    context = {
        'forms': forms,
        'search': search
    }

    
def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user: 
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Dang nhap khong thanh cong")
        else:
            print("Someone tried to login and fail")
            print("Username: {} and password: {}".format(username,password))    
            return HttpResponse("invalid login")
    else:
        return render(request,'registrations/login.html',{})    
    

# Bắt đầu xóa form
@login_required
@login_required
def delete_form(request, vaccine_info_id):
    vaccine_info = get_object_or_404(VaccineInfo, id=vaccine_info_id)

    if request.method == 'POST':
        vaccine_info.delete()
        return redirect('form_saved')
    
    context = {
        'vaccine_info': vaccine_info,
    }
    return render(request, 'functions/delete.html', context)
# Kết thúc xóa form


@login_required
def createForm(request): 
    context={}
    return render(request, 'functions/self.html')

# Bắt đầu edit form
@login_required
def update_form(request, vaccine_info_id):
    vaccine_info = get_object_or_404(VaccineInfo, id=vaccine_info_id)
    
    if request.method == 'POST':
        vaccine_form = vaccine(request.POST, instance=vaccine_info)
        if vaccine_form.is_valid(): 
            vaccine_form.save()
            return redirect('form_saved')
    else:
        vaccine_form = vaccine(instance=vaccine_info)
    context = {
        'vaccine_form': vaccine_form,
    }
    return render(request, 'functions/update.html', context)
# Kết thúc edit form

@login_required
def relative_update_form(request, relative_vaccine_info_id):
    relative_vaccine_info = get_object_or_404(RelativeVaccineInfo, id=relative_vaccine_info_id)
    relative_info = relative_vaccine_info.relative_info

    if request.method == 'POST':
        vaccine_form = RelativeVaccine(request.POST, instance=relative_vaccine_info)
        personal_form = RelativeInfo(request.POST, instance=relative_info)
        if vaccine_form.is_valid() and personal_form.is_valid():
            vaccine_form.save()
            personal_form.save()
            return redirect('form_saved')
    else:
        vaccine_form = RelativeVaccine(instance=relative_vaccine_info)
        personal_form = RelativeInfo(instance=relative_info)
    context = {
        'vaccine_form': vaccine_form,
        'personal_form': personal_form,
    }

    return render(request, 'functions/relative_update.html', context)

@login_required
def relative_delete_form(request, relative_vaccine_info_id):
    relative_vaccine_info = get_object_or_404(RelativeVaccineInfo, id=relative_vaccine_info_id)

    if request.method == 'POST':
        relative_vaccine_info.delete()
        return redirect('form_saved')
    
    context = {
        'relative_vaccine_info': relative_vaccine_info,
    }
    return render(request, 'functions/relative_delete.html', context)   

# Bắt đầu lưu form
@login_required(login_url='/login')
def Form_saved(request):
    user = request.user
    save_list = PersonalInfo.objects.filter(user=user)
    vaccine_list = VaccineInfo.objects.filter(user=user)
    relative_list = Relative.objects.filter(user=user)
    relative_vaccine_list = RelativeVaccineInfo.objects.filter(user=user).select_related('relative_info')

    vaccineFilter = FilterBar(request.GET, queryset=vaccine_list)
    vaccine_list = vaccineFilter.qs
    nameFilter = NameFilter(request.GET, queryset=save_list)
    save_list = nameFilter.qs
    Relative_vaccine_Filter = FilterBar(request.GET, queryset=relative_vaccine_list)
    Relative_name_Filter = RelativeNameFilter(request.GET, queryset=relative_list)
    relative_vaccine_list = Relative_vaccine_Filter.qs
    relative_list = Relative_name_Filter.qs

    unique_entries = set()  # Use a set to store unique entries based on relative name and relative vaccine name
    for relative in relative_list:
        unique_vaccines = set()  # Use a set to store unique relative vaccine names for each relative

        for relative_vaccine in relative_vaccine_list:
            if relative_vaccine.relative_info == relative:
                entry = (relative.Relative_name, relative_vaccine.Tên_Vaccine)

                if entry not in unique_entries:
                    unique_vaccines.add(relative_vaccine.Tên_Vaccine)
                    unique_entries.add(entry)

        relative.unique_vaccines = unique_vaccines

    return render(
        request,
        'functions/saved.html',
        {
            'save_list': save_list,
            'vaccine_list': vaccine_list,
            'relative_list': relative_list,
            'relative_vaccine_list': relative_vaccine_list,
            'vaccineFilter': vaccineFilter,
            'nameFilter': nameFilter,
            'Relative_vaccine_Filter': Relative_vaccine_Filter,
            'Relative_name_Filter': Relative_name_Filter,
        },
    )
# Kết thúc lưu Form