# This manifest adjusts Nginx settings to handle more concurrent requests

exec { 'fix-nginx':
  command => '/usr/sbin/nginx -s reload',
  require => Service['nginx'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['fix-nginx'],
}
