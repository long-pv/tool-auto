import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2
import numpy as np
import time
import threading
import keyboard

# ============================
#  DANH SÁCH ẢNH CẦN CLICK
# ============================
IMAGE_SEQUENCE = [
    "images/hoatdong.png",
    "images/rongthieng.png",
    "images/thamgiarongthieng.png",
    "images/morongthieng.png",
    "images/nextrongthieng1.png",
    "images/nextrongthieng2.png",
    "images/nextrongthieng3.png",
    "images/treomay.png",
    "images/ketthucrongthieng.png",
    "images/dongy.png",
]

running = False  # trạng thái chạy


# ============================
#  TÌM & CLICK ẢNH
# ============================
def find_and_click(image_path, threshold=0.8):
    try:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        template = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if template is None:
            print(f"[ERROR] Missing file: {image_path}")
            return False

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)

        for pt in zip(*loc[::-1]):
            x = pt[0] + template.shape[1] // 2
            y = pt[1] + template.shape[0] // 2
            pyautogui.moveTo(x, y, duration=0.13)
            pyautogui.click()
            return True

        return False

    except:
        return False


# ============================
#  XỬ LÝ DANH SÁCH ẢNH
# ============================
def process_images():
    for img in IMAGE_SEQUENCE:

        if not running:
            return False

        print(f"Searching: {img}")

        while running:
            found = find_and_click(img)
            if found:
                print(f"Clicked: {img}")
                time.sleep(1)
                break

            time.sleep(0.4)

        if not running:
            return False

    return True


# ============================
#  CHẠY CHÍNH
# ============================
def run_process_loop(total_runs):
    global running

    count = 0

    while running and count < total_runs:
        print(f"Run {count + 1}/{total_runs}")

        ok = process_images()
        if not ok:
            return

        count += 1
        time.sleep(1)

    # ============================
    #  KẾT THÚC → STOP
    # ============================
    running = False
    messagebox.showinfo("Completed", "Mission completed successfully!")


# ============================
#  START
# ============================
def start():
    global running

    if running:
        return

    try:
        total = int(entry.get())
        if total <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Invalid number!")
        return

    running = True

    threading.Thread(target=run_process_loop, args=(total,), daemon=True).start()

    print("Started. Press ESC to stop.")
    threading.Thread(target=esc_listener, daemon=True).start()


# ============================
#  STOP
# ============================
def stop():
    global running
    running = False
    print("Stopped manually.")


# ============================
#  ESC LISTENER
# ============================
def esc_listener():
    global running
    while running:
        if keyboard.is_pressed("esc"):
            running = False
            print("Stopped by ESC key.")
            break
        time.sleep(0.1)


# ============================
#  UI
# ============================
window = tk.Tk()
window.title("Auto Tool")
window.geometry("300x200")

tk.Label(window, text="Enter number of runs:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(window, font=("Arial", 12))
entry.pack()

tk.Button(window, text="Start", font=("Arial", 12), command=start).pack(pady=10)
tk.Button(window, text="Stop", font=("Arial", 12), command=stop).pack(pady=5)

window.mainloop()
