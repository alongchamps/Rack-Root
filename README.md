# Rack-Root - the home lab inventory project
This is my first modern web app (ever) and its purpose is to help me learn to write a web app from scratch! This will be for tracking the inventory of a home lab.

This web app is a chance for me to write some modern web app code and also demonstrate how I pick up new technologies. I'm writing this mostly for myself and my own portfolio.

I'm keeping the scope small for now, at least to make this manageable.

# Front end
Web - nginx

Formatting - help from Bootstrap

# Back end
Python - I'm going with Flask for this project

Database - to be detemrined, probably something schemaless

# Features
* Track the inventory and relationships of hardware/VMs in your home lab. Everything from racks to servers to NAS devices to the hard drives inside are intended to be in scope. Of course, that's not a complete list of object types.
* For your network(s)/VLANs, track the networks you're using, what they're for, and IPAM allocations. For example, my home network only has 50 IPs in the DHCP scope and all the other IPs are available for static assignment.
* Full text search of any field in order to locate resources quickly. Get an alert for a hard drive with serial `B4T9X2H8J6` having problems? Find out where it is quickly and identify your warranty status.
* Speaking of warranty tracking - when did you buy this device? What kind of warranty did it come with? When does that expire? And so on. Rack Root will help you centraize this in one spot.

# Future ideas
*This is pretty much a wish list*
* Add custom object types (easy, needs flexible code)
* IPAM visualization (easy-ish, depends on what I can use for visualization)
* Rack visualization (easy-ish, same as IPAM viz)
* Network device relationship mapping

# Out of scope
*These things are not considered to be in scope because they aren't worth going after for me in this project.*
* External database support - While I am using a separate database container for this deployment, and everything is containerized, I am writing it to work with just that database.
* Automatic device discovery/mapping - It would be really cool to just point at an IP with credentials and slurp up all the data, but that seems too complicated for this project.
