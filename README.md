# Rack Root - Aaron's Home Lab inventory project
*aka, what happens when Aaron decides to learn full stack web development and needs a project to do*

This project is, first and foremost, for my portfolio. Prior to this, I've never written a modern web app, and that is what I set out to do here. I'm not open to feature/pull requests, even though all source is available. With that out of the way, let's get into the functionality of the app.

Rack Root is a home lab inventory project that aims to track devices, networks, and some of their basic metadata. For example, what are the DHCP range(s) on the networks and when does a given device's warranty expire?

# Documentation
I gathered some notes on how I initialized this project over in [docs](docs.md).

# Features
* Track the inventory of hardware devices and networking in your home lab. For example, add your NAS and all of the hard drives inside of it.
* For your network(s)/VLANs, track the networks you're using, what they're for, and IPAM allocations. For example, my home WiFi and Kubernetes are all on the same network and have separate DHCP scopes.
* And speaking of warranty status, this can track when you bought hardware and when the warranty runs out.

# Future ideas
* Text search to the database that will look in all available fields for the search terms (mostly done!)
* IPAM visualization (easy-ish, depends on what I can use for visualization)
* Device to network visualizations
* Device to device relationships (e.g. a hard drive in a NAS)
* Create `rack-root-frontend` and `rack-root-backend` containers. I've started some notes for myself over in the [containerization](containerization.md) docs.

# Contributing
This project isn't open to contributors, sorry!