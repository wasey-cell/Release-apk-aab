from kivymd.app import MDApp  
from kivy.lang import Builder  
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog  
from kivymd.uix.button import MDRaisedButton,MDFlatButton, MDRoundFlatButton, MDRectangleFlatButton,MDFillRoundFlatIconButton,MDRoundFlatIconButton,MDRectangleFlatIconButton 
from kivymd.uix.toolbar import MDTopAppBar 
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField  
from kivy.uix.boxlayout import BoxLayout  
from kivymd.uix.boxlayout import MDBoxLayout  
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.core.audio import SoundLoader 
from kivy.core.window import Window
from kivymd.uix.label import MDIcon
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.clock import Clock  
import random  
  
kv = '''
<MDRaisedButton>:
    font_size: 70

<MDLabel>:
    text_size: self.size
    valign: "middle"
    halign: "center"
    markup: True

<MDTextField>:
    multiline: False
    size_hint_y: None
    height: "38dp"

Screen:
    FloatLayout:

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1

            MDLabel:
                text: 'X0X Gam€'
                halign: 'center'
                font_size: '50sp'
                size_hint_y: 0.1
                theme_text_color: 'Custom'
                text_color: app.theme_cls.primary_color
                text_size: self.size
                valign: "middle"

            MDGridLayout:
                cols: 2
                size_hint_y: 0.1
                spacing :10

                MDLabel:
                    id: play1
                    text: 'score'
                    halign: 'center'
                    font_style: 'H5'
                    theme_text_color: 'Custom'
                    text_color: app.theme_cls.primary_color
                    text_size: self.size
                    valign: "middle"
                    shorten: True
                    shorten_from: "right"
                    max_lines: 2

                MDLabel:
                    id: play2
                    text: 'score'
                    halign: 'center'
                    font_style: 'H5'
                    theme_text_color: 'Custom'
                    text_color: app.theme_cls.primary_color
                    text_size: self.size
                    valign: "middle"
                    shorten: True
                    shorten_from: "right"
                    max_lines: 2
            MDGridLayout:
                id: button_grid
                cols: 5
                spacing: 1
                size_hint_y: 0.8
                pos_hint: {'top': 1}

                MDRaisedButton:
                    id: p1
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p2
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p3
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p4
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p5
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p6
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p7
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p8
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p9
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p10
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p11
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p12
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p13
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p14
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p15
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p16
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p17
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p18
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p19
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p20
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p21
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p22
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p23
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p24
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p25
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p26
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p27
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p28
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p29
                    text: ''
                    size_hint: 1, 1
                MDRaisedButton:
                    id: p30
                    text: ''
                    size_hint: 1, 1

        Widget:
            id: highlight_layer
            size_hint_y: 0.8
            size_hint_x: 1
            pos_hint: {'top': 0.9}
'''

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = [  
            "Red", "Pink", "Purple", "DeepPurple", "Indigo", "Blue", "LightBlue",  
            "Cyan", "Teal", "Green", "LightGreen", "Lime", "Yellow", "Amber",  
            "Orange", "DeepOrange", "Brown", "Gray", "BlueGray"  
        ]
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = random.choice(self.colors)   
        layout = MDBoxLayout(
            orientation="vertical",
            spacing="40dp",
        )
        title=MDTopAppBar(
            title="XoX Game",
            elevation=3
        )
        btn1 = MDRectangleFlatIconButton(
            text="Single Player",
            icon="account",
            font_style="H4",
            size_hint=(None, None),
            size=("500dp", "300dp"),
            pos_hint={"center_x":0.5,"center_y":0.7}
        )
        btn1.bind(on_press=lambda x: self.set_game(True))
        
        btn2 = MDRectangleFlatIconButton(
            text="Two player",
            icon="account-multiple",
            font_style="H4",
            size_hint=(None, None),
            size=("500dp", "300dp"),
            pos_hint={"center_x":0.5,"center_y":0.4}
        )
        btn2.bind(on_press=lambda x: self.set_game(False))
        f_lay=FloatLayout() 
        layout.add_widget(title)
        f_lay.add_widget(btn1)
        f_lay.add_widget(btn2)
        layout.add_widget(f_lay)
        self.add_widget(layout)
        
    def set_game(self,bott):
        try:
            sound=SoundLoader.load('sharp-pop-328170.mp3')
            sound.play()
        except:
            pass
        if bott:
            self.manager.get_screen('screen1').bot = bott
            self.manager.current = 'diff'
        else:
            self.manager.get_screen('screen1').bot = bott
            self.manager.current = 'screen1'

class ActApp(MDScreen):  
    def __init__(self,**kwargs):
        super().__init__(**kwargs)  
        self.theme_cls.theme_style = 'Light'  
        root = Builder.load_string(kv)
        self.add_widget(root)
        self.root_widget = root  
        for i in range(1, 31):
            btn = self.root_widget.ids[f'p{i}']
            btn.bind(on_press=self.game)
        self.highlight_layer = root.ids.highlight_layer
        self.back=False
        self.dialog = None  
        self.pp1 = ''  
        self.pp2 = ''  
        self.p1s = 0  
        self.p2s = 0  
        self.end = 0
        self.bot = False
        self.colors = [  
            "Red", "Pink", "Purple", "DeepPurple", "Indigo", "Blue", "LightBlue",  
            "Cyan", "Teal", "Green", "LightGreen", "Lime", "Yellow", "Amber",  
            "Orange", "DeepOrange", "Brown", "Gray", "BlueGray"  
        ]  
        b = root.ids  
        self.win = [  
            (b.p1, b.p2, b.p3), (b.p2, b.p3, b.p4), (b.p3, b.p4, b.p5),  
            (b.p6, b.p7, b.p8), (b.p7, b.p8, b.p9), (b.p8, b.p9, b.p10),  
            (b.p11, b.p12, b.p13), (b.p12, b.p13, b.p14), (b.p13, b.p14, b.p15),  
            (b.p16, b.p17, b.p18), (b.p17, b.p18, b.p19), (b.p18, b.p19, b.p20),  
            (b.p21, b.p22, b.p23), (b.p22, b.p23, b.p24), (b.p23, b.p24, b.p25),  
            (b.p26, b.p27, b.p28), (b.p27, b.p28, b.p29), (b.p28, b.p29, b.p30),  
            (b.p1, b.p6, b.p11), (b.p6, b.p11, b.p16), (b.p11, b.p16, b.p21), (b.p16, b.p21, b.p26),  
            (b.p2, b.p7, b.p12), (b.p7, b.p12, b.p17), (b.p12, b.p17, b.p22), (b.p17, b.p22, b.p27),  
            (b.p3, b.p8, b.p13), (b.p8, b.p13, b.p18), (b.p13, b.p18, b.p23), (b.p18, b.p23, b.p28),  
            (b.p4, b.p9, b.p14), (b.p9, b.p14, b.p19), (b.p14, b.p19, b.p24), (b.p19, b.p24, b.p29),  
            (b.p5, b.p10, b.p15), (b.p10, b.p15, b.p20), (b.p15, b.p20, b.p25), (b.p20, b.p25, b.p30),  
            (b.p1, b.p7, b.p13), (b.p2, b.p8, b.p14), (b.p3, b.p9, b.p15),  
            (b.p6, b.p12, b.p18), (b.p7, b.p13, b.p19), (b.p8, b.p14, b.p20),  
            (b.p11, b.p17, b.p23), (b.p12, b.p18, b.p24), (b.p13, b.p19, b.p25),  
            (b.p16, b.p22, b.p28), (b.p17, b.p23, b.p29), (b.p18, b.p24, b.p30),  
            (b.p3, b.p7, b.p11), (b.p4, b.p8, b.p12), (b.p5, b.p9, b.p13),  
            (b.p8, b.p12, b.p16), (b.p9, b.p13, b.p17), (b.p10, b.p14, b.p18),  
            (b.p13, b.p17, b.p21), (b.p14, b.p18, b.p22), (b.p15, b.p19, b.p23),  
            (b.p18, b.p22, b.p26), (b.p19, b.p23, b.p27), (b.p20, b.p24, b.p28),  
        ]  
        self.original_win = self.win.copy()
        self.theme_cls.primary_palette = random.choice(self.colors)  
        self.dialog_open = False  
        self.gameend=False
        self.repeat = []  
        self.turn = 'p1'  
        
    def reset(self):
        self.game_over_dialog.dismiss()
        self.highlight_layer.canvas.clear()
        try:
            sound=SoundLoader.load('sharp-pop-328170.mp3')
            sound.play()
        except:
            pass
        b=self.root_widget.ids
        for i in range(1,31):
            b[f'p{i}'].text=''
        self.dialog = None
        self.pp1 = ''
        self.pp2 = ''
        self.p1s = 0
        self.p2s = 0
        self.end = 0
        self.theme_cls.primary_palette = random.choice(self.colors)
        self.root_widget.do_layout()
        self.dialog_open = False
        self.gameend=False
        self.repeat = []
        self.turn = 'p1'
        self.win = self.original_win.copy()
        if self.back:
            self.root_widget.ids.play1.text = f'{self.pp1} [O]\n{self.p1s}'
            self.root_widget.ids.play2.text = f'{self.pp2} [X]\n{self.p2s}'
            return 
        if self.bot:
            self.pp1 = "Human"
            self.pp2 = "Bot"
            self.root_widget.ids.play1.text = f'{self.pp1} [O]\n{self.p1s}'
            self.root_widget.ids.play2.text = f'{self.pp2} [X]\n{self.p2s}'
        else:
            self.on_enter()
        
    def on_enter(self):
        if self.bot:
            self.pp1="Human"
            self.pp2="Bot"
            self.turn="p1"
            self.root_widget.ids.play1.text = f'{self.pp1} [O]\n{self.p1s}'
            self.root_widget.ids.play2.text = f'{self.pp2} [X]\n{self.p2s}'
            return    
        if not self.dialog:  
            content = BoxLayout(orientation='vertical', spacing=20, padding=10, size_hint_y=None)  
            content.bind(minimum_height=content.setter('height'))  
  
            self.player1_input = MDTextField(  
                hint_text="Player 1 Name", icon_right='account', 
                size_hint_x=1,  
                pos_hint={"center_x": 0.5}  
            )  
            self.player2_input = MDTextField(  
                hint_text="Player 2 Name",icon_right='account' , 
                size_hint_x=1,  
                pos_hint={"center_x": 0.5}  
            )  
  
            content.add_widget(self.player1_input)  
            content.add_widget(self.player2_input)  
  
            self.dialog = MDDialog(  
                title="Enter Player Names\n",padding=10, 
                type="custom",  
                content_cls=content,  
                auto_dismiss=False,  
                buttons=[  
                    MDRectangleFlatIconButton(  
                        text="Let's Start",icon='play',  
                        on_press=self.sett  
                    )  
                ]  
            )  
        self.dialog.open()  
        self.dialog_open = True  
  
    def sett(self, dt=None):
        try:
            sound=SoundLoader.load('sharp-pop-328170.mp3')
            sound.play()
        except:
            pass
        if self.player1_input.text and self.player2_input.text:
            name1 = self.player1_input.text[:8] if len(self.player1_input.text) > 8 else self.player1_input.text
            name2 = self.player2_input.text[:8] if len(self.player2_input.text) > 8 else self.player2_input.text
        
            self.pp1 = name1
            self.pp2 = name2
            if self.pp1 == self.pp2:
                self.pp2 += '°'
            self.root_widget.ids.play1.text = f'{self.pp1} [O]\n{self.p1s}'
            self.root_widget.ids.play2.text = f'{self.pp2} [X]\n{self.p2s}'
            self.dialog.dismiss()  
            self.dialog_open = False
  
            self.toss()
    def stop(self):
        self.game_over_dialog.dismiss()
        try:
            sound=SoundLoader.load('sharp-pop-328170.mp3')
            sound.play()
        except:
            pass
        self.back=True
        self.reset()
        self.back=False
        self.manager.current = 'main'
        
    def highlight_line(self, btns):
        with self.highlight_layer.canvas:
            if self.turn=='p1':
                Color(1,0,0,0.7)
            else:
                Color(0,1,0,0.7)	
            coords = []
            for btn in btns:
                coords.extend([btn.center_x, btn.center_y])
            if len(coords)>=4:
                Line(points=coords, width=4)
    	   	
    def toss(self):
        btn_heads = MDFillRoundFlatIconButton(text='Heads', icon='brain',on_press=lambda inst: self.toss_win('head'))
        btn_tails = MDFillRoundFlatIconButton(text='Tails', icon='paw',on_press=lambda inst: self.toss_win('tail'))
        self.toss_dialog = MDDialog(title='Toss',auto_dismiss=False,text=f"{self.pp1}'s call",buttons=[btn_heads, btn_tails])
        self.toss_dialog.open()
        
    def toss_win(self,choice):
        try:
            sound=SoundLoader.load('wood-surface-single-coin-payout-4-215284.mp3')
            sound.play()
        except:
            pass
        opt=['head','tail']
        select=random.choice(opt)
        if choice==select:
            self.toss_dialog.text=f'{self.pp1} win the toss\nIts {self.pp1} turn first'
            Clock.schedule_once(self.toss_dialog_dis,3)
        else:
            self.toss_dialog.text=f'{self.pp1} lost the toss\nIts {self.pp2} turn first'
            self.turn='p2'
            Clock.schedule_once(self.toss_dialog_dis,3)
            
    def toss_dialog_dis(self,dt=None):
        self.toss_dialog.dismiss()			 
        
    def game(self, instance):
        try:
            sound=SoundLoader.load('sharp-pop-328170.mp3')
            sound.play()
        except:
            pass
        self.root_widget.ids.play1.text = f'{self.pp1} [O]\n{self.p1s}'  
        self.root_widget.ids.play2.text = f'{self.pp2} [X]\n{self.p2s}'  
  
        if self.dialog_open or self.gameend:  
            return  
  
        if instance not in self.repeat:
            self.end += 1
            if self.turn == 'p1':
                instance.text = 'O'
                self.repeat.append(instance)
                self.check()
                
                if self.bot and not self.gameend:
                    self.turn = 'p2'
                    Clock.schedule_once(self.make_ai_move, 0.5)
                    
                else:
                    self.turn = 'p2'
                    
            elif not self.bot and self.turn == 'p2':
                instance.text = 'X'
                self.repeat.append(instance)
                self.check()
                self.turn = 'p1'
                
            if self.end == 30:
                Clock.schedule_once(self.game_over, 1)

    def make_ai_move(self, dt=None):
        if self.gameend:
            return
        try:
            sound=SoundLoader.load('sharp-pop-328170.mp3')
            sound.play()
        except:
            pass
        if self.dif=="easy":
            move_id = self.get_ai_move_clumsy()
        elif self.dif=="medium":
            move_id = self.get_ai_move_sneaky()
        elif self.dif=="hard":
            move_id = self.get_ai_move_terminator()  
        if move_id: 
            ai_btn = self.root_widget.ids[f'p{move_id}'] 
            ai_btn.text = "X"
            self.repeat.append(ai_btn)  
            self.end += 1  
            self.check()  
            self.turn = 'p1'
        
            if self.end == 30:
                Clock.schedule_once(self.game_over, 1)
  
    def check(self):  
        matched = []  
        for line in self.win:  
            if line[0].text and line[0].text == line[1].text == line[2].text:
                
                if line not in matched:
                    b1,b2,b3=line
                    self.highlight_line([b1,b2,b3])    
                    matched.append(line)  
  
        if matched:  
            self.win = [line for line in self.win if line not in matched]  
            points = len(matched)
            try:
                sound=SoundLoader.load('video-game-bonus-323603.mp3')
                sound.play()
            except:
                pass
            if self.turn == 'p1':  
                self.p1s += points  
            else:  
                self.p2s += points  
  
            self.root_widget.ids.play1.text = f'{self.pp1} [O]\n{self.p1s}'  
            self.root_widget.ids.play2.text = f'{self.pp2} [X]\n{self.p2s}'
            
    def game_over(self,dt=None):
        try:
            sound=SoundLoader.load('spin-complete-295086.mp3')
            sound.play()
        except:
            pass
        self.gameend = True
        if self.p1s > self.p2s:
            winner = self.pp1
        elif self.p1s < self.p2s:
            winner = self.pp2
        else:
            winner = None
        content = MDBoxLayout(orientation="vertical", spacing="10dp", padding="10dp", adaptive_height=True, size_hint_y=None, height=180)
        content.add_widget(MDIcon(
            icon="scale-balance" if winner is None else "trophy",
            font_size='64sp',
            size_hint=(None, None),
            size=("40dp", "40dp"),
            pos_hint={'center_x':0.5},
            theme_text_color="Custom",
            text_color=(1, 0.5, 0.2, 1),
        ))
        content.add_widget(
            MDLabel(
                text=("Īt's @ T!ê" if winner is None else f"{winner} Wiñ$"),
                size_hint=(None, None),pos_hint={'center_x':0.5},
                size=('350dp', '120dp'),
                halign="center",
                markup=True,
                font_style='H4',
                font_size='40dp',
                theme_text_color="Primary",
            )
        )

        content.add_widget(MDRoundFlatIconButton(text="Play Again",icon='refresh', size_hint=(None,None), size=("50dp","15dp"),pos_hint={'center_x':0.5} ,on_release=lambda x: self.reset()))
        content.add_widget(MDRoundFlatIconButton(text="Back",icon="exit-to-app",pos_hint={'center_x':0.5} ,size_hint=(None,None), size=("50dp","15dp"), on_release=lambda x: self.stop()))
        self.game_over_dialog = MDDialog(title="G∆m€ Ove®", type="custom",size_hint=(None,None),size=('300dp','400dp'), auto_dismiss=False, content_cls=content)
        self.game_over_dialog.open()
        
    def get_available_moves(self):
        available = []
        for i in range(1, 31):
            btn = self.root_widget.ids[f'p{i}']
            if btn not in self.repeat:
                available.append(i)
        return available

    def evaluate_position(self):
        score = 0
        
        for line in self.win:
            x_count = sum(1 for btn in line if btn.text == 'X')
            o_count = sum(1 for btn in line if btn.text == 'O')
            
            if x_count == 3:
                score += 100
            elif o_count == 3:
                score -= 100
            elif x_count == 2 and o_count == 0:
                score += 50
            elif o_count == 2 and x_count == 0:
                score -= 50
            elif x_count == 1 and o_count == 0:
                score += 10
            elif o_count == 1 and x_count == 0:
                score -= 10
        
        return score

    def get_ai_move_clumsy(self):
        available_moves = self.get_available_moves()
        if not available_moves:
            return None
        
        if random.random() < 0.5: 
            best_move = None
            best_score = float('-inf')

            for move in available_moves:  
                btn = self.root_widget.ids[f'p{move}']  
              
                btn.text = 'X'  
                self.repeat.append(btn)  
              
                score = self.evaluate_position()  
              
                if score > best_score:  
                    best_score = score  
                    best_move = move  
              
                btn.text = ''  
                self.repeat.remove(btn)  
          
            if best_move is None:  
                best_move = random.choice(available_moves)  
              
            return best_move  
        else:  
            return random.choice(available_moves)

    def get_ai_move_sneaky(self):
        available_moves = self.get_available_moves()
        if not available_moves:
            return None
        
        if random.random() < 0.75: 
            best_move = None
            best_score = float('-inf')

            for move in available_moves:  
                btn = self.root_widget.ids[f'p{move}']  
              
                btn.text = 'X'  
                self.repeat.append(btn)  
              
                score = self.evaluate_position()  
              
                if score > best_score:  
                    best_score = score  
                    best_move = move  
              
                btn.text = ''  
                self.repeat.remove(btn)  
          
            if best_move is None:  
                best_move = random.choice(available_moves)  
              
            return best_move  
        else:  
            return random.choice(available_moves)

    def get_ai_move_terminator(self):
        available_moves = self.get_available_moves()
        if not available_moves:
            return None
        best_move = None
        best_score = float('-inf')

        for move in available_moves:  
            btn = self.root_widget.ids[f'p{move}']  
          
            btn.text = 'X'  
            self.repeat.append(btn)  
          
            score = self.evaluate_position()  
          
            if score > best_score:  
                best_score = score  
                best_move = move  
          
            btn.text = ''  
            self.repeat.remove(btn)  
      
        if best_move is None:  
            best_move = random.choice(available_moves)  
          
        return best_move
class set_diff(MDScreen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(
            orientation="vertical",
            spacing="40dp",
        )
        title=MDTopAppBar(
            title="Choose Difficulty",
            elevation=3
        )
        btn1 = MDRectangleFlatIconButton(
            text="Easy",
            icon="emoticon-happy-outline",
            font_style="H4",
            size_hint=(None, None),
            size=("500dp", "300dp"),
            pos_hint={"center_x":0.5,"center_y":0.8}
        )
        btn1.bind(on_press=lambda x: self.setdif("easy"))
        
        btn2 = MDRectangleFlatIconButton(
            text="Medium",
            icon="emoticon-neutral-outline",
            font_style="H4",
            size_hint=(None, None),
            size=("500dp", "300dp"),
            pos_hint={"center_x":0.5,"center_y":0.6}
        )
        btn2.bind(on_press=lambda x: self.setdif("medium"))
        btn3 = MDRectangleFlatIconButton(
            text="Hard",
            icon="emoticon-angry-outline",
            font_style="H4",
            size_hint=(None, None),
            size=("500dp", "300dp"),
            pos_hint={"center_x":0.5,"center_y":0.4}
        )
        btn3.bind(on_press=lambda x: self.setdif("hard"))
        f_lay=FloatLayout() 
        layout.add_widget(title)
        f_lay.add_widget(btn1)
        f_lay.add_widget(btn2)
        f_lay.add_widget(btn3)
        layout.add_widget(f_lay)
        self.add_widget(layout)
    def setdif(self,d):
        try:
            sound=SoundLoader.load('sharp-pop-328170.mp3')
            sound.play()
        except:
            pass
        self.manager.get_screen('screen1').dif = d
        self.manager.current = 'screen1'
class MyApp(MDApp):
    def build(self):     
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ActApp(name='screen1'))
        sm.add_widget(set_diff(name="diff"))
        return sm

if __name__ == '__main__':  
    MyApp().run()