class Persona: #Se crea la clase Persona
    def __init__(self, id, nombre, apellidos): 
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
    
    def mostrar_info(self):
        print(f"Persona: {self.nombre} {self.apellidos}, ID: {self.id}") 

class Artista(Persona): #Se crea la clase Artista
    def __init__(self, id_artista, nombre, apellidos, nacionalidad, tecnica_pintura): #el __init__ sirve para iniciar los atributos de la clase
        super().__init__(id_artista, nombre, apellidos) #se llama a la clase padre con super() que sirve para heredar atributos y métodos de la clase padre
        self.nacionalidad = nacionalidad
        self.tecnica_pintura = tecnica_pintura
        self.pinturas = [] # Lista para almacenar muchas pinturas del artista

    def mostrar_info(self): #método para mostrar la información del artista
        print(f"Artista: {self.nombre}, Nacionalidad: {self.nacionalidad}, Técnica: {self.tecnica_pintura}") #se llama self para referirse a los atributos de la clase

    def enviar_propuesta_exhibicion(self): #método para enviar una propuesta de exhibición
        print(f"{self.nombre} envió una propuesta de exhibición.")

    def enviar_pinturas(self, pintura): #método para enviar pinturas
        self.pinturas.append(pintura)

class Pintura: #Se crea la clase Pintura
    def __init__(self, titulo, fecha_creacion, artista): #se inician los atributos de la clase
        self.titulo = titulo
        self.fecha_creacion = fecha_creacion
        self.autor = artista # Relación con la clase Artista

    def exhibir(self):
        print(f"Exhibiendo pintura: {self.titulo} de {self.autor.nombre}")

class MuseoDeArte:
    def __init__(self, id_museo, nombre, direccion, telefono):
        self.id_museo = id_museo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.pinturas = [] # Lista para almacenar muchas pinturas en el museo
        self.asesores = [] # Lista para almacenar muchos asesores en el museo

    def lanzar_exhibicion(self, exhibicion):
        print(f"Museo {self.nombre} lanza la exhibición: {exhibicion.titulo}")

    def mostrar_info(self):
        print(f"Museo: {self.nombre}, Dirección: {self.direccion}, Tel: {self.telefono}")

class Asesor(Persona):
    def __init__(self, id_asesor, nombre, apellidos):
        super().__init__(id_asesor, nombre, apellidos) #hereda de la clase padre 

    def notificar_estado_propuesta(self):
        print(f"Asesor {self.nombre} notificó estado de propuesta.")

    def enviar_sugerencias(self): # método para enviar sugerencias
        print(f"Asesor {self.nombre} envió sugerencias.")

class Exhibicion:
    def __init__(self, id_exhibicion, titulo, fecha_comienzo, fecha_finalizacion):
        self.id_exhibicion = id_exhibicion
        self.titulo = titulo
        self.fecha_comienzo = fecha_comienzo
        self.fecha_finalizacion = fecha_finalizacion
        self.pinturas = [] # Lista para almacenar muchas pinturas en la exhibición

    def mostrar_info(self):
        print(f"Exhibición: {self.titulo}, Empieza: {self.fecha_comienzo}, Termina: {self.fecha_finalizacion}")

class Visitante(Persona):
    def __init__(self, id_visitante, nombre, apellidos):
        super().__init__(id_visitante, nombre, apellidos)

    def dar_comentarios(self):
        print(f"Visitante {self.nombre} dejó un comentario.")

    def comprar_entradas(self):
        print(f"{self.nombre} compró una entrada.")

    def asistir_exhibicion(self, exhibicion):
        print(f"{self.nombre} asistió a la exhibición: {exhibicion.titulo}")

def mostrar_informacion_objeto(objeto):
    objeto.mostrar_info()

#Ejemplo
# Artista
vincent = Artista( 
    id_artista=1,
    nombre="Vincent",
    apellidos="van Gogh",
    nacionalidad="Neerlandés",
    tecnica_pintura="Óleo sobre lienzo"
)
# Pintura
noche_estrellada = Pintura(
    titulo="La Noche Estrellada",
    fecha_creacion="1889",
    artista=vincent
)
noche_estrellada.exhibir()  # pintura en exhibición
# Asesor
geraldo = Asesor(
    id_asesor=203,
    nombre="Geraldo",
    apellidos="Perez Ramirez"
)
geraldo.enviar_sugerencias()  # El asesor envía sugerencias
# Visitante
samantha = Visitante(
    id_visitante=420,
    nombre="Samantha",
    apellidos="García López"
)
samantha.comprar_entradas()  # El visitante compra entradas
# Exhibición
expo = Exhibicion(
    id_exhibicion=1,
    titulo="Van Gogh y los Colores de la Noche",
    fecha_comienzo="20/08/2025",
    fecha_finalizacion="26/08/2025"
)
# Museo de arte
museo_van_gogh = MuseoDeArte(
    id_museo=100,
    nombre="Museo Van Gogh",
    direccion="Museumplein 6, 1071 DJ Amsterdam",
    telefono=31205705200
)
#relaciones
museo_van_gogh.pinturas.append(noche_estrellada) #se cita primero a el museo, la lista pinturas y se añade la pintura
museo_van_gogh.asesores.append(geraldo)
expo.pinturas.append(noche_estrellada)
samantha.asistir_exhibicion(expo)
# Comentario visitante
samantha.dar_comentarios()
objetos = [vincent, expo, museo_van_gogh]
for objeto in objetos:
    mostrar_informacion_objeto(objeto)

