#!/bin/bash

echo "======================================"
echo "DateLink Streamlit Dating App Setup"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Create virtual environment (optional but recommended)
echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "To run the app, execute:"
echo "  streamlit run dating_app.py"
echo ""
echo "The app will be available at:"
echo "  http://localhost:8501"
echo ""
