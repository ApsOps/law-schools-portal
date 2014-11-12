from django.http import HttpResponse
from django.views import generic
from .forms import RegistrationForm, LoginForm, EntryForm
from django.contrib.auth.models import User
from .models import LawSchool
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from braces import views
import csv

# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
                 generic.CreateView):
    form_class = RegistrationForm
    form_valid_message = "Account created successfully! Go ahead and login."
    model = User
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class LoginView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
                generic.FormView):
    form_class = LoginForm
    form_valid_message = "You're logged into your account."
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(views.LoginRequiredMixin, views.MessageMixin,
                 generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been successfully logged out.")
        return super(LogOutView, self).get(request, *args, **kwargs)


def workRedirectView(request):
    if request.user.is_staff:
        return ExportTemplateView.as_view()(request)
    return WorkView.as_view()(request)


class WorkView(views.LoginRequiredMixin, views.FormValidMessageMixin,
               generic.CreateView):
    form_class = EntryForm
    form_valid_message = "Data added successfully."
    model = LawSchool
    success_url = reverse_lazy('work')
    template_name = "work/entry.html"


class ExportTemplateView(views.LoginRequiredMixin,
                         views.StaffuserRequiredMixin, generic.TemplateView):
    template_name = "work/export.html"


class ExportView(views.LoginRequiredMixin, views.StaffuserRequiredMixin,
                 generic.View):

    csv_filename = 'csvfile.csv'

    def get_csv_filename(self):
        return self.csv_filename

    def render_to_csv(self, field_names, queryset):
        response = HttpResponse(content_type='text/csv')
        cd = 'attachment; filename="{0}"'.format(self.get_csv_filename())
        response['Content-Disposition'] = cd

        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    def get(self, request, *args, **kwargs):
        queryset = LawSchool.objects.all()
        opts = queryset.model._meta
        field_names = [field.name for field in opts.fields]
        return self.render_to_csv(field_names, queryset)
