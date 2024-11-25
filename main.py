from kivy.app import App
from controller import CameraController

class CameraApp(App):
    def build(self):
        self.controller = CameraController()  # Lancer le contrôleur
        return self.controller.view  # Retourner la vue associée au contrôleur

    def on_stop(self):
        """Libérer la caméra lorsque l'application est fermée."""
        self.controller.stop_camera()

if __name__ == '__main__':
    CameraApp().run()
