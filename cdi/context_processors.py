from cdi.home.models import College, Address

def host(request):
    hostname = 'http://'+request.get_host()
    if 'clubs' or 'events' or 'academics' in request.path:
        college_list = College.objects.all().order_by('-rating', 'name')
        return { 'HOST':hostname, 'COLLEGES': college_list }
    return { 'HOST':hostname }
#    html = []
#    for k, v in values:
#        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#    return HttpResponse('<table>%s</table>' % '\n'.join(html))
