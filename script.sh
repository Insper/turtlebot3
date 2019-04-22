#!/bin/sh
git checkout master
git pull origin master
sudo apt-get update
sudo apt autoclean

if [ -f ~/update.txt ]
then
    echo "Ja foi atualizado..."
else
    touch ~/update.txt
    echo "Atualizando o ajuste da camera..." > ~/update.txt
    date >> ~/update.txt
    sed -i '7i\    <param name="hFlip" type="int" value="1" />\' ~/catkin_ws/src/turtlebot3/turtlebot3_bringup/launch/turtlebot3_rpicamera.launch
    sed -i '8i\    <param name="vFlip" type="int" value="1" />\' ~/catkin_ws/src/turtlebot3/turtlebot3_bringup/launch/turtlebot3_rpicamera.launch 
fi

echo "finish update"
