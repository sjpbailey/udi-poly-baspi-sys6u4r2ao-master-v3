# Universal Devices BASpi-SYS6U4R2AO NodeServer

## Based on the Contemporary Controls BASpi-AO2 Controller

![Irrigation Single Poly](/Users/stevenbailey/UDI Development PG3/Nodeservers/udi-poly-baspi-sys6u4r2ao-master-v3/Images/Shot_1.png)

* The controller uses pull down commands for the outputs. Here is a program example within the ISY, there is no need for an Else statement on and off happen for the duration time in Then:

![Irrigation ISY Program](/Users/stevenbailey/UDI Development PG3/Nodeservers/udi-poly-baspi-sys6u4r2ao-master-v3/Images/shot_2.png)

* It would be great if the Else statement also included an additional If statement. 
This is also a very diverse platform that is evolving.

## BASpi-AO2 DIY BacNet Control Device by Contemporary Controls

* Main
[Contemporary Controls BASpi DIY](https://www.ccontrols.com/basautomation/baspi.php)
* BASpi 6U6R Controller
[Contemporary Controls BASpi 6U6R](https://www.ccontrols.com/pdf/ds/BASPI-datasheet.pdf)
* BASpi 6U6R Installation
[Contemporary Controls BASpi 6U6R Install](https://www.ccontrols.com/pdf/BASpi-hardware-install-guide.pdf)
* BASpi-AO2 Controller
[Contemporary Controls BASpi-AO2](https://www.ccontrols.com/pdf/ds/BASPI-AO2-datasheet.pdf)
* BASpi-AO2 Installation
[Contemporary Controls BASpi-AO2 Install](https://www.ccontrols.com/pdf/TD180600.pdf)
* BASpi Controller Configuration
[Contemporary Controls BASpi Configuration Quick Start](https://www.ccontrols.com/pdf/is/BASPI-QSGuide.pdf)

### Details

* The purpose of this Nodeserver is for custom control for general Home automation for up to four 4; Binary Outputs, six 6; Universal Inputs and two 2; Analog Outputs.

* It utilizing the Contemporary Controls BASpi-AO2 control Module.
Please see links above for information & configuration of this Device.

* This will be included in a Network series for custom home control for Irrigation, Pool, six 6 car garage door controller, HVAC, VVT, Boiler, Well along with any custom control you create utilizing the bascontrol_ns module.

#### Future

* Need to somehow add pulldown for the Universal Inputs. The universal inputs have a large list of configurable UOM's of their own.
Please see configuration quick start link above. On page two, 2 it shows the GUI for the device there you can pick on each universal input to configure its type, a seperate UOM. Also see the viedo below.

![Future Adds](/Users/stevenbailey/UDI Development PG3/Nodeservers/udi-poly-baspi-sys6u4r2ao-master-v3/Images/shot_3.png)

[Universal Input Configuration Viedo](https://www.youtube.com/watch?v=hTd1mR7npP4)

* Python 3.7.7

* Supported Nodes
  * Six 6 Universal Inputs
  * Six 4 Binary Outputs
  * Two 2 Analog Outputs
  
##### Configuration

###### Defaults

* Default Short Poll:  Every 60 seconds
* Default Long Poll: Every 4 minutes (heartbeat)
* requirments: polyinterface, bascontrolns, requests

###### User Provided

* Enter your IP address for your BASpi-AO2 controller,
* key = baspiao1_ip Value = Enter Your BASpi IP Address.
* Save and restart the NodeServer
* sjb/gtb
