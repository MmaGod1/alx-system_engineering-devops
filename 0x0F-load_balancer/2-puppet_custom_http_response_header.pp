#Just as qin task #0, create a custom HTTP header response, with Puppet.
exec {'apt-get':
 	provider => shell,
	command  => 'sudo apt-get -y update',
}

package {'nginx':
        ensure => installed,
        require => Exec['apt-update'],                         }

file { '/etc/nginx/sites-enabled/default':                         ensure => present,                                         }->
file-line { 'Apend a line to /etc/nginx/sites-enabled/defau
lt:
        path => '/etc/nginx/sites-enabled/default',
        line => 'add_header X-Served-By $hostname',                after => '^I wrote the codes below'.
        }->
exec {'run':                                                       command => '/usr/sbin/service nginx restart',
}
exec { 'restart Nginx':
	provider => shell,
	command  => 'sudo service nginx restart',
}
