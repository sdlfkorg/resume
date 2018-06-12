from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

INTRO = """
    I am a passionate software developer who love working in an efficient and friendly environment. In these years, I have gathered the knowledge of web development from work, and also spend a lot of free time exploring the latest technology advancement in web development and block chain technology. For example, I have finished several Dapps on ethereum platform and deployed on Rinkeby network.
    
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
        'description': [
            "Developed applications and tools for enterprise hybrid-cloud solution, consisting of multiple platforms and applications running on hyperconverged infrastructure.",
            "Developed and maintained Portal for Cloud Storage Application.",
            "Developed and Validated Database for Cloud Storage Management System.",
            "Developed and Maintained client portal for in-house Virtual Desktop Infrastructure (VDI) Solution."
        ],
        'from_to': 'December 2016 - Present'
    },
    {
        'title': 'Patent Engineer',
        'company': 'Louis International Patent Office',
        'description': [
            "Provided Clients with professional advice in regards to patent applications. Responsibilities included: i. Investigation and Identification of prior art ii. Specification drafting and patent refining iii. Office Action analysis and responses."
        ],
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

