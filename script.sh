git checkout master
git pull
sudo apt-get update
sudo apt autoclean
echo "finish update"
rm -rf /home/pi/net/control.py
mv /home/pi/turtlebot3/Bumper/control.py /home/pi/net
rm -rf /home/pi/turtlebot3/Bumper
rm -rf /home/pi/turtlebot3/Menu_Troca_Rede
rm -rf /home/pi/turtlebot3/Suportes_Turtlebot3
