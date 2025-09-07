import cv2
import numpy as np

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)

cap = cv2.VideoCapture(0)  # 0 = cámara web principal

# Definir parámetros del detector
parameters = cv2.aruco.DetectorParameters()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los marcadores
    corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None:
        for i, corner in enumerate(corners):
            # Dibujar el marcador detectado
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

            # Calcular el centro del marcador
            pts = corner[0]
            x_center = int((pts[0][0] + pts[1][0] + pts[2][0] + pts[3][0]) / 4)
            y_center = int((pts[0][1] + pts[1][1] + pts[2][1] + pts[3][1]) / 4)

            # Dibujar un círculo en el centro
            cv2.circle(frame, (x_center, y_center), 5, (0, 255, 0), -1)

            # Obtener el centro de la pantalla
            frame_height, frame_width, _ = frame.shape
            center_frame = frame_width // 2

            # Dibujar línea central de referencia
            cv2.line(frame, (center_frame, 0), (center_frame, frame_height), (255, 0, 0), 2)

            # Decidir la dirección
            if x_center < center_frame - 50:
                direction = "Mover a la IZQUIERDA"
            elif x_center > center_frame + 50:
                direction = "Mover a la DERECHA"
            else:
                direction = "AVANZAR"

            # Imprimir en consola
            print(f"ID: {ids[i][0]} | Centro: ({x_center}, {y_center}) | {direction}")

            # Mostrar en la ventana
            cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (0, 0, 255), 2, cv2.LINE_AA)

    # Mostrar video
    cv2.imshow("Detección de ArUco", frame)

    # Presionar 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
