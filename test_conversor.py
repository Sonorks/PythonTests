import unittest
import conversor


class TestConversor(unittest.TestCase):

    def test_convertir_diez_a_romano(self):
        self.assertEqual(conversor.convertir(10),'X')
        #self.assertRaises(UnboundLocalError, lambda: conversor.convertir(101))

    def test_convertir_numero_mayor_a_cien_excepcion(self):
        self.assertRaises(UnboundLocalError, lambda: conversor.convertir(101))

if __name__ == "__main__":
    unittest.main()