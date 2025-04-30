# USB Keylogger PoC – Basado en Autorun y Python

Cuando el USB empezó a hacerse popular —por ser liviano, práctico y súper útil para guardar información— también empezaron a circular historias de “USBs con virus”. Y no era paranoia: estos dispositivos podían contener malware que se ejecutaba apenas los conectabas a una computadora.

Esto era posible gracias a una función de Windows llamada **autorun.inf**, que permitía que ciertos archivos se ejecutaran automáticamente al insertar el dispositivo. Los atacantes aprovechaban esta funcionalidad para propagar malware de manera sencilla y silenciosa.

## ⚙¿Qué hace este PoC?

Básicamente, se trata de un keylogger que:
- Captura las pulsaciones del teclado.
- Guarda cada palabra en un archivo `output.txt`.
- Envía ese archivo a través de sockets a una máquina atacante cuando la víctima presiona la tecla **ESC**.

## ¿Cómo fue desarrollado?

### Modificación del código
Adapté el código original para que se ajustara a mi red local, eligiendo:
- La IP de mi **localhost** para recibir el archivo.
- El puerto **447** como canal de comunicación.
- La tecla **ESC** como desencadenante del envío (por ser poco usada).

###  Ofuscación con IA
Luego decidí **ofuscar el código** usando inteligencia artificial. Esto ayuda a que el ejecutable final sea más difícil de analizar, ocultando su lógica interna y evitando detecciones simples.

### Creación del .exe
Usé **auto-py-to-exe** para convertir el script en un ejecutable `.exe`. Activé las opciones:
- `onefile`: empaqueta todo en un solo archivo.
- `hide console`: evita que se abra una ventana negra al ejecutarlo, haciéndolo más discreto.

### VirusTotal – Antes y después
- Al principio, el ejecutable fue detectado por **15 de 72** motores antivirus.
- Luego, al **firmarlo con un certificado autofirmado** usando una herramienta de GitHub, lo volví a subir a VirusTotal y el resultado fue **3 de 71**. 
> ¡Una gran diferencia!

### Creación del autorun.inf
Utilicé el programa **Autorun Creator** para generar un archivo `autorun.inf` con el siguiente contenido:
[AutoRun] OPEN=KEYLOGGEROFUSCADO.EXE LABEL=- USB Flash Drive 250429 -


Este archivo le indica a Windows que ejecute el programa automáticamente al insertar la USB.

## Prueba del PoC

Para la prueba final utilicé dos máquinas virtuales:
- Una con **Windows 10** (víctima), donde inserté la USB.
- Otra con **Parrot OS** (atacante), escuchando con Netcat en el puerto 447.

Desde el Administrador de tareas de Windows pude confirmar que el proceso `keyloggerofuscado.exe` se ejecutaba en segundo plano **incluso con Windows Defender activado**.

El ejecutable comenzaba a registrar las pulsaciones del teclado apenas se ejecutaba. Al presionar la tecla ESC, se enviaba automáticamente el archivo con las capturas al equipo atacante.

## ¿Esto funcionaría en un entorno real?

Sí, **bajo ciertas condiciones**:
- Si el usuario ejecuta el archivo manualmente (ya que `autorun.inf` está deshabilitado por defecto en Windows modernos).
- Usando técnicas de **ingeniería social** o herramientas como **Rubber Ducky** para simular la ejecución.
- Siempre que el ejecutable logre evadir al antivirus, lo cual —como vimos— es posible con técnicas de ofuscación y firma.

Aunque la ejecución automática podría fallar por políticas de seguridad actuales, **el ejecutable sigue siendo funcional** y tiene capacidad para operar silenciosamente y evadir detecciones.

---

## Advertencia ética

Este proyecto fue creado con fines **educativos** y de **concientización en ciberseguridad**. No debe utilizarse con propósitos maliciosos ni en sistemas donde no se tenga autorización explícita.

El objetivo es mostrar cómo prácticas aparentemente obsoletas aún pueden tener impacto si se combinan con técnicas modernas.

---

## Créditos

Inspirado por el video de ["El Pingüino de Mario"](https://www.youtube.com/@ElPinguinoDeMario) sobre cómo crear un keylogger en Python. 
Y en los repositorios: https://github.com/Maalfer/python_keylogger/blob/main/script.py
https://github.com/ArtesOscuras/AV_bypass_with_python





