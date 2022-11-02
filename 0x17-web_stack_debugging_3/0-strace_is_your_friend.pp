# Find apache error and fix with puppet

exec { 'filename':
  provider => shell,
  command  => "sed 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path     => '/bin' 
}
