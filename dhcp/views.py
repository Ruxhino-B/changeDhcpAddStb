

from django.shortcuts import render
from .models import IpPools, Radreply, Regions
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
import string
from django.db.models import Q
# Create your views here.

class IpPoolsListView(ListView):
    # model = IpPools
    template_name = 'ippools.html'

    def get_queryset(self):
        object_list = IpPools.objects.all()[:50]
        return object_list

def PassDataBetweenTable(request):
    data_list = []
    city_id = request.GET.get('city_id')
    with open('stb.txt') as file:

    # mac = request.GET.get('mac')
        for mac in file:

            mac = mac.strip('\n')
            try:
                data = IpPools.objects.get(stb_mac=mac)
                # print(data)
                data_list.append(data)
                if city_id:
                    data_list = []
                    region = Regions.objects.get(id=city_id)
                    mac_data = IpPools.objects.get(stb_mac=mac)
                    mac_ip = mac_data.ipaddress
                    data = IpPools.objects.filter(Q(city_id=city_id) & Q(stb_mac__isnull=True))[:30]
                    data_for_change = data[0]
                    data_ip = data[0].ipaddress
                    if mac_ip[0:5] == data_ip[0:5]:
                        print("JANE BRENDA NJE IP POOLI")
                    else:
                        data_for_change.stb_mac = mac
                        print(data_for_change.stb_mac)
                        data_for_change.save()
                        mac_data.stb_mac = None
                        mac_data.save()
                        try:
                            radreply_ip = Radreply.objects.get(username=mac,attribute='DHCP-Your-IP-Address')
                            radreply_ip.value = data_ip
                            radreply_ip.save()
                            radreply_getway = Radreply.objects.get(username=mac, attribute='DHCP-Router-Address')
                            radreply_getway.value = region.gateway
                            radreply_getway.save()
                            radreply_subnet = Radreply.objects.get(username=mac, attribute='DHCP-Subnet-Mask')
                            radreply_subnet.value = region.subnet
                            radreply_subnet.save()
                            data = IpPools.objects.get(stb_mac=mac)
                            # print(data)
                            data_list.append(data)
                        except Radreply.DoesNotExist:
                            mesazh = f"Nuk ekziston ne Radreply: {mac}\n"
                            print(mesazh)
                            with open('error.txt', 'a') as f:
                                f.write(mesazh)





            except IpPools.DoesNotExist:
                mesazh=f"Nuk ekziston: {mac}\n"
                print(mesazh)
                with open('error.txt','a') as f:
                    f.write(mesazh)
    return render(request, 'passdata.html', {'object_list': data_list})



