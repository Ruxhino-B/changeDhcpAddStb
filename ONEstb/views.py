from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from dhcp.models import Radreply
from .models import ONE_STB
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required
def changeHexRandreply(request):
    if request.method == "POST":
        mac = request.POST.get('mac')
        try:
            vendor = Radreply.objects.get(username=mac, attribute='DHCP-Vendor')
            if (vendor.value == "0x204a564341535f424f4f543d31302e38302e31332e323a313236383620564d57435f424f4f543d31302e38302e31332e32"):
                return render(request, 'OneStb.html', {'response': f'This mac: {mac} Is OK. Plz skip this step for this mac'})
            else:
                vendor.value = "0x204a564341535f424f4f543d31302e38302e31332e323a313236383620564d57435f424f4f543d31302e38302e31332e32"
                vendor.save()
                ONE_STB.objects.create(mac=mac)
                # one_stb.save()
                return render(request, 'OneStb.html', {'response': f'Changes Have Save For STB: {mac}'})
        except Radreply.DoesNotExist:
            mesazh = f"Nuk ekziston ne Radreply: {mac}\n"
            print(mesazh)
            return render(request, 'OneStb.html',
                          {'response': 'Please Check Mac if It IS Correct Else Remove And Add Again To FBT Portal'})
    return render(request, 'OneStb.html')


def loginapp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ippools')
        else:
            return redirect('login')
    else:
        return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('ippools')
    # Redirect to a success page.