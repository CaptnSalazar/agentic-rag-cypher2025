#!/bin/bash


# Run a few demo queries
python run_demo.py <<EOF
What causes server crashes?
EOF


python run_demo.py <<EOF
Explain pros and cons of using RAG for research assistance.
EOF


python run_demo.py <<EOF
Given logs showing crashes at 2AM daily, what could be the cause?
EOF