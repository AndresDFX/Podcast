from datetime import datetime, timedelta
from random import randint

from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

class Constants(BaseConstants):
    name_in_url = 'Episodios_T1'
    players_per_group = None
    max_number_random = 11
    min_number_random = 1
    extension_sounds = "mp3"
    names_chapters = [
        "Frankie llega al colegio",
        "Cuando un carajito también es un chino",
        "Es cuestión de respeto",
        "Un nuevo equipo de fútbol",
        "¡Nuevas Oportunidades!",
        "Doralba, ¿Futbolista?", 
        "¡La culpa no es de Frankie!",
        "¡Que vivan las uvas pasas!", 
        "¡Hoy por ti, Mañana por mi!",
        "¡Romeo Tik y Julieta tok!",
        "Brillan los ojitos",
        "Un juego, una oportunidad",
        "El barrio es de todos",  
        "Los panas", 
        "Sueños inesperados",
    ]
    num_rounds = len(names_chapters)  # Número de capítulos/audios
    respuestas_correctas_p1 =0

class Subsession(BaseSubsession):
    def creating_session(self):
        # Inicializa la lista de números usados si no existe
        if 'numeros_usados' not in self.session.vars:
            self.session.vars['numeros_usados'] = []

        # Fecha de inicio experimento
        fecha_inicio = datetime(2024, 2, 15)  # Año, mes, día

        # Obtener la fecha actual
        hoy = datetime.now()

        # Calcula los jueves pasados desde la fecha de inicio
        diferencia = (hoy - fecha_inicio).days
        jueves_pasados = sum(1 for i in range(diferencia + 1) if (fecha_inicio + timedelta(days=i)).weekday() == 3)

        # Los primeros tres capítulos siempre están disponibles
        max_capitulos_disponibles = 15  # Cambiar a 5, para que cada jueves solo muestre de a 5.

        # Calcular cuántos capítulos deben estar disponibles
        if jueves_pasados > 0:
            # -1 porque los primeros 5 ya están disponibles
            cap_adicionales = 5 * (jueves_pasados - 1)
            # Ajustar si el total excede el número de capítulos
            max_capitulos_disponibles += min(cap_adicionales, Constants.num_rounds - max_capitulos_disponibles)

        # Reinicia el conteo de boletas después del capítulo 10
        if self.round_number > 10:
            self.session.vars['numeros_usados'] = []

        # Actualizar la variable de sesión con el máximo de capítulos disponibles
        self.session.vars['max_capitulos_disponibles'] = max_capitulos_disponibles


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    tiempos_reproduccion_json = models.LongStringField(blank=True)
    numero_aleatorio = models.IntegerField(initial=0)

    #### VARIABLES POSTAUDIO1
    numeros_aleatorios_p1 = models.StringField()
    contador_correctas_p1 = models.StringField()
    P1P1_emocion_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])
    P1P2_ciudad = models.StringField(
        label="2. ¿De qué ciudad es Frankie?",
        choices=[
            [1,"a. De Bogotá, Colombia"],
            [2,"b. De Valencia, Venezuela"],
            [3,"c. De Lima, Perú"],
        ],
        widget = widgets.RadioSelect
    )

    P1P3_mama = models.StringField(
        label="3. ¿Cómo se llama la mamá de Frankie?",
        choices=[
            [1,"a. Doralba"],
            [2,"b. Sandra"],
            [3,"c. Martha"],
        ],
        widget = widgets.RadioSelect
    )

    P1P4_preocupados = models.StringField(
        label="4. ¿Por qué Frankie y su mamá están preocupados por su abuela?",
        choices=[
            [1,"a. Porque está de cumpleaños y no pueden estar con ella"],
            [2,"b. Porque se le acabó la medicina y no tiene dinero para comprarla"],
            [3,"c. Porque se va de viaje y no tiene quien la acompañe"],
        ],
        widget = widgets.RadioSelect
    )    

    P1P5_gusto = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    
    P1P6_personajes = models.StringField(
        label="6. ¿Con cuál de los personajes te sientes identificado?",
        choices=[
            [1,"a. Pelusa"],
            [2,"b. Erika"],
            [3,"c. Frankie"],
            [4,"c. Ninguno"],
        ],
        widget = widgets.RadioSelect
    )

    P1P7_amigos = models.StringField(
        label="7. Si le mostrarás estos 5 primeros capítulos a alguno de tus amigos creerías que:",
        choices=[
            [1,"a. Le parecería interesante y seguiría escuchando los otros capítulos"],
            [2,"b. No le interesaría y no seguiría escuchando"],
            [3,"c. Le sería indiferente"],
        ],
        widget = widgets.RadioSelect
    )

    ####  VARIABLES POSTAUDIO2
    P2P1_emocion_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])

    P2P2_futbol = models.StringField(
        label="2. ¿Quién es la persona que más sabe de fútbol en el colegio?",
        choices=[
            [1,"a. El profesor de educación física, Milton, porque el fútbol se le da muy bien."],
            [2,"b. Doralba, la mamá de Frankie, porque tiene una Licenciatura en Deportes."],
            [3,"c. La profesora Marcela, porque juega fútbol desde niña."],
        ],
        widget = widgets.RadioSelect
    )

    P2P3_hallacas = models.StringField(
        label="3. ¿Qué son las hallacas?",
        choices=[
            [1,"a. Son un plato típico venezolano con pasas."],
            [2,"b. Son unas manualidades típicas venezolanas."],
            [3,"c. Son unas pulseras de amistad."],
        ],
        widget = widgets.RadioSelect
    )

    P2P4_musica = models.StringField(
        label="4. ¿Qué género musical escogieron los alumnos para la obra de teatro? ",
        choices=[
            [1,"a. Rock"],
            [2,"b. Pop"],
            [3,"c. Reggaeton"],
            [4,"d. Hip Hop"],
        ],
        widget = widgets.RadioSelect
    )    

    P2P5_aceptado = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    P2P6_proximos = models.StringField(
        label="6. ¿Qué crees que pasará en los próximos capítulos?",
        choices=[
            [1,"a. Que Doralba podrá ser entrenadora del equipo de fútbol del colegio"],
            [2,"b. Que Doralba no podrá homologar su título"],
            [3,"c. Que expulsarán a Doralba por querer hacer cosas diferentes a su trabajo"],
            [4,"d. No me interesa que va a ocurrir"],
        ],
        widget = widgets.RadioSelect
    )

    P2P7_amigos = models.StringField(
        label="7. Si le mostrarás estos 5 capítulos a alguno de tus amigos creerías que:",
        choices=[
            [1,"a. Le parecería interesante y seguiría escuchando los otros capítulos"],
            [2,"b. No le interesaría y no seguiría escuchando"],
            [3,"c. Le sería indiferente"],
        ],
        widget = widgets.RadioSelect
    )


####PREGUNTAS POSTAUDIO3
    P3P1_emocion_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])
    P3P2_radionovela = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    P3P3_papa = models.StringField(
        label="3. ¿Por qué el papá de Frankie no está con ellos? ",
        choices=[
            [1,"a. Porque no soporta a la mamá de Frankie."],
            [2,"b. Porque murió de una enfermedad cardiaca."],
            [3,"c. Porque le tocó quedarse en Venezuela."],
        ],
        widget = widgets.RadioSelect
    )

    P3P4_identifica = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    P3P5_celebracion = models.StringField(
        label="5. ¿Que estaban celebrando en el barrio?",
        choices=[
            [1,"a. La inauguración del Centro Cultural Colombo - Venezolano."],
            [2,"b. El cumpleaños de Doralba"],
            [3,"c. La construcción de una piscina en el colegio."],
        ],
        widget = widgets.RadioSelect
    )

    P3P6_pelusa = models.StringField(
        label="6. ¿Con quién vive Pelusa?",
        choices=[
            [1,"a. Con su tía y tío"],
            [2,"b. Con su abuelo y su papa"],
            [3,"c. Con su hermano"],
        ],
        widget = widgets.RadioSelect
    )

    P3P7_amigo = models.StringField(
        label="7. Si le mostrarás esta radionovela, a un amigo o vecino de tu misma edad, crees que:",
        choices=[
            [1,"a. Le parecería interesante y divertida, por lo que escucharía la Radionovela completa."],
            [2,"b. No le prestaría atención, porque le parecería aburrida y poco interesante."],
            [3,"c. No le gustaría y preferiría no escuchar ningún capítulo."],
        ],
        widget = widgets.RadioSelect
    )

    P3P8_familiar = models.StringField(
        label="8. Si le mostrarás esta radionovela, a un familiar tuyo de más edad, como tu mamá o tu abuelo, crees que:",
        choices=[
            [1,"a. Les encantaría, les parecería innovador y entretenido."],
            [2,"b. No llamaría su atención porque pensarían que es una historia para adolescentes."],
            [3,"c. No les gustaría."],
        ],
        widget = widgets.RadioSelect
    )

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


    def generar_numero_aleatorio(self):
        numero_aleatorio = randint(Constants.min_number_random, Constants.max_number_random)

        # Reiniciar la lista de números usados después del capítulo 10
        if self.round_number > 10:
            if numero_aleatorio not in self.session.vars.get('numeros_usados_2', []):
                self.session.vars.setdefault('numeros_usados_2', []).append(numero_aleatorio)
                return numero_aleatorio
            else:
                # Si el número ya fue usado, intentar de nuevo
                return self.generar_numero_aleatorio()
        else:
            if numero_aleatorio not in self.session.vars.get('numeros_usados', []):
                self.session.vars['numeros_usados'].append(numero_aleatorio)
                return numero_aleatorio
            else:
                # Si el número ya fue usado, intentar de nuevo
                return self.generar_numero_aleatorio()



