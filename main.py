from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class AlarmApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        self.sound = SoundLoader.load('alarm.mp3')

        btn = Button(
            text='播放闹铃',
            font_size=32
        )
        btn.bind(on_press=self.play_sound)

        layout.add_widget(btn)
        return layout

    def play_sound(self, instance):
        if self.sound:
            self.sound.play()

if __name__ == '__main__':
    AlarmApp().run()
