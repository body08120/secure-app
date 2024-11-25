import cv2
from kivy.graphics.texture import Texture


class CameraModel:
    def __init__(self):
        self.capture = None

    def start_camera(self):
        """Initialise la caméra et commence à lire le flux."""
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            print("Erreur : Impossible d'ouvrir la caméra")
            return False
        return True

    def get_frame(self):
        """Retourne une image de la caméra sous forme de texture."""
        ret, frame = self.capture.read()
        if not ret:
            print("Erreur : Impossible de lire la frame")
            return None

        # Convertir le frame en texture
        buf = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        return texture

    def stop_camera(self):
        """Libère la caméra."""
        if self.capture:
            self.capture.release()
