# python_crypto
## Secure Delivery of Credentials

### Attacking

Actualmente el robo de credenciales es muy frecuente, ya que los atacantes logran tener acceso al correo o los servicios de mensajería, obteniendo en texto plano nuestra credencial.
Principalmente los mayores ataques se dan a las cuentas Cloud como es el caso de AWS, Azure o GCP.
El administrador root de la cuenta, cuando genera un nuevo usuario, este mismo debe proveer la credencial, utilizando canales de comunicación poco seguros, debido a esto los atacantes logran obtener la credencial y hacer uso de los servicio y recursos Cloud para sus beneficios.

<img src="assets/UNID-5.jpg" width="750" height="400"/>

### Asymmetric Encryption

La criptografía asimétrica es uno de los tipos de criptografía informática y una de las técnicas de criptografía más potentes diseñadas en base al uso de una fórmula matemática muy compleja para crear un par de claves: la clave privada y la clave pública. A través de estas claves se establece un canal de comunicación seguro entre las partes, en el que tanto el emisor como el receptor deben usar criptografía asimétrica con un mismo algoritmo definido, que les permitirá crear un juego de claves único e irrepetible para cada uno.

En ese proceso de comunicación, el emisor y el receptor comparten entre ellos sus claves públicas; estas claves cifrarán posteriormente los mensajes que intercambien entre ellos. Y las claves privadas descifrarán esos mensajes para poder ver su contenido. Este proceso hace imposible que un tercero puede interferir en la comunicación y ver el contenido los mensajes.

<img src="assets/ae.png" width="400" height="250"/>


## Aplication SDC

La App SDC o Secure delivery of credentials, ofrece una solución al problema de un envió seguro, generando un cifrado de encriptación RSA, creando una llave publica y una privada para el cifrado. Como tambien un des encriptación de la credencial.

Es totalmente portable para Windows.

### Paso 1

Primero el usuario debe generar sus propias credenciales a traves de la app.exe almacenada en el repositorio de Github, compartiendo la clave publica con el Administrador Root, ya que esta llave solo cifra el texto.

**El usuario NO DEBE COMPARTI su clave privada, de lo contrario se podria acceder al documento cifrado**

<img src="assets/UNID-1.jpg" width="750" height="400"/>

### Paso 2

Una vez obtenida la clave publica por el Administrador Root, puede crear un nuevo usuario en la nube, para este ejemplo utilizaremos AWS Cloud, a traves de la App SDC logra encriptar la contraseña generada por AWS, y realizar el envio seguro del archivo cifrado al nuevo usuario.

<img src="assets/UNID-2.jpg" width="520" height="600"/>

### Paso 3

Al obtener el archivo cifrado el nuevo usuario se dispone a desencriptar el archivo cifrado junto con la clave privada por la App SDC, teniendo como resultado la contraseña de AWS generada de forma segura.

<img src="assets/UNID-3.jpg" width="520" height="600"/>

### Paso 4

AWS Cloud ofrece un segundo nivel de seguridad, al  colocar la contraseña administrada se debe volver a cambiar por una que el usuario genere. La App SDC permite generar una credencial de 20 caracteres alphanumericos de forma random. Logrando que este tipo de credenciales fortalezcan el acceso seguro.

<img src="assets/UNID-4.jpg" width="520" height="600"/>

## MFA

Otro nivel seguridad sugerido es el MFA o Autenticacion Multifactor, el cual genera 6 numeros random cada 30 segundos, los cuales deben ser ingresados una vez introducido la contraseña de AWS Account. Logrando una validacion en tiempo real para un acceso seguro.

En el caso de telefonos android se puede descargar la aplicacion "Google Authenticator" y los pasos de habilitacion en la cuenta cloud.

[Documentacion AWS Cloud MFA Instalacion](https://docs.aws.amazon.com/es_es/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

[Documentacion Azure Cloud MFA Instalacion](https://learn.microsoft.com/es-es/azure/active-directory/authentication/howto-mfaserver-deploy)

[Documentacion GCP Cloud MFA Instalacion](https://cloud.google.com/identity/solutions/enforce-mfa?hl=es)
