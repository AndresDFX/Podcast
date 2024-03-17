from random import randint

from otree.api import *


doc = """
Your app description
"""
class Constants(BaseConstants):
    name_in_url = 'EncuestaInicial_T1'
    players_per_group = None
    max_number_random = 6500

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
    A1_estrato = models.StringField(
        label="1. ¿Cuál es el estrato de la vivienda en la que vives actualmente?",
        choices=[
            [1,"a. Estrato 1"],
            [2,"b. Estrato 2"],
            [3,"c. Estrato 3"],
            [4,"d. Estrato 4"],
            [5,"e. Estrato 5"],
            [6,"f. Estrato 6"],
        ],
        widget = widgets.RadioSelect
    )

    A2_nivel_educativo = models.StringField(
        label="2. ¿Cuál tu mayor nivel de educación obtenida?",
        choices=[
            [1,"1. Ninguno"],
            [2,"2. Preescolar"],
            [3,"3. Básica Primaria"],
            [4,"4. Básica Secundaria (9° grado)"],
            [5,"5. Media /Bachillerato (11° grado)"],
            [6,"6. Técnica/Tecnológica"],
            [7,"7. Superior o Universitaria"],
            [8,"8. No sabe, no informa"],
        ],
        widget = widgets.RadioSelect
    )
    
    A3_etnia = models.StringField(
        label="3. Por tus costumbres o antepasados, te identificas como:",
        choices=[
            [1, "a. Mestizo(a)"],
            [2, "b. Indigena"],
            [3, "c. Blanco"],
            [4, "d. Afrodescendiente"],
            [5, "e. Raizal"],
            [6, "f. Palenquero"],
            [7, "g. Otra"],
            [8, "h. Prefiero no decirlo"],
            [9, "i. Ninguna"],
        ],
        widget=widgets.RadioSelect,
    )

    etnia2 = models.StringField(label="Si elegiste la opción de Otra Etnia ¿Con cuál otra te identificas?", initial=" ")
    
    A4_ocupacion = models.StringField(
        label="4. ¿Cuál es tu ocupación?",
        choices=[ 
            [1,"a. Trabaja"],
            [2,"b. Estudia"],
            [3,"c. Trabaja y Estudia"],
            [4,"d. Buscando empleo"],
            [5,"e. Estudia y busca empleo"],
            [6,"f. Ninguna de las anteriores"],
            [7,"g. Otro"],
        ],
        widget = widgets.RadioSelect
    )
    
    A5_amigos_migrantes = models.IntegerField(
        label="5. ¿Aproximadamente cuántos de tus familiares o amigos se han ido a vivir a otro país en los últimos años?",
    )
    
    A6_candidato_presidente = models.StringField(
        label="6. ¿A quién apoyaste como candidato presidencial en la primera vuelta de las elecciones del 2022?",
        choices=[ 
            [1,"a. Gustavo Petro"],
            [2,"b. Rodolfo Hernandez"],
            [3,"c. Federico Gutiérrez"],
            [4,"d. Sergio Fajardo"],
            [5,"e. John Milton Rodríguez"],
            [6,"f. Enrique Goméz"],
            [7,"g. Prefiero no decirlo / A nadie"],
        ],
        widget = widgets.RadioSelect
    )
    
    B1_revisar_hoja = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    B2_llame_entrevista = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    B3_contrate = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    B4_espere_otras_hojas = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    B5_tenga_documentos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    B6_consiga_documentacion = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])   
    B7_trato_amable= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    B8_trato_indiferencia= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    B9_trato_poco_respetosa= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    c1_familia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c2_barrio= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c3_policia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c4_jueces= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c5_caleños= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c6_españoles= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c7_venezolanos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c8_chilenos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c9_bancos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c10_presidente= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    c11_iglesia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])

    D1_preparen_perro = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D5_exp_preparen_perro = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D2_pregunten_dinero = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D6_exp_pregunten_dinero = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D3_vendan_llevar = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D7_exp_vendan_llevar = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D4_excusa_no_preparar = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D8_exp_excusa_no_preparar = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    D9_rechazo_cansancio = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D12_exp_rechazo_cansancio = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D10_rechazo_dudas_pagos = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D13_exp_rechazo_dudas_pagos = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D11_rechazo_miedo = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    D14_exp_rechazo_miedo = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    E1_llevar_hoja = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    E2_consumir_producto = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    
    F1_habla_mujeres= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    F2_habla_jovenes= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    F3_habla_pobres= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    F4_habla_indigenas= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    F5_habla_venezolanos= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    F6_habla_mayores= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])

    F7_actividad_recreativa = models.StringField(
        label="7. En 2023, ¿Con qué frecuencia te reuniste con amigos para una actividad recreativa (ir a un concierto, fiesta, cine, ver fútbol, hacer deporte)?",
        choices=[ 
            [0,"a. Nunca"],
            [1,"b. Una vez al mes"],
            [2,"c. Todas las semanas una vez"],
            [3,"d. Todas las semanas varias veces"],
            [4,"e. A diario"],
        ],
        widget = widgets.RadioSelect
    )
    F8_act_recreativa_migrantes = models.StringField(
        label="8. ¿En cuántos de estos eventos había personas nacidas fuera de Colombia?",
        choices=[ 
            [0,"a. Ninguno"],
            [1,"b. Algunos, muy pocos"],
            [2,"c. Bastantes"],
            [3,"d. Muchos"],
        ],
        widget = widgets.RadioSelect
        )
    F9_amigos_venezolanos = models.StringField(
        label="9. ¿Tienes amigos o amigas cercanos que hayan nacido en Venezuela?",
        choices=[ 
            [0,"a. No"],
            [1,"b. Si"],
        ],
        widget = widgets.RadioSelect
    )

    cuantos2 = models.IntegerField(label="¿Cuantos amigos cercanos tienes que hayan nacido en Venezuela?", initial=0)

    F10_vecinos_españoles = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F11_vecinos_venezolanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F12_vecinos_norteamericanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F13_vecinos_chilenos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F14_pareja_venezolana = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F15_donaciones = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F16_amigos_venezuela = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F17_exp_col_controles_migrantes = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    F18_exp_col_prioridad_colombianos = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    F19_exp_jov_controles_migrantes = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    F20_exp_jov_prioridad_colombianos = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    F21_ven_edu_colombianos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F22_ven_respeto = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F23_ven_contratados = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F24_ven_acceso_servicios = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F25_ven_juiciosos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    F26_ven_ladrones = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    F27_donaciones = models.StringField(
        label="25. ¿Has realizado donaciones en campañas o a fundaciones que promuevan el bienestar de los migrantes venezolanos en el último mes?",
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

class Page1_ParteA(Page):
    form_model = 'player'
    form_fields = ['A1_estrato', 'A2_nivel_educativo', 'A3_etnia', 'etnia2', 'A4_ocupacion', 'A5_amigos_migrantes', 
    'A6_candidato_presidente']

class Page2_ParteB(Page):
    form_model = 'player'
    form_fields = ['B1_revisar_hoja', 'B2_llame_entrevista', 'B3_contrate', 'B4_espere_otras_hojas',
    'B5_tenga_documentos','B6_consiga_documentacion', 'B7_trato_amable', 'B8_trato_indiferencia', 'B9_trato_poco_respetosa',
]

class Page3_ParteC(Page):
    form_model = 'player'
    form_fields = ['c1_familia', 'c2_barrio', 'c3_policia', 'c4_jueces', 'c5_caleños', 'c6_españoles', 'c7_venezolanos', 
    'c8_chilenos', 'c9_bancos', 'c10_presidente', 'c11_iglesia',
]

class Page4_ParteD(Page):
    form_model = 'player'
    form_fields = ['D1_preparen_perro', 'D5_exp_preparen_perro', 'D2_pregunten_dinero', 'D6_exp_pregunten_dinero', 
    'D3_vendan_llevar', 'D7_exp_vendan_llevar', 'D4_excusa_no_preparar', 'D8_exp_excusa_no_preparar', 'D9_rechazo_cansancio', 'D12_exp_rechazo_cansancio',
    'D10_rechazo_dudas_pagos', 'D13_exp_rechazo_dudas_pagos', 'D11_rechazo_miedo', 'D14_exp_rechazo_miedo',
]

class Page5_ParteE(Page):
    form_model = 'player'
    form_fields = ['E1_llevar_hoja', 'E2_consumir_producto',]

class Page6_ParteF(Page):
    form_model = 'player'
    form_fields = ['F1_habla_mujeres', 'F2_habla_jovenes', 'F3_habla_pobres', 'F4_habla_indigenas', 'F5_habla_venezolanos',
    'F6_habla_mayores', 'F7_actividad_recreativa', 'F8_act_recreativa_migrantes', 'F9_amigos_venezolanos', 'cuantos2',  
    'F10_vecinos_españoles', 'F11_vecinos_venezolanos', 'F12_vecinos_norteamericanos', 'F13_vecinos_chilenos',
    'F14_pareja_venezolana', 'F15_donaciones', 'F16_amigos_venezuela', 'F17_exp_col_controles_migrantes', 'F18_exp_col_prioridad_colombianos',
    'F19_exp_jov_controles_migrantes', 'F20_exp_jov_prioridad_colombianos', 'F21_ven_edu_colombianos', 'F22_ven_respeto', 
    'F23_ven_contratados', 'F24_ven_acceso_servicios', 'F25_ven_juiciosos', 'F26_ven_ladrones', 'F27_donaciones',
]

class Page7_Final(Page):
    form_model = 'player'

    def vars_for_template(self):

        # Inicializa la lista si no existe
        if 'numeros_usados' not in self.session.vars:
            self.session.vars['numeros_usados'] = []

        numero_aleatorio = randint(1, Constants.max_number_random)
        while numero_aleatorio in self.session.vars['numeros_usados']:
            numero_aleatorio = randint(1, Constants.max_number_random)

        self.session.vars['numeros_usados'].append(numero_aleatorio)
        self.numero_aleatorio = numero_aleatorio

        return {
            'numero_aleatorio': numero_aleatorio
        }




page_sequence = [Consentimiento, Inicio, Page1_ParteA, Page2_ParteB, Page3_ParteC, Page4_ParteD, Page5_ParteE, Page6_ParteF, Page7_Final]