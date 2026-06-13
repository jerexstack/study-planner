#!/bin/bash
clear

echo "============================================="
echo " INITIALIZING MOMO AUTOMATION SYSTEM "
echo " timestamp : $(date)"
echo " DIRECTORY : $(pwd)"
echo -e "\n Auditing deployment files states:"

ls -l momo_engine.py zapier_simulator2.py

echo -e "\n Executing transaction engine..."

py zapier_simulator2.py >> automation_history.log 2>&1
echo "=============================================="
echo "DEPLOYMENT RUN COMPLETE!"
echo " Summary saved to: automation_history.log"
echo "=============================================="
