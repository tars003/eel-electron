import eel

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)
    return('4635413543131')

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function


options = {
	'mode': 'electron',
	# 'args': ['node_modules/electron/dist/electron.exe', '.'],
}

eel.start('hello.html', options=options, suppress_error=True)
#eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
