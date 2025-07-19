[app]
title = RewardedAdApp
package.name = rewardedadapp
package.domain = org.example

source.include_exts = py,kv,png,jpg,ttf
requirements = python3,kivy,kivymd,kivmob,jnius

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.gradle_dependencies = com.google.firebase:firebase-ads:21.4.0
android.enable_androidx = True
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

[buildozer]
log_level = 2
warn_on_root = 1
