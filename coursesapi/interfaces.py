from .models import PageUser

class PageUserInterface:

    @staticmethod
    def getByEmail(email):
        return PageUser.objects.filter(email=email)