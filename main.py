from pynput.keyboard import Controller, Key
import time

def type_and_enter(text):
    keyboard = Controller()

    for char in text.strip():
        keyboard.type(char)
        time.sleep(0.1)  # Adjust the delay between characters if needed

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

if __name__ == "__main__":
    time.sleep(5)
    file_path = 'your_file.txt'  # Replace with your file path
    try:
        with open(file_path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                type_and_enter(line)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    