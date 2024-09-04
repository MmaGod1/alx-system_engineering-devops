# 0-strace_is_your_friend.pp

file { '/path/to/missing/file':
  ensure  => 'file',
  source  => 'puppet:///modules/your_module/missing_file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
  notify => Exec['restart_apache'],
}

exec { 'restart_apache':
  command     => '/bin/systemctl restart apache2',
  refreshonly => true,
}
