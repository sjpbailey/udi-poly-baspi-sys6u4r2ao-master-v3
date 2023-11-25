"""
Polyglot v3 node server
Copyright (C) 2021 Steven Bailey
MIT License
"""
import udi_interface
import sys
import time
import urllib3
import asyncio
from bascontrolns import Device, Platform

LOGGER = udi_interface.LOGGER


class basaoNode(udi_interface.Node):
    def __init__(self, polyglot, primary, address, name, ip, ip1, ip2, ip3, ip4, ip5, bc):
        super(basaoNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)
        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.bc = bc
        LOGGER.info(address)
        # IP Address Sorter
        if address == 'zone_{}'.format(0):
            self.ipaddress = ip
        elif address == 'zone_{}'.format(1):
            self.ipaddress = ip1
        elif address == 'zone_{}'.format(2):
            self.ipaddress = ip2
        elif address == 'zone_{}'.format(3):
            self.ipaddress = ip3
        elif address == 'zone_{}'.format(4):
            self.ipaddress = ip4
        elif address == 'zone_{}'.format(5):
            self.ipaddress = ip5
        else:
            pass

    def start(self):
        if self.ipaddress is not None:
            self.bc = Device(self.ipaddress)
            if self.bc.ePlatform == Platform.BASC_NONE:
                LOGGER.info('Unable to connect')
            elif self.bc.ePlatform == Platform.BASC_AO:
                LOGGER.info('connected to BASpi6U4R2AO')
            elif self.bc.ePlatform == Platform.BASC_EO:
                LOGGER.info('connected to BASedge6U4R2AO')
            else:
                pass
        if self.bc.ePlatform == Platform.BASC_AO or self.bc.ePlatform == Platform.BASC_EO:
            self.setDriver("ST", 1)
        else:
            self.setDriver("ST", 0)

            LOGGER.info('\t' + str(self.bc.uiQty) +
                        ' Universal inputs in this BASpi6u4r2ao')
            LOGGER.info('\t' + str(self.bc.biQty) +
                        ' Binary inputs in this BASpi6u4r2ao')
            LOGGER.info('\t' + str(self.bc.boQty) +
                        ' Binary outputs in this BASpi6u4r2ao')
            LOGGER.info('\t' + str(self.bc.aoQty) +
                        ' Analog outputs In This BASpi6u4r2ao')
            LOGGER.info(
                'Please open your Device Webpage to configure your input types')
            LOGGER.info('\n' "BASpi6U4R2AO IP IO Points configured")

        # Please Configure your Devices inputs by logginging into the devices GUI at http://"your ip address"
        # Set Nodes to match input and output types used

        ### Universal Inputs ###
        self.setInputDriver('GV1', 1)
        self.setInputDriver('GV2', 2)
        self.setInputDriver('GV3', 3)
        self.setInputDriver('GV4', 4)
        self.setInputDriver('GV5', 5)
        self.setInputDriver('GV6', 6)

        ### Binary/Digital Outputs ###
        self.setOutputDriver('GV7', 1)
        self.setOutputDriver('GV8', 2)
        self.setOutputDriver('GV9', 3)
        self.setOutputDriver('GV10', 4)
        self.setAOutputDriver('GV11', 5)
        self.setAOutputDriver('GV12', 6)

    ### Universal Input Conversion ###

    def setInputDriver(self, driver, input):
        input_val = self.bc.universalInput(input)
        count = 0
        if input_val is not None:
            count = int(float(input_val))
            self.setDriver(driver, count, force=True)
        else:
            pass

    ### Binary Output Conversion ###
    def setOutputDriver(self, driver, input):
        output_val = self.bc.binaryOutput(input)
        count = 0
        if output_val is not None:
            count = (output_val)
            self.setDriver(driver, count, force=True)
        else:
            pass

    ### Analot Output Conversion ###
    def setAOutputDriver(self, driver, input):
        output_val = self.bc.analogOutput(input)
        count = 0
        if output_val is not None:
            count = float(output_val)
            self.setDriver(driver, count, force=True)
        else:
            pass

    # Output 1
    def setOnOff(self, command=None):
        # Input Output Control
        self.mapping = {
            'DON1': {'output': 'GV7', 'index': (1)},
            'DON2': {'output': 'GV8', 'index': (2)},
            'DON3': {'output': 'GV9', 'index': (3)},
            'DON4': {'output': 'GV10', 'index': (4)},
        }
        index = self.mapping[command['cmd']]['index']
        control = self.mapping[command['cmd']]['output']
        output = self.mapping[command['cmd']]['output']
        self.ctrl = int(command.get('value',))
        self.setDriver(control, self.ctrl)
        if self.ctrl == 1:
            self.bc.binaryOutput(index, 1)
            self.setDriver(output, 1)
            LOGGER.info('Output On')
        elif self.ctrl == 0:
            self.bc.binaryOutput(index, 0)
            self.setDriver(output, 0)
            LOGGER.info('Output Off')

    # Analog Output 1
    def setValue5(self, command):
        output_ao1 = 'speed'
        speed = float(command.get('value'))

        def set_speed(self, command):
            speed = float(command.get('value'))
        if speed < -1 or speed > 11:
            LOGGER.error('Invalid volts selection {}'.format(speed))
        else:
            self.bc.analogOutput(1, speed)
            self.setDriver('GV11', speed)
            LOGGER.info('Analog Output 1 = ' + str(speed) + 'VDC')

    # Analog Output 2
    def setValue6(self, command=None):
        speed2 = float(command.get('value'))

        def set_speed(self, command):
            speed2 = float(command.set('value'))
        if speed2 < -1 or speed2 > 11:
            LOGGER.error('Invalid volts selection {}'.format(speed2))
        else:
            self.bc.analogOutput(2, speed2)
            self.setDriver('GV12', speed2)
            LOGGER.info('Analog Output 2 = ' + str(speed2) + 'VDC')

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            self.start()
            LOGGER.debug('shortPoll (node)')

    def query(self, command=None):
        self.start()
        LOGGER.info(self.bc)

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 2},
        {'driver': 'GV1', 'value': 1, 'uom': 56},
        {'driver': 'GV2', 'value': 1, 'uom': 56},
        {'driver': 'GV3', 'value': 1, 'uom': 56},
        {'driver': 'GV4', 'value': 1, 'uom': 56},
        {'driver': 'GV5', 'value': 1, 'uom': 56},
        {'driver': 'GV6', 'value': 1, 'uom': 56},
        {'driver': 'GV7', 'value': 1, 'uom': 80},
        {'driver': 'GV8', 'value': 1, 'uom': 80},
        {'driver': 'GV9', 'value': 1, 'uom': 80},
        {'driver': 'GV10', 'value': 1, 'uom': 80},
        {'driver': 'GV11', 'value': 0, 'uom': 72},
        {'driver': 'GV12', 'value': 0, 'uom': 72},
    ]

    id = 'zone'

    commands = {
        'DON1': setOnOff,
        'DON2': setOnOff,
        'DON3': setOnOff,
        'DON4': setOnOff,
        'SPEED2': setValue6,
        'SPEED': setValue5,
        'QUERY': query,
    }
