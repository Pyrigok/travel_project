from .settings import PORTAL_URL

def trav_proc(request):
	return {'PORTAL_URL': PORTAL_URL}