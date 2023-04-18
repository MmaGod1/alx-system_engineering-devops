#Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
file { '/etc/nginx/sites-enabled/default':
	ensure => present,
  }->
file-line { 'Apend a line to /etc/nginx/sites-enabled/default:
	path => '/etc/nginx/sites-enabled/default',
	line => 'add_header X-Served-By \$hostname',
	after => '^I wrote the codes below'.
}
