from plyer import notification
import time

if __name__ == '__main__':
	while True:
		notification.notify(title='*** Take Rest ***', 
					message='Rest is Vital for better Mental Health',
					app_icon='C:/Users/Voldemort/Desktop/image.ico',
					timeout=5)
		time.sleep(10)

#pythonw main.py