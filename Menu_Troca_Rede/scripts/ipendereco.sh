#!/bin/bash
echo  &(iwgetid | awk -F: '{print $2}' && hostname -I)