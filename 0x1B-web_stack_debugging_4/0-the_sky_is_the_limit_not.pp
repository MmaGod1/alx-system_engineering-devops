# This manifest adjusts Nginx settings to handle more concurrent requests

exec { 'update_ulimit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['reload_nginx'],
}

exec { 'reload_nginx':
  provider => shell,
  command  => '/usr/sbin/service nginx restart',
}
