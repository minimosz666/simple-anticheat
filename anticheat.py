import psutil
import time

# รายชื่อโปรแกรมแปลกปลอมที่ต้องการตรวจสอบ
suspicious_programs = ["malware.exe", "unknown.exe", "badprocess.exe", "Notepad.exe", "cheatengine-x86_64-SSE4-AVX2.exe"]

def log_suspicious_activity(process_name):
    with open('log.txt', 'a') as log_file:
        log_file.write(f"พบโปรแกรมแปลกปลอม: {process_name} เวลา: {time.ctime()}\n")

def check_and_terminate_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name']
            if process_name in suspicious_programs:
                print(f"แจ้งเตือน: พบโปรแกรมแปลกปลอม: {process_name}")
                log_suspicious_activity(process_name)
                proc.terminate()  # สั่งปิดโปรแกรม
                print(f"โปรแกรมแปลกปลอม {process_name} ถูกสั่งปิดและบันทึกลงใน log.txt")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    print("กำลังเริ่มค้นหาโปรแกรมแปลกปลอม")
    while True:
        check_and_terminate_processes()
        time.sleep(1)  # เช็คโปรแกรมทุกๆ 10 วินาที