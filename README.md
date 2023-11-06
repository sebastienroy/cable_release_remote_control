# cable_release_remote_control

This project aim is to create a device that can add remote control capability to a camera cable release

## Introduction

*A description of cable release can be find here : https://lensnotes.com/photography/cable-release/*

![Cable Release image](/images/Nikon-AR-3-Cable-release.jpg)

A cable release, also known as a threaded cable release, is a device used to actuate the shutter of a camera without touching the shutter button. It consists of a flexible wire moving within a sheath, with a threaded connector on one end, an a plunger on the other.  
The cable release is a purely mechanical device, as opposed to an electronic remote shutter release.  


Self-timers have been produced in mid 1900's and can be used to actuate a cable release. They can be used to add self-timer and long time exposure (1-10s) functions to a mechanical camera.  
![Ferdax self-timer](/images/ferdax.jpg)  

When cameras mechanisms became electronic, and then fully digital, remote triggers have been created, adding a lot of new remote functions to trigger the camera. However, these triggers are usually connected to the camera through a proprietary electrical connector.  
These electronic remote controls cannot be used with mechanical release threaded connector.
![Electronic Remote Shutter Release](images/camera-remotes-lineup.jpg)

## Goal of the project

> **The goal of this project is to design and build a device that can add a remote control capability to a mechanical camera.**

## Device Requirements and Architecture

As an engineer, it is a good habit to begin a project by defining all the requirements the resulting system shall satisfy.  
Because all the requirements have not the same weight (some of them are mandatory while some others are only wishes), it is also a good habit to give them a priority.  
During the design phase, in order to avoid the "tunnel effect" (a lot of work is done but there is still nothing usable), it is also a good habit to split requirements into several groups, each of the groups is an increment that defines a new release of the product.  
The first group defines what is usually called the Minimum Valuable Product (MVP). The MVP is the smallest product definition that leads to something that brings value to the user.  

The requirements can be categorized into two main families:  

+ functional requirements (which functions are brought to the user)  
+ non functional requirements (which qualities are fullfilled by the system: environmental impact, compliance with regulation laws, cost, weigth, ...).  

At the same time the requirements are written, an architecture has to be defined.  
Architecture definition is usually split into different steps.  
First, the functional architecture defines the different logical functions of the system.  
Each functional requirements of the system shall be allocated to one or several of these logical functions.  

Then, a physical architecture is designed, which target is to able to match to all the functional and non functional requirements


A good architecture leads to a good balance between the costs (components cost, but also development time and build time) and the added value for the customer.
The architecture design shall be able to meat requirements of the current definition of the product but shall also be able to support new requirements.  

Once the architecture has been defined, a cost (design, build) can be estimated for each requirement.  
The balance between estimated value and estimated cost can then be used to decide in which requirement group (which release) will be added a given requirement. In the case of a very bad balance, the decision can be made to reject the requirement.

## Functional architecture

![Functional Architecture](/images/functional_design.svg)  
*Functional Architecture definition*

## Functional Requirements

+ The device shall be able to trigger a cable release
+ The device trigger force shall be adaptable into a range from Xmin Newtons to Xmax Newtons
+ The device trigger course shall be adaptable from Ymin mm to Ymax mm
+ The device shall be used as a self timer, with control of delay and duration
+ The device shall be able to use the B mode of the camera
+ The device shall be able to use the T mode of the camera
+ The device shall allow the user to open the shutter of the camera during a user predefined amount of time
+ The device shall allow the user to open and then close the shutter of the camera during an undefined amount of time
+ The device shall be remote controlled by the user
+ The device shall be able to perform a half-press a given amount of time, before the complete press, in order to allow the camera to perform auto-focus and other parameter adaptation before releasing the shutter

## Non functional requirements

+ The device shall be complient with European Restriction of Hazardous Substances (RoHS) directive
+ The device shall be complient with European Electromagnetic Compatibility Directive
+ Durability: the device shall not contain component with limited lifespan.
+ Integrity : by construction, the device shall not be able to deteriorate the camera by applying an excessive force on its release. 
+ The device shall be able to be powered using (rechargeable) batteries
+ The device shall be able to be powered using a power bank
+ Maintenability : The device design shall allow users to upload firmware updates
+ The device end user price, including components and workforce costs, shall not exceed ZZ euros.




