## Gen Vehicle Protocol Tool
adbctool is a convinent tool to let you quickly generate a nearly complete code for a new vehicle.

You only have to do is to have the dbc file (which is a communication protocol for the car, which is usually made by the vehicle integrated company), and write a less 10 lines config for generate an encode/decode

## How to get vehicle DBC
- [opendbc](https://github.com/commaai/opendbc) is a project that opens the vehicle dbc protocol.
- [openvehicles](https://docs.openvehicles.com/en/latest/index.html) is an open car project that contains any vehicle information you want to know.

## Quick start

#### Install
You can install adbctool by following cmd.
```shell
pip3 install adbctool
```

## Example
The tool's input is :

* `vehicle dbc file `: like lincoln's dbc file, put it under this folder
* `generator tool config file`: for an example, a lincoln's is lincoln_conf.yml, detail you can see the example file of lincoln_conf.yml

```shell
# adbctool -f vehicle.dbc -t vehicle_type
adbctool -f test/acura_ilx_2016_nidec.dbc -t acura_ilx
```
