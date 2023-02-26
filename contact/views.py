from django.shortcuts import render
from django.views.generic import ListView

## 문의하기
class WriteView(ListView):
    template_name                       = 'contact/write.html'
    context_object_name                 = 'data'

    def get_queryset(self):
        return ''

    def get_context_data(self, **kwargs):
        context                         = super().get_context_data(**kwargs)
        return context