#!/bin/bash

# Script to serve Jekyll site locally
# This script checks for dependencies and starts the Jekyll server

echo "================================"
echo "Jekyll Site Local Server"
echo "================================"
echo ""

# Check if Ruby is installed
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby is not installed. Please install Ruby first."
    echo "   Visit: https://www.ruby-lang.org/en/documentation/installation/"
    exit 1
fi

echo "✓ Ruby version: $(ruby -v)"

# Check if Bundler is installed
if ! command -v bundle &> /dev/null; then
    echo "⚠️  Bundler not found. Installing..."
    gem install bundler
fi

echo "✓ Bundler installed"

# Install dependencies if needed
if [ ! -d "vendor/bundle" ]; then
    echo ""
    echo "📦 Installing dependencies (this may take a few minutes)..."
    bundle install
fi

echo ""
echo "🚀 Starting Jekyll server..."
echo "   Site will be available at: http://localhost:4000"
echo "   Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve --livereload


