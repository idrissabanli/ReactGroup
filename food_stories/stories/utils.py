from rest_framework.authentication import SessionAuthentication 

def get_filename(filename):
    return filename.upper()


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening