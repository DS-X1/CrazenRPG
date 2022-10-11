from playsound import playsound
import os
import time

def clear():
	os.system('clear')

playsound("power_up.wav")

while True:
	clear()
	print("""
	==================================================
		             
	   _,.----.                ,---.                    ,----.  .-._                       _ __        _,---.   
	 .' .' -   \  .-.,.---.  .--.'  \      ,--,----. ,-.--` , \/==/ \  .-._ .-.,.---.   .-`.' ,`.  _.='.'-,  \  
	/==/  ,  ,-' /==/  `   \ \==\-/\ \    /==/` - ./|==|-  _.-`|==|, \/ /, /==/  `   \ /==/, -   \/==.'-     /  
	|==|-   |  .|==|-, .=., |/==/-|_\ |   `--`=/. / |==|   `.-.|==|-  \|  |==|-, .=., |==| _ .=. /==/ -   .-'   
	|==|_   `-' \==|   '='  /\==\,   - \   /==/- / /==/_ ,    /|==| ,  | -|==|   '='  /==| , '=',|==|_   /_,-.  
	|==|   _  , |==|- ,   .' /==/ -   ,|  /==/- /-.|==|    .-' |==| -   _ |==|- ,   .'|==|-  '..'|==|  , \_.' ) 
	\==\.       /==|_  . ,'./==/-  /\ - \/==/, `--`\==|_  ,`-._|==|  /\ , |==|_  . ,'.|==|,  |   \==\-  ,    (  
	 `-.`.___.-'/==/  /\ ,  )==\ _.\=\.-'\==\-  -, /==/ ,     //==/, | |- /==/  /\ ,  )==/ - |    /==/ _  ,  /  
	            `--`-`--`--' `--`         `--`.-.--`--`-----`` `--`./  `--`--`-`--`--'`--`---'    `--`------'   

	=====================================================
	Copyright © 2022 KJ_GAMES. All Rights Reserved.

	                 
		""")
	menu_choice = input("""
		[1] Play Story
		[2] Load Save
		[3] About
		[4] Settings

		> """)

	if menu_choice == '1':
		playsound("atmo_select.wav")
		clear()
		men2_choice = input("""
			[1] New Game
			[2] Go Back

			> """)

		if men2_choice == '1':
			playsound("atmo_select.wav")
			clear()
			print("Welcome to your new quest! We need just a little bit of info to get you started, then you can enter your journey.")
			gender = input("""

Are you male or female?

[1] Male

> """)
			playsound("ding.wav")
			clear()
			break

		else:
			playsound("atmo_select.wav")
			pass

	elif menu_choice == '2':
		playsound("atmo_select.wav")
		clear()
		men2_choice == input("""
			[1] Go Back

			> """)

		if men2_choice == '1':
			playsound("atmo_select.wav")
			pass

	elif menu_choice == '3':
		playsound("atmo_select.wav")
		clear()
		men2_choice = input("""
			This is a hobby project by Kyle. CrazenRPG will be really cool! :)
			[1] Go Back

			> """)
		if men2_choice == '1':
			playsound("atmo_select.wav")
			pass



