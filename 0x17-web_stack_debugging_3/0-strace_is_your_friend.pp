# 0-strace_is_your_friend.pp

file { '/etc/apache2/sites-available/your_site.conf':
  ensure  => file,
  content => <<-EOT
    # Apache virtual host configuration
    <VirtualHost *:80>
      DocumentRoot /var/www/html
      # Remove or update any lines referencing missing files or incorrect configurations
    </VirtualHost>
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
  command     => '/usr/bin/systemctl restart apache2', # Correct path to systemctl
  refreshonly => true,
}
