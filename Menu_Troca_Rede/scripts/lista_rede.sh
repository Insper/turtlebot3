#!/bin/bash
iwlist wlan0 scan | grep -i  'asimov'| grep -Eo '[0-9]{1,3}'


