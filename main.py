
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class NinjaGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # 显示区
        self.status = Label(
            text="🥷 忍者待命",
            font_size=32,
            size_hint=(1, 0.7)
        )
        self.add_widget(self.status)

        # 按钮区
        controls = BoxLayout(size_hint=(1, 0.3))

        btn_left = Button(text="⬅ 左")
        btn_attack = Button(text="⚔ 攻击")
        btn_right = Button(text="右 ➡")

        btn_left.bind(on_press=self.move_left)
        btn_attack.bind(on_press=self.attack)
        btn_right.bind(on_press=self.move_right)

        controls.add_widget(btn_left)
        controls.add_widget(btn_attack)
        controls.add_widget(btn_right)

        self.add_widget(controls)

    def move_left(self, instance):
        self.status.text = "🥷 向左移动"

    def move_right(self, instance):
        self.status.text = "🥷 向右移动"

    def attack(self, instance):
        self.status.text = "⚔ 忍者攻击！"


class NinjaApp(App):
    def build(self):
        return NinjaGame()


if __name__ == "__main__":
    NinjaApp().run()
