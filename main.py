"""
StartApp Rewarded Ads Implementation for KivyMD
This example shows how to integrate StartApp rewarded ads in a KivyMD application
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from kivy.clock import Clock
from kivy.utils import platform
import threading

# Platform-specific imports
if platform == 'android':
    from jnius import autoclass, PythonJavaClass, java_method
    from android.runnable import run_on_ui_thread
    
    # StartApp SDK classes
    StartAppSDK = autoclass('com.startapp.sdk.adsbase.StartAppSDK')
    StartAppAd = autoclass('com.startapp.sdk.adsbase.StartAppAd')
    AdEventListener = autoclass('com.startapp.sdk.adsbase.adlisteners.AdEventListener')
    VideoListener = autoclass('com.startapp.sdk.adsbase.adlisteners.VideoListener')
    AdPreferences = autoclass('com.startapp.sdk.adsbase.model.AdPreferences')
    Activity = autoclass('android.app.Activity')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')

class StartAppManager:
    """Manager class for StartApp rewarded ads"""
    
    def __init__(self, app_id):
        self.app_id = app_id
        self.rewarded_ad = None
        self.is_initialized = False
        self.reward_callback = None
        
    def initialize(self):
        """Initialize StartApp SDK"""
        if platform == 'android':
            try:
                # Get current activity
                current_activity = PythonActivity.mActivity
                
                # Initialize StartApp SDK
                StartAppSDK.init(current_activity, self.app_id, False)
                
                self.is_initialized = True
                toast("StartApp SDK initialized successfully")
                
            except Exception as e:
                toast(f"Failed to initialize StartApp SDK: {e}")
        else:
            toast("StartApp is only available on Android platform")
    
    @run_on_ui_thread
    def load_rewarded_ad(self, reward_callback=None):
        """Load rewarded video ad"""
        if not self.is_initialized or platform != 'android':
            return False
            
        try:
            self.reward_callback = reward_callback
            
            # Create rewarded video ad
            current_activity = PythonActivity.mActivity
            self.rewarded_ad = StartAppAd(current_activity)
            
            # Create ad preferences for rewarded video
            ad_preferences = AdPreferences()
            ad_preferences.setType(AdPreferences.AD_TYPE.REWARDED_VIDEO)
            
            # Create listener for ad events
            listener = StartAppAdListener(self)
            
            # Load the ad
            self.rewarded_ad.loadAd(ad_preferences, listener)
            
            toast("Loading rewarded ad...")
            return True
            
        except Exception as e:
            toast(f"Failed to load rewarded ad: {e}")
            return False
    
    @run_on_ui_thread
    def show_rewarded_ad(self):
        """Show rewarded video ad"""
        if not self.is_initialized or platform != 'android':
            return False
            
        try:
            if self.rewarded_ad and self.rewarded_ad.isReady():
                # Create video listener for reward callback
                video_listener = StartAppVideoListener(self)
                self.rewarded_ad.showAd(video_listener)
                toast("Showing rewarded ad...")
                return True
            else:
                toast("Rewarded ad is not ready")
                return False
                
        except Exception as e:
            toast(f"Failed to show rewarded ad: {e}")
            return False
    
    def is_ad_ready(self):
        """Check if rewarded ad is ready to show"""
        if not self.is_initialized or platform != 'android':
            return False
            
        try:
            return self.rewarded_ad and self.rewarded_ad.isReady()
        except:
            return False

# Android-specific listener classes
if platform == 'android':
    
    class StartAppAdListener(PythonJavaClass):
        """Ad event listener for loading ads"""
        
        __javainterfaces__ = ['com/startapp/sdk/adsbase/adlisteners/AdEventListener']
        
        def __init__(self, manager):
            super().__init__()
            self.manager = manager
        
        @java_method('(Lcom/startapp/sdk/adsbase/Ad;)V')
        def onReceiveAd(self, ad):
            toast("Rewarded ad loaded successfully")
            
        @java_method('(Lcom/startapp/sdk/adsbase/Ad;)V')
        def onFailedToReceiveAd(self, ad):
            toast("Failed to load rewarded ad")
    
    class StartAppVideoListener(PythonJavaClass):
        """Video listener for reward callbacks"""
        
        __javainterfaces__ = ['com/startapp/sdk/adsbase/adlisteners/VideoListener']
        
        def __init__(self, manager):
            super().__init__()
            self.manager = manager
        
        @java_method('(Lcom/startapp/sdk/adsbase/Ad;)V')
        def onVideoCompleted(self, ad):
            toast("Rewarded video completed - User earned reward!")
            if self.manager.reward_callback:
                # Schedule callback on main thread
                Clock.schedule_once(lambda dt: self.manager.reward_callback(), 0)

class MainScreen(MDScreen):
    """Main screen with rewarded ad functionality"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Initialize StartApp manager
        self.startapp_manager = StartAppManager("206367052")  # Replace with your App ID
        
        # Create UI
        self.setup_ui()
        
        # Initialize ads
        Clock.schedule_once(self.init_ads, 1)
    
    def setup_ui(self):
        """Setup the user interface"""
        layout = MDBoxLayout(
            orientation="vertical",
            spacing="20dp",
            adaptive_height=True,
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        # Title
        title = MDLabel(
            text="StartApp Rewarded Ads Demo",
            theme_text_color="Primary",
            size_hint_y=None,
            height="48dp",
            halign="center"
        )
        layout.add_widget(title)
        
        # Load ad button
        self.load_btn = MDRaisedButton(
            text="Load Rewarded Ad",
            size_hint=(None, None),
            size=("200dp", "40dp"),
            pos_hint={"center_x": 0.5},
            on_release=self.load_ad
        )
        layout.add_widget(self.load_btn)
        
        # Show ad button
        self.show_btn = MDRaisedButton(
            text="Show Rewarded Ad",
            size_hint=(None, None),
            size=("200dp", "40dp"),
            pos_hint={"center_x": 0.5},
            disabled=True,
            on_release=self.show_ad
        )
        layout.add_widget(self.show_btn)
        
        # Status label
        self.status_label = MDLabel(
            text="Initializing...",
            theme_text_color="Primary",
            size_hint_y=None,
            height="32dp",
            halign="center"
        )
        layout.add_widget(self.status_label)
        
        # Reward counter
        self.reward_count = 0
        self.reward_label = MDLabel(
            text=f"Rewards Earned: {self.reward_count}",
            theme_text_color="Primary",
            size_hint_y=None,
            height="32dp",
            halign="center"
        )
        layout.add_widget(self.reward_label)
        
        self.add_widget(layout)
    
    def init_ads(self, dt):
        """Initialize StartApp SDK"""
        def init_thread():
            self.startapp_manager.initialize()
            Clock.schedule_once(self.on_ads_initialized, 0)
        
        threading.Thread(target=init_thread).start()
    
    def on_ads_initialized(self, dt):
        """Called when ads are initialized"""
        if self.startapp_manager.is_initialized:
            self.status_label.text = "Ads initialized. Load an ad to start."
            self.load_btn.disabled = False
        else:
            self.status_label.text = "Failed to initialize ads."
    
    def load_ad(self, instance):
        """Load rewarded ad"""
        self.status_label.text = "Loading ad..."
        self.load_btn.disabled = True
        
        def load_thread():
            success = self.startapp_manager.load_rewarded_ad(self.on_reward_earned)
            Clock.schedule_once(lambda dt: self.on_ad_load_result(success), 0)
        
        threading.Thread(target=load_thread).start()
    
    def on_ad_load_result(self, success):
        """Called when ad loading completes"""
        if success:
            # Check periodically if ad is ready
            Clock.schedule_interval(self.check_ad_ready, 1)
        else:
            self.status_label.text = "Failed to load ad."
            self.load_btn.disabled = False
    
    def check_ad_ready(self, dt):
        """Check if ad is ready to show"""
        if self.startapp_manager.is_ad_ready():
            self.status_label.text = "Ad ready! You can show it now."
            self.show_btn.disabled = False
            self.load_btn.disabled = False
            return False  # Stop the scheduled check
        return True  # Continue checking
    
    def show_ad(self, instance):
        """Show rewarded ad"""
        self.status_label.text = "Showing ad..."
        self.show_btn.disabled = True
        
        def show_thread():
            self.startapp_manager.show_rewarded_ad()
            Clock.schedule_once(lambda dt: self.on_ad_shown(), 0)
        
        threading.Thread(target=show_thread).start()
    
    def on_ad_shown(self):
        """Called when ad is shown"""
        self.status_label.text = "Watch the video to earn a reward!"
    
    def on_reward_earned(self):
        """Called when user completes the rewarded video"""
        self.reward_count += 1
        self.reward_label.text = f"Rewards Earned: {self.reward_count}"
        self.status_label.text = "Reward earned! Load another ad?"
        self.show_btn.disabled = True
        self.load_btn.disabled = False
        
        # Here you can add your reward logic
        toast(f"User earned a reward! Total rewards: {self.reward_count}")

class StartAppRewardedAdsApp(MDApp):
    """Main application class"""
    
    def build(self):
        return MainScreen()

# Example buildozer.spec requirements for Android:
"""
Add to buildozer.spec:

[app]
requirements = python3,kivy,kivymd

[buildozer]
# Android specific
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE
android.gradle_dependencies = com.startapp:inapp-sdk:4.10.5

# Add to android.manifest.application:
android.manifest.application = <meta-data android:name="com.startapp.sdk.APPLICATION_ID" android:value="YOUR_APP_ID_HERE"/>
"""

if __name__ == '__main__':
    StartAppRewardedAdsApp().run()
