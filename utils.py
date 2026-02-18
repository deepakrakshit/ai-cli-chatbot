"""
Utility Functions

This module contains helper functions that enhance the user interface and 
experience of the CLI Chatbot.

Functions:
    type_effect(text, delay): Simulates a typewriter effect for text output.

AUTHOR: Deepak Rakhit
GITHUB: https://github.com/deepakrakshit
"""

import time
import sys

def type_effect(text: str, delay: float = 0.02) -> None:
    """
    Prints text to the console one character at a time to simulate a 
    typewriter or real-time AI generation effect.

    Args:
        text (str): The string to be printed.
        delay (float, optional): The time in seconds to wait between 
                                 printing each character. Defaults to 0.02.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end