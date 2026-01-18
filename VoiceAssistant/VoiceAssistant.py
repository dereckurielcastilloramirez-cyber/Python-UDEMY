import speech_recognition as sr            #reconocimiento de voz
import pyttsx3                             #sintesis de voz para que hable el asistente
import pywhatkit                           #navegador web y youtube
import yfinance as yf                      #acceder a la API de yfinance y finanzas
import pyjokes                             #acceder ajokes
import webbrowser                          #navegador web
import wikipedia                           #buscador de wikipedia
import datetime

#Configuracion de idioma

id1= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
id2= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id4= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"


#escuchar microfono y devolver el audio como texto
def transformar_audio_en_texto():

    #almacenar recognizer en variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:
    
        #tiempo de espera para el reconocimiento de voz
        r.pause_threshold = 1              #umbral de tiempo para el reconocimiento de voz

        #indicar que comenzo a grabar el audio
        print("Puede comenzar a hablar")

        #guardar el audio
        audio = r.listen(origen)
    

        try:
            #buscar en google el audio
            pedido = r.recognize_google(audio, language="es-mx")  #metodo de reconocimiento de voz de google para español
            #Prueba de reconocimiento de voz
            print(f'Dijiste: {pedido}')

            return pedido
        
        #Caso de no comprender el audio
        except sr.UnknownValueError:
            print("No te he entendido")
            return "intenta de nuevo"

        #Encaso de no devolver el string
        except sr.RequestError:
            print("Mi no entender")
            return "intenta de nuevo"
        
        #En caso general que no se sepa el error
        except:
            print("Algo anda mal")
            return "intenta de nuevo"

#funcion para que el assistente responda a las preguntas
def hablar(mensaje):

    #encender el motor de voz pyttsx3
    engine = pyttsx3.init()

    #configurar la voz
    engine.setProperty('voice', id1)

    #pronunciar el mensaje
    engine.say(mensaje)

    #esperar el tiempo de espera de la voz
    engine.runAndWait()

#funcion para pedir el dia
def pedir_dia():
    #crear variable con la fecha
    dia = datetime.date.today()
    print(dia)
    #crear variable con el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    
    dicccionario = {0: 'Lunes',
                    1: 'Martes',
                    2: 'Miércoles',
                    3: 'Jueves',
                    4: 'Viernes',
                    5: 'Sabado',
                    6: 'Domingo'}
    
    #decir dia de la semana
    hablar(f' Hoy es {dicccionario[dia_semana]}')

#funcion para pedir la hora
def pedir_hora():

    #crear variable con la hora 
    hora = datetime.datetime.now().time()
    hora = f'Son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    #decir la hora
    hablar(f'La hora es {hora}')

#funcion para saludar
def saludo_inicial():

    #datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    #decir saludo
    hablar(f'{momento} señor, Yarvis a su servicio, ¿En qué puedo ayudarle?')

#---------------CENTRAL DE CONTROL DE PEDIDOS-----------------

def central_de_control_de_pedidos(): 

    #activar saludo inicial
    saludo_inicial()


    comenzar = True
    while comenzar:
        
        #activar el microfono y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            #abrir navegador web
            hablar('Claro señor, abriendo Youtube')

            #abrir navegador web
            webbrowser.open('https://www.youtube.com')

            continue

        elif 'abrir navegador' in pedido:
            #abrir navegador web
            hablar('Claro señor, abriendo navegador web')

            #abrir navegador web
            webbrowser.open('https://www.google.com')

            continue

                
        elif 'qué día es hoy' in pedido:
            #pedir el dia
            hablar('Claro señor')
            pedir_dia()
            continue
        
        elif 'qué hora es' in pedido:
            #pedir la hora
            hablar('Claro señor')
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            #buscar en wikipedia
            hablar('Claro señor, buscando en wikipedia')
        
            pedido = pedido.replace('busca en wikipedia', '')

            #buscar en wikipedia
            wikipedia.set_lang('es') #establecer idioma
            resultado = wikipedia.summary(pedido, sentences=1) # buscar en wikipedia el pedido pero el primer parrafo
            hablar(f'Wikipedia dice: {resultado}')

            continue
        
        elif 'busca en google' in pedido:
            #buscar en google
            hablar('Claro señor, buscando en google')
            pedido = pedido.replace('busca en google', '')
            pywhatkit.search(pedido)
            hablar('Esto encontré en google')
            continue
        
        elif 'reproducir' in pedido:
            #reproducir audio
            hablar('Claro señor, reproduciendo')
            
            pywhatkit.playonyt(pedido)

            continue
        
        elif 'broma' in pedido:
            #reproducir audio
            hablar('Claro señor, reproduciendo broma')
            hablar(pyjokes.get_joke('es'))
    
            continue

        elif 'precio de las acciones' in pedido:
            #pedir el precio de las acciones
            hablar('Claro señor, pidiendo el precio de las acciones')
            accion = pedido.split('de')[-1] #al final de la cadena de texto que es la empresa

            cartera ={'apple' : 'APPL',
                      'amazon': 'AMZN',
                      'google': 'GOOGL',
                      'tesla' : 'TSLA'} #crear objeto de la API de yfinance
            try: 
                accion_buscada = cartera[accion] #buscar accion en el diccionario
                accion_buscada = yf.Ticker(accion_buscada) #crear objeto de la API de yfinance
                precio_actual = accion_buscada.info['regularMarketPrice'] #obtener precio de la accion, por clase RegularMarketPrice
                hablar(f'El precio de la accion {accion} es de {precio_actual} dolares por accion')
                continue
            except:
                hablar('No se encontró esa accion señor')
                continue

        elif 'salir' or 'adios' in pedido:
            #decir despedida
            hablar('De acuerdo señor, sigo a su servicio, hasta luego')
            break

central_de_control_de_pedidos()