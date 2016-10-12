from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
#from django.contrib.auth.models import User
#from polls.models import Trabajador

class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_tittle(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Busco Ayuda", self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        self.browser.implicitly_wait(5)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Diana')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Espitia')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollo Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('123456789')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('dp.espitia@uniandes.edu.co')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('dp.espitia')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\Users\William\Pictures\JuanaBoda.jpg')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('dp.espitia')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(5)
        span = self.browser.find_element(By.XPATH, '//span[text()="Diana Espitia"]')

        self.assertIn('Diana Espitia', span.text)

    def test_verDetalle(self):
        self.browser.get("http://localhost:8000")
        span = self.browser.find_element(By.XPATH, '//span[text()="Diana Espitia"]')
        span.click()

        self.browser.implicitly_wait(5)

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Diana Espitia"]')

        self.assertIn('Diana Espitia', h2.text)


    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        self.browser.implicitly_wait(5)

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('dp.espitia')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('dp.espitia')

        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()
        self.browser.implicitly_wait(5)
        span = self.browser.find_element(By.XPATH, '//span[text()="Diana Espitia"]')

        self.assertIn('Diana Espitia', span.text)
