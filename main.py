from kivymd.app import MDApp
from kivy.lang import Builder
from kivmob import KivMob, TestIds, RewardedListenerInterface

KV = """
BoxLayout:
    orientation: "vertical"
    spacing: "20dp"
    padding: "20dp"

    MDFlatButton:
        text: "Show Rewarded Ad"
        pos_hint: {"center_x": 0.5}
        on_release: app.show_rewarded()
"""

class MyApp(MDApp, RewardedListenerInterface):
    def build(self):
        self.ads = KivMob(TestIds.APP)
        self.ads.set_rewarded_ad_listener(self)
        self.ads.new_rewarded(TestIds.REWARDED_VIDEO)
        self.ads.request_rewarded()
        return Builder.load_string(KV)

    def show_rewarded(self):
        if self.ads.is_rewarded_loaded():
            self.ads.show_rewarded()
        else:
            print("Rewarded ad not ready yet.")

    def on_rewarded(self, reward_type, reward_amount):
        print(f"User rewarded! Type: {reward_type}, Amount: {reward_amount}")

if __name__ == "__main__":
    MyApp().run()
