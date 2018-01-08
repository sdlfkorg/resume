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

EXPERIENCE = [
    {
        'title': 'Software Developer',
        'company': 'Promise Technology',
        'description': 'tbd',
        'from_to': 'December 2016 - Present'
    },
    {
        'title': 'Patent Engineer',
        'company': 'Louis International Patent Office',
        'description': 'tbd',
        'from_to': 'August 2014 - November 2016'
    },
]

PUBLICATIONS = [
    {
        'title': 'An optically variable thin film with electrochemical capacitor property and use thereof',
        'link': 'https://worldwide.espacenet.com/publicationDetails/biblio?CC=TW&NR=I455163B&KC=B&FT=D&ND=4&date=20141001&DB=EPODOC&locale=en_EP',
    },
    {
        'title': 'Optically variable thin film with electrochemical capacitance property and use thereof',
        'link': 'https://worldwide.espacenet.com/publicationDetails/originalDocument?FT=D&date=20140529&DB=EPODOC&locale=en_EP&CC=US&NR=2014146381A1&KC=A1&ND=5',
    }, 
    {
        'title': 'Molybdate Hexacyanoferrate (MoOHCF) Thin Film: A Red Prussian Blue Analogue for Electrochromic Window Application',
        'link': 'http://www.sciencedirect.com/science/article/pii/S0927024815003499',
    },
    {
        'title': 'Multicolor Electrochromic Thin Films and Devices Based on the Prussian Blue Family Nanoparticles',
        'link': 'http://www.sciencedirect.com/science/article/pii/S0927024815003918',
    },

]

class MyView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        for key, val in MY_INFO.items():
            
            context[key] = val
        context['education'] = EDUCATION
        context['experience'] = EXPERIENCE
        context['publications'] = PUBLICATIONS
        # context['test'] = 'sdfsdf'
        # print(self.request.GET)
        return context

