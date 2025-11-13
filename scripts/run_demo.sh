#!/bin/bash

# Populate sample data
curl -X GET http://localhost:8000/risk/AAPL > demo/sample_aapl_risk.json
echo "Demo data populated."