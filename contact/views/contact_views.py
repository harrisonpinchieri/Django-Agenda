from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')[:25]

    context = {
        'contacts': contacts,
    }

    return render(request,
                  'contact/index.html',
                  context
                  )
