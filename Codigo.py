
class Artista:
    def __init__(self, nombre, nacionalidad, tecnica_pintura):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.tecnica_pintura = tecnica_pintura
        self.pinturas = []

    def mostrar_info(self):
        print(f"Artista: {self.nombre}, Nacionalidad: {self.nacionalidad}, Técnica: {self.tecnica_pintura}")

    def enviar_propuesta_exhibicion(self):
        print(f"{self.nombre} envió una propuesta de exhibición.")

    def enviar_pinturas(self, pintura):
        self.pinturas.append(pintura)


class Pintura:
    def __init__(self, titulo, fecha_creacion, artista):
        self.titulo = titulo
        self.fecha_creacion = fecha_creacion
        self.autor = artista

    def exhibir(self):
        print(f"Exhibiendo pintura: {self.titulo} de {self.autor.nombre}")


class MuseoDeArte:
    def __init__(self, id_museo, nombre, direccion, telefono):
        self.id_museo = id_museo
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.pinturas = []
        self.asesores = []

    def lanzar_exhibicion(self, exhibicion):
        print(f"Museo {self.nombre} lanza la exhibición: {exhibicion.titulo}")

    def mostrar_informacion(self):
        print(f"Museo: {self.nombre}, Dirección: {self.direccion}, Tel: {self.telefono}")


class Asesor:
    def __init__(self, id_asesor, nombre, apellidos):
        self.id_asesor = id_asesor
        self.nombre = nombre
        self.apellidos = apellidos

    def notificar_estado_propuesta(self):
        print(f"Asesor {self.nombre} notificó estado de propuesta.")

    def enviar_sugerencias(self):
        print(f"Asesor {self.nombre} envió sugerencias.")


class Exhibicion:
    def __init__(self, id_exhibicion, titulo, fecha_comienzo, fecha_finalizacion):
        self.id_exhibicion = id_exhibicion
        self.titulo = titulo
        self.fecha_comienzo = fecha_comienzo
        self.fecha_finalizacion = fecha_finalizacion
        self.pinturas = []

    def mostrar_info_exhibicion(self):
        print(f"Exhibición: {self.titulo}, Empieza: {self.fecha_comienzo}, Termina: {self.fecha_finalizacion}")


class Visitante:
    def __init__(self, id_visitante, nombre, apellidos):
        self.id_visitante = id_visitante
        self.nombre = nombre
        self.apellidos = apellidos

    def dar_comentarios(self):
        print(f"Visitante {self.nombre} dejó un comentario.")

    def comprar_entradas(self):
        print(f"{self.nombre} compró una entrada.")

    def asistir_exhibicion(self, exhibicion):
        print(f"{self.nombre} asistió a la exhibición: {exhibicion.titulo}")

# Creación de objetos según el diagrama de objetos proporcionado

# Artista
vincent = Artista(
    nombre="Vincent van Gogh",
    nacionalidad="Neerlandés",
    tecnica_pintura="Óleo sobre lienzo"
)
vincent.mostrar_info()  # información del artista

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
    fecha_comienzo="20/06/2025",
    fecha_finalizacion="26/06/2025"
)
expo.mostrar_info_exhibicion()  # Información de la exhibición

# Museo de arte
museo_van_gogh = MuseoDeArte(
    id_museo=100,
    nombre="Museo Van Gogh",
    direccion="Museumplein 6, 1071 DJ Amsterdam",
    telefono=31205705200
)
museo_van_gogh.mostrar_informacion()  # Información del museo

# Establecimiento de relaciones
museo_van_gogh.pinturas.append(noche_estrellada)
museo_van_gogh.asesores.append(geraldo)
expo.pinturas.append(noche_estrellada)
samantha.asistir_exhibicion(expo)

# Comentario del visitante
samantha.dar_comentarios()