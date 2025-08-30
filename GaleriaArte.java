public class GaleriaArte {  //se crea la clase principal GaleriaArteApp
    // Clase Persona
    static class Persona {
        protected int id;
        protected String nombre;
        protected String apellidos;

        public Persona(int id, String nombre, String apellidos) {
            this.id = id;
            this.nombre = nombre;
            this.apellidos = apellidos;
        }

        public void mostrarInfo() {
            System.out.println("Persona: " + nombre + " " + apellidos + ", ID: " + id);
        }
    }

    // Clase Artista
    static class Artista extends Persona {
        private String nacionalidad;
        private String tecnicaPintura;

        public Artista(int id, String nombre, String apellidos, String nacionalidad, String tecnicaPintura) {
            super(id, nombre, apellidos); 
            this.nacionalidad = nacionalidad;
            this.tecnicaPintura = tecnicaPintura;
        }

        public void mostrarInfo() {
            System.out.println("Artista: " + nombre + ", Nacionalidad: " + nacionalidad + ", Técnica: " + tecnicaPintura);
        }

        public void enviarPropuestaExhibicion() {
            System.out.println(nombre + " envió una propuesta de exhibición.");
        }

        public void enviarPinturas() {
            System.out.println(nombre + " envió la pintura ");
        }
    }

    // Clase Pintura
    static class Pintura {
        private String titulo;
        private String fechaCreacion;
        private Artista autor;

        public Pintura(String titulo, String fechaCreacion, Artista autor) {
            this.titulo = titulo;
            this.fechaCreacion = fechaCreacion;
            this.autor = autor;
        }

        public void exhibir() {
            System.out.println("Exhibiendo pintura: " + titulo + " de " + autor.nombre);
        }
    }

    // Clase MuseoDeArte
    static class MuseoDeArte {
        private int idMuseo;
        private String nombre;
        private String direccion;
        private long telefono;
        public java.util.ArrayList<Pintura> pinturas = new java.util.ArrayList<>();
        public java.util.ArrayList<Asesor> asesores = new java.util.ArrayList<>();

        public MuseoDeArte(int idMuseo, String nombre, String direccion, long telefono) {
            this.idMuseo = idMuseo;
            this.nombre = nombre;
            this.direccion = direccion;
            this.telefono = telefono;
        }

        public void lanzarExhibicion(Exhibicion exhibicion) {
            System.out.println("Museo " + nombre + " lanza la exhibición: " + exhibicion.getTitulo());
        }

        public void mostrarInfo() {
            System.out.println("Museo: " + nombre + ", Dirección: " + direccion + ", Tel: " + telefono);
        }
    }

    // Clase Asesor
    static class Asesor extends Persona {
        public Asesor(int id, String nombre, String apellidos) {
            super(id, nombre, apellidos);
        }

        public void notificarEstadoPropuesta() {
            System.out.println("Asesor " + nombre + " notificó estado de propuesta.");
        }

        public void enviarSugerencias() {
            System.out.println("Asesor " + nombre + " envió sugerencias.");
        }
    }

    // Clase Exhibicion
    static class Exhibicion {
        private int idExhibicion;
        private String titulo;
        private String fechaComienzo;
        private String fechaFinalizacion;
        public java.util.ArrayList<Pintura> pinturas = new java.util.ArrayList<>();

        public Exhibicion(int idExhibicion, String titulo, String fechaComienzo, String fechaFinalizacion) {
            this.idExhibicion = idExhibicion;
            this.titulo = titulo;
            this.fechaComienzo = fechaComienzo;
            this.fechaFinalizacion = fechaFinalizacion;
        }

        public void mostrarInfo() {
            System.out.println("Exhibición: " + titulo + ", Empieza: " + fechaComienzo + ", Termina: " + fechaFinalizacion);
        }

        public String getTitulo() {
            return titulo;
        }
    }

    // Clase Visitante
    static class Visitante extends Persona { //extends indica que hereda de la clase Persona
        public Visitante(int id, String nombre, String apellidos) {
            super(id, nombre, apellidos);
        }

        public void darComentarios() {
            System.out.println("Visitante " + nombre + " dejó un comentario.");
        }

        public void comprarEntradas() {
            System.out.println(nombre + " compró una entrada.");//El sistem out es para imprimir en consola
        }

        public void asistirExhibicion(Exhibicion exhibicion) {//PUBLIC ES UN ESPECIFICADOR DE ACCESO, VOID INDICA QUE NO RETORNA NADA
            System.out.println(nombre + " asistió a la exhibición: " + exhibicion.getTitulo());
        }
    }

    // Método main: es el punto de entrada del programa
    public static void main(String[] args) { //public static especificador de acceso y modificador de método, void indica que no retorna nada
        Artista vincent = new Artista(1, "Vincent", "van Gogh", "Neerlandés", "Óleo sobre lienzo");
        vincent.mostrarInfo();
        vincent.enviarPropuestaExhibicion();
        vincent.enviarPinturas();
        Pintura nocheEstrellada = new Pintura("La Noche Estrellada", "1889", vincent); //new indica que se está creando un nuevo objeto
        nocheEstrellada.exhibir();
        Exhibicion expo = new Exhibicion(1, "Van Gogh y los Colores de la Noche", "20/08/2025", "26/08/2025");
        expo.mostrarInfo();
        Visitante samantha = new Visitante(420, "Samantha", "García López");
        samantha.comprarEntradas();
        samantha.asistirExhibicion(expo);
        samantha.darComentarios();
        Asesor geraldo = new Asesor(203, "Geraldo", "Perez Ramirez");
        geraldo.enviarSugerencias();
        MuseoDeArte museoVanGogh = new MuseoDeArte(100, "Museo Van Gogh", "Museumplein 6, 1071 DJ Amsterdam", 3120505200L);
        museoVanGogh.mostrarInfo();
        museoVanGogh.pinturas.add(nocheEstrellada);
        museoVanGogh.asesores.add(geraldo);
        expo.pinturas.add(nocheEstrellada);
        }
    }

