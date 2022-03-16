from .models import Team, Service


def footer_content(request):
    services = Service.objects.all()
    teams = Team.objects.all()
    context = {
        'services': services,
        'teams': teams
    }
    return context
