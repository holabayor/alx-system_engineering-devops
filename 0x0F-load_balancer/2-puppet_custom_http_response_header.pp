# Nginx configuration: header customization

exec {'Customize header':
  command  => 'sudo apt update;
  sudo apt install -y nginx;
  sudo sed -i '53 a \\tadd_header X-Served-By \$hostname;' /etc/nginx/sites-available/default;
  sudo /etc/init.d/nginx restart',
  provider => 'shell'
}
