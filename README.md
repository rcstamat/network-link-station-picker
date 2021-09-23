# network-link-station-picker
#### Algorithm for selecting the best signal tower in a network for a set of devices ####

We are given a network of signal towers (link stations) and a list of devices that need to connect to the network. Based on their x,y position and the stations power we must connect the devices to the optimal station.

The optimal station is the one that satisfies the maximum power:  
power = (station reach - device's distance from station) ^2, only if device is in reach otherwise  
power = 0

station structure is defined as a list of x pos, y pos, r reach  
devices strucutre is defined as a list if x pos, y pos

For the devices given as input the result should be:
"Best link station for point x,y is x,y with power z", where z can be any of the optimal solutions
or  
"No link station within reach for point x,y", if power is 0

#### Example ####
Input:  
- stations [[0,0,10],[20,20,5],[10,0,12]]  
- devices [[0,0],[100,100],[15,10],[18,18]]

Output:  

Best link station for point 0,0 is 0,0 with power 100  
No link station within reach for point 100,100  
Best link station for point 15,10 is 10,0 with power 1  
Best link station for point 18,18 is 20,20 with power 9  


#### Solution ####

Assumption: All data values including coordinates, distance, reach and power are positive integer numbers 

- Solution 1
  For each station and each device calculates the power and selects the the maximum value.
  Considering s stations and d devices, complexity is O(s*d)
  
- Solution 2
  Create a map of cells that stores the maximum power in that particular point for all the stations.
  Once that is build the devices are able to retrieve the optimal station in O(1) time.
  Also, a cache can be used to prevent recalculating the map if the status of the stations hasn't changed.
  
  Considering that the point farthest to the origin has x,y coordinates then the map size would be O(x*y) 
  in space and would require O(x*y*s) time to calculate.
  It's better than solution 1 if the stations don't change often in comparisson to the devices.
  
  For the example above this would be how the map would look like:

![power_map](https://user-images.githubusercontent.com/48902923/129020202-ad341608-7717-47f7-b5c2-375605032613.png)
![reach_map](https://user-images.githubusercontent.com/48902923/129020197-346b3476-8a5b-4fe9-9c1d-fed849e0ab0e.png)
![station_owner_map](https://user-images.githubusercontent.com/48902923/129020204-2acd61c3-f09a-463e-bc1a-83dcad5366e8.png)


#### Run ####

You can run the script using:

> python3 station_picker.py input_file [--model] [--caching] [--invalidate_cache]
where:
  - input_file is json containing the devices and stations
  - model is the solution method, either NetworkModel1 or NetworkModel2 
  - caching is the ability to use cache
  - invalidate-cache is to reset the cache

For running the example above:
> python3 station_picker.py input_1_normal.json --model=NetworkModel2 --caching=True --invalidate_cache=False
