from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.core.window import Window
import cv2

class CameraApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.capture = None

    def build(self):
        # Fixer la hauteur de la caméra
        camera_height = 400
        camera_width = 600

        # Ajuster la taille de la fenêtre à la caméra
        Window.size = (camera_width + 200, camera_height)  # Ajouter la largeur du bouton (200 px)

        # Layout principal horizontal
        main_layout = BoxLayout(orientation='horizontal', spacing=0, padding=0)

        # Zone caméra
        self.camera_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.img_widget = Image(size_hint=(1, None), height=camera_height)
        self.camera_layout.add_widget(self.img_widget)

        # Zone bouton
        self.button_layout = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        self.button_identify = Button(
            text="S'identifier",
            font_size=20,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}  # Centré horizontalement dans sa colonne
        )
        self.button_layout.add_widget(self.button_identify)
        self.button_layout.add_widget(BoxLayout(size_hint=(1, 1)))  # Spacer pour aligner le bouton en haut

        # Ajouter les deux sous-layouts au layout principal
        main_layout.add_widget(self.camera_layout)
        main_layout.add_widget(self.button_layout)

        # Ouvrir la caméra
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            print("Erreur : Impossible d'ouvrir la caméra")
            return main_layout

        # Planifier la mise à jour de la caméra
        Clock.schedule_interval(self.update_camera_feed, 1.0 / 30.0)

        return main_layout

    def update_camera_feed(self, dt):
        """Mettre à jour l'image de la caméra dans l'interface."""
        ret, frame = self.capture.read()
        if not ret:
            print("Erreur : Impossible de lire la frame")
            return

        # Convertir le frame en texture
        buf = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img_widget.texture = texture

    def on_stop(self):
        """Libérer la caméra lorsque l'application est fermée."""
        if self.capture:
            self.capture.release()

if __name__ == '__main__':
    CameraApp().run()
