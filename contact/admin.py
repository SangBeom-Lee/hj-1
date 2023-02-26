from django.contrib import admin
from contact.models import Contact
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    summernote_fields                       = ('content')
    list_display                            = (
      'id',
      'title',
      'content',
      'created_at',
      'updated_at',
      'answer',
      'answer_at'
    )
    list_display_links                      = list_display