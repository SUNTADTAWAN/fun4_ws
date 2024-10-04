# FRA501 FUN4 6531

### Architecture diagram
![image](https://github.com/user-attachments/assets/41e547a7-8a3d-4282-be49-6382faf9a942)


### Work space
![image](https://github.com/user-attachments/assets/18a85e6d-38cd-45fb-9c47-1a4b07cfadec)


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
2. Go to workspace
   ```sh
   cd fun4_ws
   ``` 
3. Remove Build install and log Before build
   ```sh
   rm -rf build/ install/ log/
   ```
4. Build Package
   ```sh
   colcon build
   ```
5. Source
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

   
#### Mode 1 
   Change mode to mode1(IPK Mode)
   ```sh
   ros2 service call /request_mode fun4_interfaces/srv/Mode "request_mode:data: 1"
   ```
   Pubblish position x,y,z (data:[x,y,z])
   ```sh
   ros2 topic pub /target_mode1 std_msgs/msg/Float64MultiArray "layout:
   dim: []
   data_offset: 0
   data: [0.0,0.0,0.0]" 
   ```

#### Mode 2
   Change mode to mode2(Teleop Mode)
   ```sh
   ros2 service call /request_mode fun4_interfaces/srv/Mode "request_mode:data: 2"
   ```

#### Mode 3 (Default mode)
   Change mode to mode3(Auto Mode)
   ```sh
   ros2 service call /request_mode fun4_interfaces/srv/Mode "request_mode:data: 3"
   ```

## How to Fix when Bug
4. Something else :
   
   2.1. Kill all node
   
   2.2. Restart your computer
   
   2.3. Ask chatGPT and let's fix it

   2.4. 

