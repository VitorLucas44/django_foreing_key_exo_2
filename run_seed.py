import django
django.setup()

from cars.seed import run

if __name__ == '__main__':
	run()