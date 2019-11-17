from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.db import transaction
from schoreg.forms import UserForm, SchoolForm, ContactForm
from panel.models import School, AbstractSchool, SchoolContact


# Create your views here.
class schoreg(CreateView):
    model = School

    user_form_class = UserForm
    school_form_class = SchoolForm
    contact_form_class = ContactForm

    template_name = "schoreg/register.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(School, self).get_context_data(*args, **kwargs)
    #     return context

    def post(self, request):
        post_data = request.POST or None
        user_form = self.user_form_class(post_data, prefix='user')
        school_form = self.school_form_class(post_data, prefix='school')
        contact_form = self.contact_form_class(post_data, prefix='contact')

        context = self.get_context_data(
                                        user_form=user_form,
                                        school_form=school_form,
                                        contact_form=contact_form,
                                        )
        if school_form.is_valid():
            try:
                self.form_save(school_form)
            except Exception as e:
                print(e)
                return render(self.request, 'schoreg/register.html', context)

        if contact_form.is_valid():
            try:
                post = self.form_save(contact_form, commit=False)
                # post.school =
                post.save()
            except Exception as e:
                print(e)
                return render(self.request, 'schoreg/register.html', context)

        if user_form.is_valid():
            try:
                self.form_save(user_form)
            except Exception as e:
                print(e)
                return render(self.request, 'schoreg/register.html', context)

        # if abstractschool_form.is_valid():
        #     try:
        #         post = self.form_save(abstractschool_form , commit=False)
        #         # post.school =
        #     except Exception as e:
        #         print(e)
        #         return render(self.request, 'schoreg/register.html', context)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save(commit=False)
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj


# def register(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Form submission successful')
#     else:
#         form = UserForm()
#
#     return render(request, "schoreg/register.html", {"form": form})
