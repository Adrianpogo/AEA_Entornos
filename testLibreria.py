import unittest
import os
from libreria import Libreria


class TestLibreria(unittest.TestCase):
    """
    Clase de pruebas para la clase Libreria.
    """

    def setUp(self):
        """
        Configuración de las pruebas.
        """
        self.libreria = Libreria()
        self.test_file = 'test_libreria.json'
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)

    def tearDown(self):
        """
        Limpieza después de cada prueba.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_anadir_libro(self):
        """
        Prueba para el método anadir_libro.
        """
        # Caso típico
        self.assertEqual(self.libreria.anadir_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", 1985), "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 2)

        # Caso extremo: Añadir un libro con título vacío
        self.assertEqual(self.libreria.anadir_libro("", "Autor", "Género", 2000), "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 3)

    def test_buscar_libro(self):
        """
        Prueba para el método buscar_libro.
        """
        # Caso típico
        self.assertEqual(len(self.libreria.buscar_libro("Cien años de soledad")), 1)
        self.assertEqual(len(self.libreria.buscar_libro("El principito")), 0)

        # Caso extremo: Buscar con título vacío
        self.assertEqual(len(self.libreria.buscar_libro("")), 0)

    def test_buscar_por_autor(self):
        """
        Prueba para el método buscar_por_autor.
        """
        # Caso típico
        self.assertTrue(len(self.libreria.buscar_por_autor("Gabriel García Márquez")) > 0)
        self.assertEqual(len(self.libreria.buscar_por_autor("J.K. Rowling")), 0)


    def test_eliminar_libro(self):
        """
        Prueba para el método eliminar_libro.
        """
        # Caso típico
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 0)
        self.assertEqual(self.libreria.eliminar_libro("El principito"), "Libro no encontrado")

        # Caso extremo: Eliminar un libro con título vacío
        self.assertEqual(self.libreria.eliminar_libro(""), "Libro no encontrado")

    def test_guardar_cargar_libros(self):
        """
        Prueba para los métodos guardar_libros y cargar_libros.
        """
        # Caso típico
        self.assertEqual(self.libreria.guardar_libros(self.test_file), "Libros guardados")
        self.assertTrue(os.path.exists(self.test_file))
        self.libreria = Libreria()  # Reiniciar la librería para cargar desde el archivo
        self.assertEqual(self.libreria.cargar_libros(self.test_file), "Libros cargados")
        self.assertEqual(len(self.libreria.libros), 1)

        # Caso extremo: Cargar desde un archivo inexistente
        self.assertEqual(self.libreria.cargar_libros("archivo_inexistente.json"), "Archivo no encontrado")

    def test_contar_libros(self):
        """
        Prueba para el método contar_libros.
        """
        # Caso típico
        self.assertEqual(self.libreria.contar_libros(), 1)
        self.libreria.anadir_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", 1985)
        self.assertEqual(self.libreria.contar_libros(), 2)

        # Caso extremo: Contar libros en una biblioteca vacía
        self.libreria = Libreria()
        self.assertEqual(self.libreria.contar_libros(), 0)


if __name__ == '__main__':
    unittest.main()
