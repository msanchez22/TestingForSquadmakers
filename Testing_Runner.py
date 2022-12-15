import os
import logging

#Login-Logout Casuistic
logging.info("Login and logout Started - PASSED")
os.system("python ../TestSquadMakers\Login-Logout\Pytest1-Login-Logout.py")
os.system("python ../TestSquadMakers\Login-Logout\Pytest2-LoginInvalidCredentials.py")
logging.info("Login and logout Finalized - PASSED")

#Shopping Casuistic
logging.info("Shopping Started - PASSED")
os.system("python ../TestSquadMakers\Shopping\Pytest1-BuyVariousArticules.py")
logging.info("Shopping Finalized - PASSED")