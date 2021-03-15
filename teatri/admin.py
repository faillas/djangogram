from django.contrib import admin
from .models import Profili
from .models import Teatri
from .models import Frequenze
from .models import Tag
from .models import Hashtag


# Register your models here.
admin.site.register(Profili)
admin.site.register(Teatri)
admin.site.register(Frequenze)
admin.site.register(Tag)
admin.site.register(Hashtag)
