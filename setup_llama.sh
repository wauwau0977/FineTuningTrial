#!/bin/bash

# Set working directory
INSTALL_DIR="./llama.cpp"

# Clone llama.cpp if it does not exist
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Cloning llama.cpp repository..."
    git clone https://github.com/ggerganov/llama.cpp "$INSTALL_DIR"
else
    echo "llama.cpp already exists. Pulling latest updates..."
    cd "$INSTALL_DIR" && git pull
fi

# Navigate to directory
cd "$INSTALL_DIR"

# Build using CMake
echo "Building llama.cpp..."
mkdir -p build && cd build
cmake ..
cmake --build . --config Release

# Add llama.cpp bin directory to PATH in .bashrc or .zshrc
echo "Adding llama.cpp/bin to system PATH..."
if [[ $SHELL == *"zsh"* ]]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [[ $SHELL == *"bash"* ]]; then
    SHELL_CONFIG="$HOME/.bashrc"
else
    SHELL_CONFIG="$HOME/.profile"
fi

# Add export PATH line if it's not already in the shell config
if ! grep -q "export PATH=\$PATH:$INSTALL_DIR/build/bin" "$SHELL_CONFIG"; then
    echo "export PATH=\$PATH:$INSTALL_DIR/build/bin" >> "$SHELL_CONFIG"
fi

# Apply changes to current shell session
export PATH=$PATH:$INSTALL_DIR/build/bin

# Verify installation
echo "Verifying llama-quantize installation..."
if command -v llama-quantize &> /dev/null; then
    echo "✅ llama-quantize is now available!"
    llama-quantize --help
else
    echo "❌ Error: llama-quantize not found in PATH!"
fi

echo "Done! Restart your terminal or run 'source $SHELL_CONFIG' to apply changes."
