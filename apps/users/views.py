# from django.views.generic import ListView, DetailView, FormView
# from django.http import HttpResponse as resp
# from django.http import Http404
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.conf.global_settings import ALLOWED_HOSTS
# from django.shortcuts import render
# from school.models import *
# from school.models.achievements import *
# from school.forms  import *

# # CONSTANTS

# global IS_LOGGED_OUT
# IS_LOGGED_OUT = False

# class HomeView(View):
#     def get(self, request : dict):
#         global IS_LOGGED_OUT
#         context = {
#             'facilities' : Facility.objects.all(),
#             'achievements': Achievement.objects.all(),
#             'sceneries' : Scenery.objects.all(),
#             'student_ads' : StudentAd.objects.all(),
#             'enroll' : EnrollVacancy.objects.all(),
#             'headline' : '' # TODO: add headline option 
#         }
#         if IS_LOGGED_OUT :
#             IS_LOGGED_OUT = False
#             context['msg']= '''
#                 <div class="alert alert-success alert-dismissible fade show position" role="alert">
#                 You successfully logged out!
#                 <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
#                 </div>
#             '''
            
#         return render(request, 'school/index.html', context)

# # TODO: Implement enrollement forms and display
# class EnrollmentView(ListView):
#     model =  EnrollVacancy
#     template_name = 'enrollment.html'

# # TODO: Implement Vacancy submisssion forms 
# class VacancyListView(ListView):
#     model = Vacancy
#     template_name = 'vacancy_list.html'
#     context_object_name = 'vacancies'

# class EnrollView(FormView):
#     form_class = EnrollForm
#     template_name = 'forms/enroll.html'

# class Apply(View):
#     form_class = ApplyForm
#     template_name = 'forms/apply.html'

#     def get(self, request):
#         return  render(request, self.template_name, {'form': self.form_class})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'forms/v_sucess.html')
#         else:
#             for key in self.request:
#                 print(self.request.POST[key])

# class Dashboard(LoginRequiredMixin, View):

#     def get(self, request):
#         try:
#             id = int(request.user.identity)
#             match id:
#                 case 1:  # Dean
#                     return render(request, 'dean/index.html')
#                 case 2:  # Deputy
#                     return render(request, 'dean/index.html')
#                 case 3:  # Hod
#                     return render(request, 'hod/index.html')
#                 case 4:  # Teacher
#                     return render(request, 'teacher/index.html')
#                 case 5:  # Student
#                     return render(request, 'student/index.html')

#         except AttributeError:  # Admin
#             return resp(f'Wrong Path, Admin Pages {ALLOWED_HOSTS[0]}/admin/')

# # TODO: Display errors if users are not allowed and if they ain't in the db
# class LoginView(LoginView):
#         authentication_form = LoginForm
#         template_name = 'login.html'
#         next_page = 'dashboard'

# class LogoutView(LogoutView):
#     template_name = None
#     next_page =  'home'

#     def get_default_redirect_url(self):
#         self.overr()
#         return super().get_default_redirect_url()

#     def get_success_url(self) -> str:
#         self.overr()
#         return super().get_success_url()
    
#     def overr(self):
#         global IS_LOGGED_OUT 
#         IS_LOGGED_OUT = True
