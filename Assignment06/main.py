class Logger:
    def __init__(self):
        print("Logger created. Ready to log!")

    def __del__(self):
        print("Logger destroyed. Shutting down...") 

log = Logger()

del log
