file { '/etc/apache2/sites-available/your_site.conf':
  ensure  => file,
  content => <<EOT
  # Remove line referencing the missing file
  EOT
  require => Package['apache2'],
}

# Restart Apache after configuration changes
service { 'apache2':
  ensure => running,
  enable => true,
  notify => Exec['restart_apache'],
}

exec { 'restart_apache':
  command => '/etc/init.d/apache2 restart',
}
