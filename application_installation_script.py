import os 
import platform
import subprocess

print('Hi there')
#Dictionary mapping each operating system with its installation command
Dictionary_of_Os_with_installation_command={ 'Darwin':[ 'brew','install'], 'Linux':[ 'sudo','apt-get', 'install'],'Windows': ['choco','install']}

#Dictionary mapping each application with their package name used for installation
Dictionary_of_applications_to_install={ 'node':'nodejs', 'curl':'curl', 'wget':'wget'}


def checking_operating_system():
	"""Checking operating system script is running on"""
	
	print('Checking operating system...')
	
	#Using the plafform.system() to determine operating system of machine runing the script
	operating_system=platform.system()
	print("Gotten, {}'s environment. Let's go..".format(operating_system))

	return operating_system


def Fetching_installation_command_for_OS():
	"""Fetches installation command for system's operating sytem"""
	
	#Calling checking_operating_system to obatain system's operating system
	operating_system=checking_operating_system()
	print("Fetching installation command for {}'s system".format(operating_system))

	#Obtaining specific installation command for system's operating system
	installation_command_for_OS=Dictionary_of_Os_with_installation_command[operating_system]
	
	return installation_command_for_OS


def installing_apps(application):
	"""Installs application after checks"""
	
	#Calling the Fetching_installation_command_for_os to obtain installation command for system's operating system
	installation_command_for_OS=Fetching_installation_command_for_OS()
	
	
	#Installing node in the Darwin system has a unique sequence of command
	#Package name is 'node' instead of 'nodejs'
	#Checking for such condtion so as to install properly on Darwin system
	#Then, appending the application to be installed in to list of installation commands
	if installation_command_for_OS == Dictionary_of_Os_with_installation_command['Darwin'] and application == 'node':
		installation_command_for_OS.append(application)
	else:
		installation_command_for_OS.append(Dictionary_of_applications_to_install[application])

	
	print('Installing {} .....'.format(application))
	
	#Calling the installation command for the application
	subprocess.run(installation_command_for_OS)
	
	#Removing application from installation_command_for_OS
	del installation_command_for_OS[len(installation_command_for_OS)-1]
	
			
	

def checking_if_apps_are_already_installed():
	"""Checks if application is already installed, if not installed, installs it"""
	
	for application in Dictionary_of_applications_to_install:
		try:
			
			#Running command to check if application is on system
			subprocess.run([application, '--help'], capture_output=True)
			print('It is')
		except:
			print('{}, not on system'.format(application))

			#Calling installing_apps() function to install application
			installing_apps(application)


print('checking if system has required applications')

#Calling function to start the whole process
checking_if_apps_are_already_installed()
print('All done')




	


