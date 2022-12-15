# Testing For Squadmakers

## Prequirements or installations

1. VisualStudioCode o cualquier gestor de codigo
2. Python
3. Selenium WebDrivers
4. ChromeDriver.exe
5. Git


## Project Requriments for Run

1. Crear un entono virtual (CMD)
    -Pip install virtualenv
    -virtualenv venv
    -cd venv
    -cd scripts
    -activate

2. Instalar requerimientos y pluggins
    -pip freeze
    -pip install -r requirements.txt


## Features for testing

    - Logout
    - Comprar varios articulos

## Requirements for testing

    -WebPage: https://www.saucedemo.com/
    -User: standard_user
    -Password: secret_sauce
    
## Description by client

El reto se basará en hacer la toma de requerimientos
propuestos y automatizar esas pruebas E2E en la web dada.
Para ello se necesitará crear un repositorio online en el servicio
que se prefiera (Gitlab, Github...) donde se subirá el código
resultante

de la prueba. 

Features; 

1 Comprar uno o varios articulos
2 Hacer logout


# GHERKIN CASUISTIC

## Feature: Login and Logout 

- Folder Casuistic: Login-Logout

- Scenarios: 

1. Pytest1-Login-Logout.py - login y logout de sesión con usuario y contraseña correctos.

    Given: el usuario ha de introducir de forma correcta su usuario y su contraseña, que ha registrado previamente.

    Steps:
        - Ingresar al browser o navegador
        - Ingresar a la web page correspondiente
        - En el campo username ingresar datos de usuario
        - En el campo passowrd ingresar datos de contraseña
        - Hacer click en login o ingresar 

    When: el usuario clica sobre el botón de login.

    Then: el usuario puede iniciar sesión de forma correcta.

    When:. el usuario clica sobre el boton logout.

    Then: el usuario sale de la sesión de forma correcta. 

2. Pytest2-LoginInvalidCredentials.py - Login with invalid credentials.

    Given: el usuario no puede ingresar con contraseñas incorrectas al sistema.

    Steps:
        - Ingresar al browser o navegador
        - Ingresar a la web page correspondiente
        - En el campo username ingresar datos de usuario incorrectos
        - En el campo passowrd ingresar datos de contraseña incorrectos
        - Hacer click en login o ingresar 
        - Verificar mensaje de error de login

    When: el usuario clica sobre el botón de login con credenciales invalidas.

    Then: el usuario no puede iniciar sesión de forma correcta.


## Feature: Shopping Various Articules

- Folder Casuistic: Login-Logout

- Scenarios: 

1. Pytest1-BuyVariousArticules.py - Comprar varios articulos en la tienda o shop.

    Given: el usuario puede seleccionar uno o varios articulos y hacer la compra de estos de forma correcta.

    Steps:
        - Ingresar al browser o navegador
        - Ingresar a la web page correspondiente
        - En el campo username ingresar datos de usuario
        - En el campo passowrd ingresar datos de contraseña
        - Hacer click en login o ingresar 
        - En el Dashboard de productos seleccionar los que desean comprar
        - Una vez agregados al carro de compras verificar resumen de compra
        - Una vez que se verifican los articulos correctos hacer click en boton de checkout
        - Ingresar los datos personales del comprador en checkout form
        - Hacer click en el boton "Continue"
        - Verificar resumen de facturación
        - Hacer click en el boton "Finish"
        - Verificar mensaje de compra satisfactoria

    When: el usuario clica sobre el botón de finish en checkout de compra

    Then: el usuario puede adquiere los productos seleccionados y finaliza la compra de forma satisfactoria


# HOW TO RUN?

## Test By test

Pueden correr las pruebas por separadas ingresando a las rutas de cada test y ejecutando finalmente el archivo.py correspondiente al test deseado a ejecutar. 

- Login Logout:

python ../TestSquadMakers\Login-Logout\Pytest1-Login-Logout.py
python ../TestSquadMakers\Login-Logout\Pytest2-LoginInvalidCredentials.py

- Shopping Various Articules

python ../TestSquadMakers\Shopping\Pytest1-BuyVariousArticules.py

## All test casuistic

Pueden correr toda la pila de prueba ejecutando el archivo "Testing_Runner.py"

python ../TestSquadMakers\Testing_Runner.py



## Important

-el archivo.env es donde se setean los diferentes ambientes o url de prueba
-el archivo requirements.txt es donde se encuentra todo lo necesario a nivel de pluggins e instalaciones para ejecutar el proyecto