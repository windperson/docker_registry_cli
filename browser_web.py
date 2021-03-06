import subprocess, sys

from flask import Flask
app = Flask(__name__, static_folder='css')

registry_endpoint = ""
ssl = ""

@app.route('/registry/search')
def get_docker_registry():

    p = subprocess.Popen(['python', 'browser.py', registry_endpoint, 'html', 'all', ssl], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out


@app.route('/css/<path:path>')
def send_js(path):
	print path
	return send_from_directory(app.static_folder, path)

def usage():
	 return "Usage: browser_web.py <registry_endpoint> <ssl>"


if __name__ == '__main__':
	commandlineargs = sys.argv[1:]
	len_sys_argv = len(commandlineargs)

	if len_sys_argv < 2:
		print usage()
	else:
		registry_endpoint = commandlineargs[0]
		ssl = commandlineargs[1]
		print registry_endpoint, ssl
		app.run(host='localhost', port=9001)
