echo Your pianobar configuration is correct if you hear music
echo Press Ctrl and C to exit
cd ~/Desktop/pandora-lightshow
sudo cp config /root/.config/pianobar/
sudo sed -ie 's/autostart/#autostart/g' /root/.config/pianobar/config
sudo pianobar
