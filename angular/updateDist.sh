#!/bin/bash
rm -rf ../angular_display
mkdir -p ../angular_display
ng build --outputPath=../angular_display --prod  --outputHashing=all
