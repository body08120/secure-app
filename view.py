from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics.texture import Texture
from kivy.core.window import Window


class CameraView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'

        # Fixer la hauteur de la caméra
        camera_height = 400
        camera_width = 600

        # Ajuster la taille de la fenêtre à la caméra
        Window.size = (camera_width + 200, camera_height)  # Ajouter la largeur du bouton (200 px)

        # Layout principal : caméra
        self.camera_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.img_widget = Image(size_hint=(1, None), height=camera_height)  # Hauteur de la caméra fixée
        self.camera_layout.add_widget(self.img_widget)

        # Layout principal : bouton
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
        self.add_widget(self.camera_layout)
        self.add_widget(self.button_layout)

    def update_image(self, texture):
        """Met à jour l'image affichée par la caméra."""
        self.img_widget.texture = texture
