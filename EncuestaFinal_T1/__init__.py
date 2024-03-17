from random import randint
from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'EncuestaFinal_T1'
    players_per_group = None
    max_number_random = 6500
    min_number_random = 1

    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # Inicializa la lista de números usados si no existe
        if 'numeros_usados' not in self.session.vars:
            self.session.vars['numeros_usados'] = []


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    numero_aleatorio = models.IntegerField(initial=0)
    # ******************************************************************************************************************** #
    # *** Variables Cuestionario
    # ******************************************************************************************************************** #    
    EF_B1_revisar_hoja = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_B2_llame_entrevista = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_B3_contrate = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_B4_espere_otras_hojas = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_B5_tenga_documentos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_B6_consiga_documentacion = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])   
    EF_B7_trato_amable= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_B8_trato_indiferencia= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_B9_trato_poco_respetosa= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_c1_familia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c2_barrio= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c3_policia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c4_jueces= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c5_caleños= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c6_españoles= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c7_venezolanos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c8_chilenos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c9_bancos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c10_presidente= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    EF_c11_iglesia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    
    EF_F1_habla_mujeres= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    EF_F2_habla_jovenes= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    EF_F3_habla_pobres= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    EF_F4_habla_indigenas= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    EF_F5_habla_venezolanos= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    EF_F6_habla_mayores= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])

    EF_F7_actividad_recreativa = models.StringField(
        label="7. En 2023, ¿Con qué frecuencia te reuniste con amigos para una actividad recreativa  (ir a un concierto, fiesta, cine, ver fútbol, hacer deporte)?",
        choices=[ 
            [0,"a. Nunca"],
            [1,"b. Una vez al mes"],
            [2,"c. Todas las semanas una vez"],
            [3,"d. Todas las semanas varias veces"],
            [4,"e. A diario"],
        ],
        widget = widgets.RadioSelect
    )

    EF_F8_act_recreativa_migrantes = models.StringField(
        label="8. ¿En cuántos de estos eventos había personas nacidas fuera de Colombia?",
        choices=[ 
            [0,"a. Ninguno"],
            [1,"b. Algunos, muy pocos"],
            [2,"c. Bastantes"],
            [3,"d. Muchos"],
        ],
        widget = widgets.RadioSelect
        )
    EF_F9_amigos_venezolanos = models.StringField(
        label="9. ¿Tienes amigos o amigas cercanos que hayan nacido en Venezuela?",
        choices=[ 
            [0,"a. No"],
            [1,"b. Si"],
        ],
        widget = widgets.RadioSelect
    )

    EF_cuantos2 = models.IntegerField(label="¿Cuantos amigos cercanos tienes que hayan nacido en Venezuela?", initial="0")

    EF_F10_vecinos_españoles = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F11_vecinos_venezolanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F12_vecinos_norteamericanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F13_vecinos_chilenos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F14_pareja_venezolana = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F15_donaciones = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F16_amigos_venezuela = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
   
    EF_F17_exp_col_controles_migrantes = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F18_exp_col_prioridad_colombianos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F19_ven_edu_colombianos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F20_ven_respeto = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F21_ven_contratados = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F22_ven_acceso_servicios = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F23_ven_juiciosos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    EF_F24_ven_ladrones = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    EF_F25_campaña = models.StringField(
        label="9. ¿Participarías en una campaña para otorgar 1,000 empleos a jóvenes venezolanos?",
        choices=[ 
            [0,"a. No, no me interesa."],
            [1,"b. No, no quiero."],
            [1,"b. No, no tengo tiempo."],
            [1,"b. Si"],
            
        ],
        widget = widgets.RadioSelect
    )

    EF_F26_donaciones = models.StringField(
        label="10. ¿Has realizado donaciones en campañas o a fundaciones que promuevan el bienestar de los migrantes venezolanos en el último mes?",
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

class Page2_ParteB(Page):
    form_model = 'player'
    form_fields = ['EF_B1_revisar_hoja', 'EF_B2_llame_entrevista', 'EF_B3_contrate', 'EF_B4_espere_otras_hojas',
    'EF_B5_tenga_documentos','EF_B6_consiga_documentacion', 'EF_B7_trato_amable', 'EF_B8_trato_indiferencia', 'EF_B9_trato_poco_respetosa',
]

class Page3_ParteC(Page):
    form_model = 'player'
    form_fields = ['EF_c1_familia', 'EF_c2_barrio', 'EF_c3_policia', 'EF_c4_jueces', 'EF_c5_caleños', 'EF_c6_españoles', 'EF_c7_venezolanos', 
    'EF_c8_chilenos', 'EF_c9_bancos', 'EF_c10_presidente', 'EF_c11_iglesia',
]

class Page6_ParteF(Page):
    form_model = 'player'
    form_fields = ['EF_F1_habla_mujeres', 'EF_F2_habla_jovenes', 'EF_F3_habla_pobres', 'EF_F4_habla_indigenas', 'EF_F5_habla_venezolanos',
    'EF_F6_habla_mayores', 'EF_F7_actividad_recreativa', 'EF_F8_act_recreativa_migrantes', 'EF_F9_amigos_venezolanos', 'EF_cuantos2',  
    'EF_F10_vecinos_españoles', 'EF_F11_vecinos_venezolanos', 'EF_F12_vecinos_norteamericanos', 'EF_F13_vecinos_chilenos',
    'EF_F14_pareja_venezolana', 'EF_F15_donaciones', 'EF_F16_amigos_venezuela', 'EF_F17_exp_col_controles_migrantes', 'EF_F18_exp_col_prioridad_colombianos',
    'EF_F19_ven_edu_colombianos', 'EF_F20_ven_respeto', 
    'EF_F21_ven_contratados', 'EF_F22_ven_acceso_servicios', 'EF_F23_ven_juiciosos', 'EF_F24_ven_ladrones', 'EF_F25_campaña', 'EF_F26_donaciones'
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





page_sequence = [Inicio, Page2_ParteB, Page3_ParteC, Page6_ParteF, Page7_Final ]
