import json
from random import randint, random
from otree.api import Page
from .models import Constants


class TiemposReproduccion(Page):
    form_model = 'player'
    form_fields = ['tiempos_reproduccion_json']

    def vars_for_template(self):
        max_capitulos_disponibles = self.session.vars.get('max_capitulos_disponibles', 0)
        nombres_capitulos_anteriores = Constants.names_chapters[:self.round_number - 1]
        lista_numeros = list(range(1, min(self.round_number + 1, max_capitulos_disponibles + 1)))
        rutas_audios = [f'sounds/capitulo{i}.{Constants.extension_sounds}' for i in lista_numeros]

        capitulos_y_rutas = list(zip(nombres_capitulos_anteriores, rutas_audios[:-1]))

        return {
            'num_pagina': self.round_number,
            'ruta_ultimo_audio': rutas_audios[-1] if self.round_number <= max_capitulos_disponibles else None,
            'capitulos_y_rutas': capitulos_y_rutas,
            'nombre_actual': Constants.names_chapters[self.round_number - 1],
            'mostrar_capitulos': self.round_number <= max_capitulos_disponibles
        }

    def live_method(self, data):
        if not self.numero_aleatorio:
            self.numero_aleatorio = self.generar_numero_aleatorio()
            # Enviar el número aleatorio al frontend
            return {self.id_in_group: self.numero_aleatorio}

class ResultadosParciales1(Page):
    def is_displayed(self):
        return self.round_number == 5

    def vars_for_template(self):
        #boletas_adicionales = self.player.contador_correctas_p1
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds()]
        numeros_aleatorios_p1 = json.loads(self.player.numeros_aleatorios_p1 or '[]')
        tiempos_reproduccion = [p.tiempos_reproduccion_json for p in self.player.in_all_rounds()]

        todos_los_numeros = numeros_aleatorios + numeros_aleatorios_p1

        return {
            #'boletas_adicionales': boletas_adicionales,
            'todos_los_numeros': todos_los_numeros,
            'tiempos_reproduccion': tiempos_reproduccion,
        }

class ResultadosParciales2(Page):
    def is_displayed(self):
        return self.round_number == 10

    def vars_for_template(self):
        #boletas_adicionales = self.player.contador_correctas_p1
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds()]
        tiempos_reproduccion = [p.tiempos_reproduccion_json for p in self.player.in_all_rounds()]

        todos_los_numeros = numeros_aleatorios
        return {
            #'boletas_adicionales': boletas_adicionales,
            'todos_los_numeros': todos_los_numeros,
            'tiempos_reproduccion': tiempos_reproduccion,
        }
    


class ResultadosFinales(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds)

    def vars_for_template(self):
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds() if p.numero_aleatorio is not None]
        return {
            'numeros_aleatorios': numeros_aleatorios,
            'num_pagina': self.round_number
        }

class Inicio(Page):
    def is_displayed(self):
        return self.round_number == 1
    form_model = 'player'

class Preguntas1(Page):

    form_model = 'player'
    form_fields = ['P1P1_emocion_1', 'P1P2_ciudad', 'P1P3_mama', 'P1P4_preocupados', 'P1P5_gusto', 'P1P6_personajes', 'P1P7_amigos' ]
    def is_displayed(self):
        return self.round_number == 5

    def before_next_page(self):
        numeros_aleatorios_p1 = []
          #for campo in self.form_fields:
          #    if getattr(self.player, campo) == Constants.respuestas_correctas_p1.get(campo, ''):
          #       self.player.contador_correctas_p1 += 0
          #      nuevo_numero = self.player.generar_numero_aleatorio()
          #     numeros_aleatorios_p1.append(nuevo_numero)

        self.player.numeros_aleatorios_p1 = json.dumps(numeros_aleatorios_p1)

class Preguntas2(Page):
    form_model = 'player'
    form_fields = ['P2P1_emocion_2', 'P2P2_futbol', 'P2P3_hallacas', 'P2P4_musica', 'P2P5_aceptado', 'P2P6_proximos', 'P2P7_amigos']
    def is_displayed(self):
        return self.round_number == 10

class Preguntas3(Page):
    def is_displayed(self):
        return self.round_number == 15
    form_model = 'player'
    form_fields = ['P3P1_emocion_3', 'P3P2_radionovela', 'P3P3_papa', 'P3P4_identifica', 'P3P5_celebracion', 'P3P6_pelusa', 'P3P7_amigo', 'P3P8_familiar']


class x_EF_Page2_ParteB(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds)
    form_model = 'player'
    form_fields = ['EF_B1_revisar_hoja', 'EF_B2_llame_entrevista', 'EF_B3_contrate', 'EF_B4_espere_otras_hojas',
    'EF_B5_tenga_documentos','EF_B6_consiga_documentacion', 'EF_B7_trato_amable', 'EF_B8_trato_indiferencia', 'EF_B9_trato_poco_respetosa',
    ]

class x_EF_Page3_ParteC(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds)
    form_model = 'player'
    form_fields = ['EF_c1_familia', 'EF_c2_barrio', 'EF_c3_policia', 'EF_c4_jueces', 'EF_c5_caleños', 'EF_c6_españoles', 'EF_c7_venezolanos', 
    'EF_c8_chilenos', 'EF_c9_bancos', 'EF_c10_presidente', 'EF_c11_iglesia',
]


class x_EF_Page6_ParteF(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds)
    form_model = 'player'
    form_fields = ['EF_F1_habla_mujeres', 'EF_F2_habla_jovenes', 'EF_F3_habla_pobres', 'EF_F4_habla_indigenas', 'EF_F5_habla_venezolanos',
    'EF_F6_habla_mayores', 'EF_F7_actividad_recreativa', 'EF_F8_act_recreativa_migrantes', 'EF_F9_amigos_venezolanos', 'EF_cuantos2',  
    'EF_F10_vecinos_españoles', 'EF_F11_vecinos_venezolanos', 'EF_F12_vecinos_norteamericanos', 'EF_F13_vecinos_chilenos',
    'EF_F14_pareja_venezolana', 'EF_F15_donaciones', 'EF_F16_amigos_venezuela', 'EF_F17_exp_col_controles_migrantes', 'EF_F18_exp_col_prioridad_colombianos',
    'EF_F19_ven_edu_colombianos', 'EF_F20_ven_respeto', 
    'EF_F21_ven_contratados', 'EF_F22_ven_acceso_servicios', 'EF_F23_ven_juiciosos', 'EF_F24_ven_ladrones', 'EF_F25_campaña', 'EF_F26_donaciones', 
]


page_sequence = [Inicio, TiemposReproduccion, Preguntas1, Preguntas2, 
                ResultadosParciales1, ResultadosParciales2, Preguntas3, x_EF_Page2_ParteB, 
                x_EF_Page3_ParteC, x_EF_Page6_ParteF, ResultadosFinales]


