from random import randint
from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'EncuestaSeguimiento'
    players_per_group = None
    max_number_random = 6500
    min_number_random = 1

    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # Inicializa la lista de números usados si no existe
        if 'numeros_usados' not in self.session.vars:
            self.session.vars['numeros_usados'] = []

        if 'ronda_intermedia' not in self.session.vars:
            self.session.vars['ronda_intermedia'] = Constants.num_rounds // 2



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    numero_aleatorio = models.IntegerField(initial=0)
    # ******************************************************************************************************************** #
    # *** Variables Cuestionario
    # ******************************************************************************************************************** #    
    ES_c1_familia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c2_barrio= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c3_policia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c4_jueces= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c5_caleños= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c6_españoles= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c7_venezolanos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c8_chilenos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c9_bancos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c10_presidente= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c11_iglesia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    
    ES_F10_vecinos_españoles = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F11_vecinos_venezolanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F12_vecinos_norteamericanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F13_vecinos_chilenos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F14_pareja_venezolana = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F15_donaciones = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])   
    ES_F16_amigos_venezuela = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F17_exp_col_controles_migrantes = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F18_exp_col_prioridad_colombianos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F19_ven_edu_colombianos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F20_ven_respeto = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F21_ven_contratados = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F22_ven_acceso_servicios = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F23_ven_juiciosos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F24_ven_ladrones = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    ES_F25_campaña = models.StringField(
        label="15.¿Participarías en una campaña para otorgar 1,000 empleos a jóvenes venezolanos?",
        choices=[ 
            [0,"a. No, no me interesa."],
            [1,"b. No, no quiero."],
            [1,"b. No, no tengo tiempo."],
            [1,"b. Si"],
            
        ],
        widget = widgets.RadioSelect
    )
    ES_F26_donaciones = models.StringField(
        label="16. ¿Has realizado donaciones en campañas o a fundaciones que promuevan el bienestar de los migrantes venezolanos en el último mes?",
        choices=[ 
            [0,"a. No"],
            [1,"b. Si"],      
        ],
        widget = widgets.RadioSelect
    )
    

# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Consentimiento(Page):
    form_model = 'player'

class Inicio(Page):
    form_model = 'player'

class Page3_ParteC(Page):
    form_model = 'player'
    form_fields = ['ES_c1_familia', 'ES_c2_barrio', 'ES_c3_policia', 'ES_c4_jueces', 'ES_c5_caleños', 'ES_c6_españoles', 'ES_c7_venezolanos', 
    'ES_c8_chilenos', 'ES_c9_bancos', 'ES_c10_presidente', 'ES_c11_iglesia',
]

class Page6_ParteF(Page):
    form_model = 'player'
    form_fields = ['ES_F10_vecinos_españoles', 'ES_F11_vecinos_venezolanos', 'ES_F12_vecinos_norteamericanos', 'ES_F13_vecinos_chilenos',
    'ES_F14_pareja_venezolana', 'ES_F15_donaciones', 'ES_F16_amigos_venezuela', 'ES_F17_exp_col_controles_migrantes', 'ES_F18_exp_col_prioridad_colombianos',
    'ES_F19_ven_edu_colombianos', 'ES_F20_ven_respeto', 
    'ES_F21_ven_contratados', 'ES_F22_ven_acceso_servicios', 'ES_F23_ven_juiciosos', 'ES_F24_ven_ladrones', 'ES_F25_campaña', 'ES_F26_donaciones',
]

class Page7_Final(Page):
    form_model = 'player'

    def vars_for_template(self):

        # Inicializa la lista si no existe
        if 'numeros_usados' not in self.session.vars:
            self.session.vars['numeros_usados'] = []

        numero_aleatorio = randint(Constants.min_number_random, Constants.max_number_random)
        while numero_aleatorio in self.session.vars['numeros_usados']:
            numero_aleatorio = randint(Constants.min_number_random, Constants.max_number_random)

        self.session.vars['numeros_usados'].append(numero_aleatorio)
        self.numero_aleatorio = numero_aleatorio

        return {
            'numero_aleatorio': numero_aleatorio
        }



page_sequence = [Inicio, Page3_ParteC, Page6_ParteF, Page7_Final ]
