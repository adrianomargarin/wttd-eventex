from django.contrib import admin

from eventex.core.models import Talk
from eventex.core.models import Course
from eventex.core.models import Speaker
from eventex.core.models import Contact


class ContactInline(admin.TabularInline):

    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):

    inlines = [ContactInline]
    list_display = ['name', 'website_link', 'photo_img', 'email', 'phone']
    prepopulated_fields = {'slug': ['name']}

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'Website'

    def photo_img(self, obj):
        return '<img width="32px" src="{}"/>'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'Foto'

    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = 'E-mail'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'Telefone'


class TalkModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.filter(course=None)



admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course)
