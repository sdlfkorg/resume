from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

INTRO = """
    A fullstack developer, passionate on python and javascript. 
    
"""


MY_INFO = {
    'first_name': 'Jay',
    'last_name': 'Liao',
    'phone': '0933-453-100',
    'address': '4F., No.7, Aly. 2, Ln. 91, Jianmin Rd., Beitou Dist., Taipei City 112, Taiwan (R.O.C.)',
    'email': 'sdlfkorg@gmail.com',
    'intro': INTRO
}

EDUCATION = [
    {
        'school_name': 'NATIONAL TAIWAN UNIVERSITY',
        'degree': 'MASTER OF SCIENCE',
        'department': 'Bio-Industrial Mechatronics Engineering (BIME)',
        'from_to': 'September 2010 - July 2012'
    },
    {
        'school_name': 'NATIONAL TAIWAN UNIVERSITY',
        'degree': 'BACHELOR OF SCIENCE',
        'department': 'Bio-Industrial Mechatronics Engineering (BIME)',
        'from_to': 'September 2006 - July 2010'
    }
]

class MyView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        for key, val in MY_INFO.items():
            
            context[key] = val
        context['education'] = EDUCATION
        # context['test'] = 'sdfsdf'
        # print(self.request.GET)
        return context

