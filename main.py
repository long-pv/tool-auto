import pyautogui
import cv2
import numpy as np
import keyboard
import time
import os

# ======================
# CONFIG
# ======================
STEPS = [
    ("images/giodo.png"),
    ("images/quayve.png")
]

DELAY_AFTER_CLICK = 0.3     # thời gian sau khi click
DELAY_RETRY = 0.5           # thời gian chờ khi chưa tìm thấy ảnh (giảm tải CPU)
CONFIDENCE = 0.8            # độ chính xác nhận diện ảnh


# ======================
# FIND IMAGE
# ======================
def find_image(path):
    try:
        screen = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

        template = cv2.imread(path, cv2.IMREAD_COLOR)
        if template is None:
            print(f"[ERROR] Không load được ảnh: {path}")
            return None

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= CONFIDENCE)
        for pt in zip(*loc[::-1]):
            h, w = template.shape[:-1]
            center_x = pt[0] + w//2
            center_y = pt[1] + h//2
            return (center_x, center_y)

        return None
    except:
        return None


# ======================
# MAIN ROUTINE
# ======================
def run():
    print("Nhập số lần lặp quy trình: ")
    total_loops = int(input("> "))

    print(f"Chạy {total_loops} vòng. Nhấn ESC để dừng bất kỳ lúc nào.")
    time.sleep(2)

    loop_count = 0

    while loop_count < total_loops:
        print(f"\n=== Vòng {loop_count + 1}/{total_loops} ===")

        for img in STEPS:
            print(f"Tìm ảnh: {img} ...")

            while True:
                if keyboard.is_pressed("esc"):
                    print("Đã dừng bằng ESC.")
                    return

                pos = find_image(img)
                if pos:
                    print(f"→ Click {img} tại {pos}")
                    pyautogui.moveTo(pos[0], pos[1], 0.15)
                    pyautogui.click()
                    time.sleep(DELAY_AFTER_CLICK)
                    break  # sang bước kế tiếp
                else:
                    time.sleep(DELAY_RETRY)  # giảm tải CPU + chờ ảnh xuất hiện

        loop_count += 1
        print(f"Hoàn thành vòng {loop_count}/{total_loops}")
        time.sleep(0.5)  # nghỉ nhẹ giữa vòng lặp

    print("Đã chạy xong toàn bộ số vòng bạn yêu cầu.")


# ======================
# START
# ======================
if __name__ == "__main__":
    run()
