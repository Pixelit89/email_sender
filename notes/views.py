import glob, zipfile, os, re
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core.mail import EmailMessage
from .models import Note
from .forms import AddNoteForm


class IndexView(generic.ListView):
    model = Note
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = AddNoteForm
        return context


def add_note(request):
    new_note = Note(name=request.POST['name'], email=request.POST['email'])
    new_note.save()
    return HttpResponseRedirect(reverse('index'))


def del_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return HttpResponseRedirect(reverse('index'))


def send(request, mail_to):
    my_zip = zipfile.ZipFile('CV_and_Code_zip/code.zip', 'w', zipfile.ZIP_DEFLATED)

    for dirs, subdirs, files in os.walk('.'):
        if not re.search('.idea', dirs) \
           and not re.search('__pycache__', dirs):
            for file in files:
                # Ignore zip itself and a file with a password to email.
                if not re.search('password', file)\
                   and not re.search('code', file):
                    my_zip.write(os.path.join(dirs, file))
    my_zip.close()

    cv = glob.glob('**/CV*.docx', recursive=True)
    code = glob.glob('**/code.zip', recursive=True)

    email = EmailMessage(
        subject='Test task',
        body="""Hello, my name is Andrei Ivashkevich.
                I saw a test task on your site, so I decided to make it.
                But unfortunately I am not a Java Developer, but Python Developer.
                So I made in on Python.
                Sorry for interrupting you. But if you would have a time to estimate my work I will be very appreciate for this.
                Thank you.
                """,
        to=[mail_to],
    )
    email.attach_file(cv[0])
    email.attach_file(code[0])
    email.send()

    return HttpResponseRedirect(reverse('index'))