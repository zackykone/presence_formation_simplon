from django.shortcuts import render

# Create your views here.
from .models import Participant

def enregistrer_participant(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        participant = Participant(nom=nom, prenom=prenom, telephone=telephone, email=email)
        participant.save()

        return render(request, 'participants/enregistrer_participant.html', {'success': True})

    return render(request, 'participants/enregistrer_participant.html')
