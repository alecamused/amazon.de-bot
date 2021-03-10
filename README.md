# amazon.de-bot

DISCLAIMER : You are using this bot at your own risk. I will NOT take any responsibility at all. This especially includes stuff that's ordered on your behalf, stuff that doesn't get ordered even if available, your PC catching fire, you catching the flu or corona, the weather or the world ending. I tested this on amazon.de so your results may vary. Only uncomment the "buy section" after you are confident, the script works as you expected!

This is a very basic PS5 order-bot for amazon(.de)
It was largely inspired by https://github.com/EddieXu123/Amazon-Bot, go check EddieXu123's version out, it might suit your needs better than this.

Starting the script will launch a Chrome-Window, try to log you in with the username and password from auth.py (edit those) and wait for your input to the console (to give you time to finish logging in - in case you need 2fa auth). 
Once you are logged in to amazon, go to the python-console and hit enter. Then the Script will loop following actions : 
  visit the ps5-page
  choose the ps5 product 
  click the to-the-cart-button if it's available
If the button was successfully clicked, the script will take you to your cart and try to complete the checkout process with your default settings.
To avoid any surprises - make sure your cart is empty (or at least, there are no unwanted items in it).
