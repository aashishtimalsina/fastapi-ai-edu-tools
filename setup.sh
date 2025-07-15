#!/bin/bash

# FastAPI Google AI Education Tools Setup Script

echo "Setting up FastAPI Google AI Education Tools..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file from example if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please edit .env file and add your Google AI Studio API key"
fi

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit the .env file and add your Google AI Studio API key"
echo "2. Run the application with: uvicorn app.main:app --reload"
echo ""
echo "Your Google AI Studio API key should be added to .env as:"
echo "GOOGLE_API_KEY=your_actual_api_key_here"
