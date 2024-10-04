# FRA501 FUN4 6531

### Architecture

### 1. Install Environment
1. Install Ubuntu 22.04
   
    https://ubuntu.com/download/desktop

2. Install ROS2 (Humble)

   https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

3. Install python3

4. Install RoboticToolbox

   https://github.com/petercorke/robotics-toolbox-python

5. Install numpy

### 2. Setup Environmaent
1. clone Package
   ```sh
   git clone https://github.com/SUNTADTAWAN/fun4_ws.git
   ```
2. Build Package
   ```sh
   colcon build
   ```
3. Source
   ```sh
   source install/setup.bash
   ```

### 3. Run
1. run launch file
   ```sh
   ros2 launch example_description fun4.launch.py 
   ```
2. run teleop_twist_keyboard
   ```sh
   ros2 run ros2_teleop_keyboard teleop_twist_keyboard.py
   ```

### 4. How to use
1. When you want to change mode

   Mode 1 (IPK_Mode)
   ```sh
   ros2 service call /request_mode fun4_interfaces/srv/Mode "request_mode:data: 1"
   ```
   Mode 2 (Teleop_Mode)
   ```sh
   ros2 service call /request_mode fun4_interfaces/srv/Mode "request_mode:data: 2"
   ```
   Mode 3 (Auto_Mode)
   ```sh
   ros2 service call /request_mode fun4_interfaces/srv/Mode "request_mode:data: 3"
   ```


## How to Fix when Bug
4. Something else :
   
   2.1. Kill all node
   
   2.2. Restart your computer
   
   2.3. Ask chatGPT and let's fix it

   2.4. 

