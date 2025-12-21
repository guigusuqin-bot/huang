from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
import os
import shutil


class AlarmApp(App):
    def build(self):
        self.sound = None

        layout = BoxLayout(
            orientation="vertical",
            padding=40,
            spacing=30
        )

        self.play_btn = Button(
            text="播放闹铃",
            font_size=32,
            size_hint=(1, 0.4)
        )
        self.play_btn.bind(on_press=self.play_alarm)

        self.stop_btn = Button(
            text="停止闹铃",
            font_size=32,
            size_hint=(1, 0.4)
        )
        self.stop_btn.bind(on_press=self.stop_alarm)

        layout.add_widget(self.play_btn)
        layout.add_widget(self.stop_btn)

        return layout

    def on_start(self):
        """
        App 启动时，把 alarm.mp3 从 APK 资源复制到可读目录
        """
        target_path = self.get_alarm_path()

        if not os.path.exists(target_path):
            try:
                shutil.copy("alarm.mp3", target_path)
            except Exception as e:
                print("❌ 复制 alarm.mp3 失败:", e)

    def play_alarm(self, instance):
        if self.sound is None:
            self.sound = SoundLoader.load(self.get_alarm_path())
            if self.sound:
                self.sound.loop = True
            else:
                print("❌ 未能加载 alarm.mp3")
                return

        self.sound.play()

    def stop_alarm(self, instance):
        if self.sound:
            self.sound.stop()

    def get_alarm_path(self):
        """
        Android / 桌面 通用、安全路径
        """
        return os.path.join(self.user_data_dir, "alarm.mp3")


if __name__ == "__main__":
    AlarmApp().run()
