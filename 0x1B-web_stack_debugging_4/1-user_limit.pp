# Adjust system limits to allow a higher number of open files

exec { 'update-soft-limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['update-hard-limit'],
}

exec { 'update-hard-limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
