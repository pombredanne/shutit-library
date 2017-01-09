from shutit_module import ShutItModule

class test_kitchen(ShutItModule):


	def build(self, shutit):
		if shutit.whoiam != 'root':
			shutit.fail('must be root')
		if not shutit.command_exists('gem'):
			shutit.fail('gem must be available')
		shutit.send('gem install test-kitchen')
		shutit.send('gem install kitchen-vagrant')
		return True

def module():
		return test_kitchen(
			'git.test_kitchen.test_kitchen', 0.9549975645,
			description='',
			maintainer='',
			delivery_methods=['bash'],
			depends=['tk.shutit.vagrant.vagrant.vagrant','shutit-library.chefdk.chefdk']
		)
