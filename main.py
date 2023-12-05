# coded by 010mak
# give credit if you use it please

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
from random import randint
from kivy.core.text import LabelBase

# Register custom font
LabelBase.register(name='custom_font', fn_regular='fonts/custom_font.ttf')

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.basket_size = (60, 60)
        self.basket_pos = (Window.width / 2 - self.basket_size[0] / 2, 10)
        self.item_size = (50, 50)
        self.item_pos = (randint(0, Window.width - self.item_size[0]), Window.height)
        self.score = 0

        self.score_label = Label(text=f"Score: {self.score}", font_name='custom_font', size_hint=(None, None), pos=(20, Window.height - 40))
        self.add_widget(self.score_label)

        self.is_game_over = False
        self.dragging = False
        self.dincer_visible = False

        self.music = SoundLoader.load('sounds/music.mp3')
        if self.music:
            self.music.play()

        self.violin_sound = SoundLoader.load('sounds/violin.mp3')

        with self.canvas:
            self.basket = Rectangle(source='images/basket.png', pos=self.basket_pos, size=self.basket_size)
            self.item = Rectangle(source='images/Cornish.png', pos=self.item_pos, size=self.item_size)
            self.dincer = Rectangle(source='images/Dincer.png', pos=(0, 0), size=(Window.width, Window.height))
            self.dincer.opacity = 0  # Initially invisible

        Clock.schedule_interval(self.update, 1 / 60.)

    def on_touch_down(self, touch):
        if self.basket.collide_point(*touch.pos):
            self.dragging = True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.dragging:
            self.basket.pos = (touch.x - self.basket_size[0] / 2, self.basket.pos[1])
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        self.dragging = False
        return super().on_touch_up(touch)

    def update(self, dt):
        if self.is_game_over:
            return

        self.item.pos = (self.item.pos[0], self.item.pos[1] - 2)

        if self.item.pos[1] < 0:
            self.item.pos = (randint(0, Window.width - self.item_size[0]), Window.height)
            self.score += 1
            self.score_label.text = f"Score: {self.score}"
            if self.score % 10 == 0 and self.violin_sound:
                self.violin_sound.play()
                self.dincer_visible = True
                self.dincer.opacity = 1
                Clock.schedule_once(self.hide_dincer, 3)

        if self.basket.collide_widget(self.item):
            self.is_game_over = True
            self.display_game_over()

    def hide_dincer(self, dt):
        self.dincer_visible = False
        self.dincer.opacity = 0

    def display_game_over(self):
        self.clear_widgets()
        game_over_label = Label(text="Game Over! Tap to restart.", font_name='custom_font', size_hint=(None, None), pos=(Window.width / 2, Window.height / 2))
        self.add_widget(game_over_label)

    def on_touch_down(self, touch):
        if self.is_game_over:
            self.reset_game()
        else:
            super().on_touch_down(touch)

    def reset_game(self):
        self.clear_widgets()
        self.add_widget(self.score_label)
        self.score = 0
        self.score_label.text = f"Score: {self.score}"
        self.is_game_over = False
        self.basket_pos = (Window.width / 2 - self.basket_size[0] / 2, 10)
        self.item_pos = (randint(0, Window.width - self.item_size[0]), Window.height)
        self.dincer_visible = False
        self.dincer.opacity = 0
        if self.music:
            self.music.play()

class GameApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    GameApp().run()