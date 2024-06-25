## Running

```sh
# Use pyenv (Optional)
pyenv install 3.11.9
pyenv local 3.11.9

# Set environment
poetry shell

# Install packages
poetry install

# Download livekit plugins
poetry run talk2-me download-files

# Running
poetry run talk2-me start
```

## Playground
Go to https://agents-playground.livekit.io/

## WIP
- [x] Voice talks
- [ ] Video track

**Related Issue:**

```sh
LOG: [W NNPACK.cpp:64] Could not initialize NNPACK! Reason: Unsupported hardware.
```
Still looking how to solve this issue. Currently only able to voice talks.