def read_requirements(path):
	packages = {}
	with open(path) as txt:
		for line in txt:
			package, version = line.split('==')
			package = package.replace('_', '-')
			packages[package.strip()] = version.strip()
	return packages

def print_packages(header, packages):
	print "*"*100
	print "{0}: {1}".format(header, len(packages))
	for package, version in packages.iteritems():
		if isinstance(version, list):
			print '{0}=={1} > {2}'.format(package, version[0], version[1])
		else:
			print '{0}=={1}'.format(package, version)
	print "-"*100

old = read_requirements('old.txt')
news = read_requirements('new.txt')

removed = {}
equals = {}
changed = {}

for package, version in old.iteritems():
	if not package in news:
		removed[package] = version
	else:
		if version == news[package]:
			equals[package] = version
		else:
			changed[package] = [version, news[package]]
		del news[package]

print_packages('Equals', equals)
print_packages('Changed', changed)
print_packages('Removed', removed)
print_packages('New', news)
