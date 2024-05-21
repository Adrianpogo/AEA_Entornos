import json


class Libreria:
    """
    Una clase para representar una biblioteca de libros.

    Métodos públicos:
    - anadir_libro: Añade un libro a la biblioteca.
    - buscar_libro: Busca un libro por su título.
    - buscar_por_autor: Busca libros por un autor.
    - eliminar_libro: Elimina un libro por su título.
    - guardar_libros: Guarda la lista de libros en un archivo JSON.
    - cargar_libros: Carga la lista de libros desde un archivo JSON.
    - contar_libros: Cuenta el número de libros.

    """

    def __init__(self):
        """Inicializa una instancia de la clase Libreria con una lista vacía de libros."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la biblioteca.

        Parámetros:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        genero (str): El género del libro.
        anio (int): El año de publicación del libro.

        Retorna:
        str: Un mensaje indicando que el libro ha sido añadido.
        """
        self.libros.append({
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'anio': anio
        })
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Parámetros:
        titulo (str): El título del libro que se busca.

        Retorna:
        list: Una lista de libros que coinciden con el título buscado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por un autor.

        Parámetros:
        autor (str): El autor de los libros que se buscan.

        Retorna:
        list: Una lista de libros que coinciden con el autor buscado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por su título.

        Parámetros:
        titulo (str): El título del libro que se desea eliminar.

        Retorna:
        str: Un mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la lista de libros en un archivo JSON.

        Parámetros:
        archivo (str): La ruta del archivo donde se guardarán los libros.

        Retorna:
        str: Un mensaje indicando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la lista de libros desde un archivo JSON.

        Parámetros:
        archivo (str): La ruta del archivo desde donde se cargarán los libros.

        Retorna:
        str: Un mensaje indicando si los libros han sido cargados o si el archivo no se encontró.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"
        
    
    def contar_libros(self):
        """
        Devuelve el número de libros en la biblioteca.

        Retorna:
        int: El número de libros en la biblioteca.
        """
        return len(self.libros)


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))