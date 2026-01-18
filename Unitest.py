import unittest
import Cambia_texto

class ProbarCambiaTexto(unittest.TestCase):
    
    def test_mayusculas(self):
        palabra = 'parametro'
        resultado = Cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'PARAMeTRo')

if __name__ ==  ' __main__':
    unittest.main()
