#!/bin/bash

# Production startup script for Similar Company Finder Crew
# This script handles the complete production deployment process

set -e  # Exit on any error

echo "🚀 Starting Similar Company Finder Crew Production Deployment"
echo "============================================================"

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found!"
    echo "📝 Please copy .env.example to .env and configure your API keys:"
    echo "   cp .env.example .env"
    echo "   # Then edit .env with your actual API keys"
    exit 1
fi

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed or not in PATH"
    echo "📝 Please install Docker to use containerized deployment"
    echo "   Or run directly with: uv run similar_company_finder_template"
    exit 1
fi

# Check if docker-compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "❌ docker-compose is not installed or not in PATH"
    echo "📝 Please install docker-compose for easy deployment"
    exit 1
fi

# Load environment variables for validation
source .env

# Validate required environment variables
echo "🔍 Validating environment configuration..."

if [ -z "$ANTHROPIC_API_KEY" ] || [ "$ANTHROPIC_API_KEY" = "your_anthropic_api_key_here" ]; then
    echo "❌ ANTHROPIC_API_KEY is not properly configured"
    echo "📝 Please set your actual Anthropic API key in .env file"
    exit 1
fi

echo "✅ Environment validation passed"

# Run tests
echo "🧪 Running production readiness tests..."
if ! python test_anthropic.py; then
    echo "❌ Tests failed! Please fix issues before deploying."
    exit 1
fi

echo "✅ All tests passed!"

# Build and start the service
echo "🏗️  Building and starting the service..."
docker-compose down --remove-orphans
docker-compose up -d --build

# Wait a moment for the service to start
sleep 5

# Check if the service is running
if docker-compose ps | grep -q "Up"; then
    echo "✅ Service is running successfully!"
    echo ""
    echo "📊 Service Status:"
    docker-compose ps
    echo ""
    echo "📝 To view logs: docker-compose logs -f similar-company-finder"
    echo "🛑 To stop: docker-compose down"
    echo ""
    echo "🎉 Production deployment completed successfully!"
else
    echo "❌ Service failed to start. Checking logs..."
    docker-compose logs
    exit 1
fi
