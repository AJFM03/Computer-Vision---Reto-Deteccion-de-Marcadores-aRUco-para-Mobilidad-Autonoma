🤖 Detección de Marcadores ArUco para Navegación Autónoma
📌 Contexto

En el University Rover Challenge (URC) existe una misión llamada Navegación Autónoma, donde el rover debe detectar un marcador ArUco en el entorno y desplazarse hacia él de manera inteligente.

Este proyecto implementa un sistema de visión computacional en Python que:

Detecta marcadores ArUco en tiempo real usando una cámara.

Calcula la posición del marcador dentro de la imagen.

Imprime instrucciones en pantalla para que el rover pueda decidir su movimiento:

Mover a la Derecha si el marcador está a la izquierda de la imagen.

Mover a la Iaquierda si está a la derecha.

Avanzar si el marcador está centrado.

De esta forma, se sientan las bases para integrar un sistema de visión en el control autónomo del rover.

🛠️ Requisitos

Antes de ejecutar el programa, instala las siguientes librerías en Python:

pip install opencv-python opencv-contrib-python numpy

📂 Archivos del proyecto

generate_marker.py → Genera un marcador ArUco en formato PNG para imprimir y usar en las pruebas.

detectar_aruco.py → Código principal que captura video en tiempo real, detecta marcadores e imprime la dirección de movimiento.

▶️ Ejecución

Genera un marcador con el script:

python generate_marker.py


Esto creará un archivo como aruco_marker_id_80.png.

Imprime el marcador y colócalo frente a la cámara.

Corre el programa de detección:

python detectar_aruco.py

📷 Funcionamiento

La cámara abre un video en tiempo real.

Si se detecta un marcador ArUco:

Se dibuja un borde alrededor del marcador.

Se marca su centro con un punto verde.

Se imprime en la consola y sobre la imagen la instrucción para el rover:

Mover a la IZQUIERDA

Mover a la DERECHA

AVANZAR

Ejemplo en consola:

ID: 50 | Centro: (312, 240) | Mover a la IZQUIERDA

🎯 Extensiones futuras

Detección de múltiples marcadores al mismo tiempo.

Estimación de distancia al marcador usando la pose 3D.

Integración con el sistema de control del rover para movimiento real.

Pruebas en condiciones de iluminación y terrenos variables (simulando el URC).

🚀 Conclusión

Este proyecto demuestra cómo la visión por computadora con OpenCV puede aplicarse en la misión de Navegación Autónoma del URC, detectando marcadores ArUco y generando instrucciones simples de movimiento que luego pueden ser enviadas al rover para su desplazamiento automático.
