# Republish Velodyne /scan topic

## Motivation

The slam_toolbox subscribes to the /scan topic and expects the data of the messages in
/scan topic to be consistent. Additionally, we have customized the environment such that
slam_toolbox looks for the laser topic to have TF2 frame as 'lidar_1_link'.

To achieve these two changes, this node serves as a simple broadcaster which makes minor
changes to the existing ```/scan``` topic and publishes a new topic called ```/scan_new```

## Problem with Existing Beam Increments

- The SLAM toolbox requires the /scan topic to have certain fixed number of beams.
- These number of beams is determined by the angle (360 degrees) and the "pitch" of each beam
    called 'increment'
- As of March 2023, the velodyne driver is slightly flawed in that it says:
    - No. of beams = 897, but increment = 0.00700000021607
    - However, 2*pi/897 tells us that increment should be 0.0070124836
    - [Reference](https://github.com/SteveMacenski/slam_toolbox/issues/141)

## Solution

1. This node is just a repeater node which subscribes to /scan and publishes /scan_new
2. The /scan topic carries the message of type sensor_msgs.msg.LaserScan
3. Only two aspects of the this message are modified:
    - increment is set to 0.0070124836
    - the frame ID associated with laser scan is set to 'lidar_1_link' (original was 'velodyne')