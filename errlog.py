from datetime import datetime

log_file = "log.txt"

def time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def log(message):
    with open(log_file, "a") as file:
        file.write(f"[{time()}] {message}\n")
        print(f"[{time()}] {message}\n")

def read_log():
    with open(log_file, "r") as file:
        logs = file.read()
        return logs

def end_log():
    with open(log_file, "w") as file:
        file.write("")
        return "log cleared!"
