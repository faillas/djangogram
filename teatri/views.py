from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from teatri.models import Profili, Teatri, Frequenze, Tag, Hashtag

# Create your views here.
def teatri_list(request):
    profili = Profili.objects.all()
    teatri = Teatri.objects.order_by('likes')
    frequenze = Frequenze.objects.order_by('freq')
    tag = Tag.objects.order_by('freq_t')
    hashtag = Hashtag.objects.order_by('freq_h')
    return render(request, 'teatri/teatri_list.html', {'profili': profili, 'teatri': teatri, 'frequenze': frequenze, 'tag': tag, 'hashtag': hashtag})

def profili_detail(request, pk):
    profili = Profili.objects.all()
    Profili.objects.get(pk=pk)
    profili = get_object_or_404(Profili, pk=pk)
    # per vedere tutti i parametri come le frequenze, avrei dovuto usare object.all non solo a Profili
    teatri = Teatri.objects.filter(codifica=pk)
    frequenze = Frequenze.objects.filter(Id_freq=pk)
    tag = Tag.objects.filter(Id_tag=pk)
    hashtag = Hashtag.objects.filter(Id_hashtag=pk)
    return render(request, 'teatri/profili_detail.html', {'Profili': profili, 'Teatri': teatri, 'Frequenze': frequenze, 'Tag': tag, 'Hashtag': hashtag})

def index(request, pk):
    return render(request, 'teatri/index.html')