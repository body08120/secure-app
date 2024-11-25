from kivy.clock import Clock
from model import CameraModel
from view import CameraView

class CameraController:
    def __init__(self):
        self.model = CameraModel()  # Instance du modèle
        self.view = CameraView()  # Instance de la vue

        if self.model.start_camera():
            # Planifie la mise à jour de la caméra toutes les 1/30 secondes
            Clock.schedule_interval(self.update_camera_feed, 1.0 / 30.0)

    def update_camera_feed(self, dt):
        """Mise à jour de l'image de la caméra."""
        texture = self.model.get_frame()
        if texture:
            self.view.update_image(texture)

    def stop_camera(self):
        """Arrête la caméra lorsque l'application est fermée."""
        self.model.stop_camera()
