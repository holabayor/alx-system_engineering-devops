# Find apache error and fix with puppet

exec { 'correct filename':
  provider => shell,
  command  => "sed -i 's/.phpp/.php' /var/www/html/wp-settings.php",
  path     => '/bin'
}
