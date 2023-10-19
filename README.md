# ws2812x LED Custom Code

This is a Python codebase for controlling WS2812x LED strips on a Raspberry Pi. 
These are just the scripts that I have created.

## Prerequisites

Before running the code, make sure you have the following prerequisites installed on your Raspberry Pi:

- Python 3.x
- [rpi_ws281x library](https://github.com/jgarff/rpi_ws281x) for controlling the WS2812x LED strip.
- [NumPy](https://numpy.org/) for array manipulation (required for some scripts).

## File Descriptions

- `brightness.py`: Control the brightness of the LED strip.
- `breathe.py`: Manual effect for Speak To Me and Breathe (in the air) from Dark Side of the Moon.
- `strip_config.py`: Configure the LED strip parameters such as the number of LEDs, GPIO pin, and brightness.
- `arg_parser.py`: A utility to parse command-line arguments for controlling the LED strip.
- `clear.py`: Turn off all LEDs and clear the LED strip.
- `music.py`: Synchronize LED animations with music or audio input.
- `general.py`: Implement various general LED animations.
- `default.py`: A sample script with basic functionality for initializing the LED strip.

## Usage

To run any of the scripts, follow these general steps:

1. Clone this repository to your Raspberry Pi:

   ```
   git clone https://github.com/Alexander-Aghili/led-programs.git
   cd ws2812x-led-python
   ```

2. Install the required dependencies as mentioned in the Prerequisites section.

3. Configure your LED strip by editing `strip_config.py` to match your setup (e.g., LED count, GPIO pin).

4. Run the desired script:

   ```
   python3 script_name.py [optional arguments]
   ```

   Replace `script_name.py` with the name of the script you want to run.

## Example Usage

### Adjust Brightness

To run default example, run:

```
python3 default.py
```

## Contributing

If you have improvements or additional features to add to this codebase, feel free to fork the repository, make your changes, and submit a pull request. We welcome contributions from the community.

## License

This codebase is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Thanks to the [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library for enabling control of WS2812x LED strips on the Raspberry Pi.

Enjoy controlling your WS2812x LED strip with these Python scripts on your Raspberry Pi!