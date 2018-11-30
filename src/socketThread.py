import socket as sock
import queue
import threading

class sockThread (threading.Thread):
    def __init__(self,skt, threadID="none", name="none" ):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.s = skt
      self.queue = queue.Queue(100)
      self.fstop = False
    def run(self):
        while not self.fstop:
            if not self.queue.empty():
                msg = self.queue.get()
                self.s.send(msg.encode())
    def stop(self):
        self.fstop = True
    def post(self, m):
        self.queue.put(m)
    def get(self):
        return self.s.recv(1024)

class refuseConnection (threading.Thread):
    def __init__(self, sr):
        threading.Thread.__init__(self)
        self.s = sr
        self.fstop = False
    def run(self):
        while not self.fstop:
            self.s.listen(1)
            r , rr = self.s.accept()
            r.send("refuse".encode())
            del(rr)
            r.close()
    def stop(self):
        self.fstop = True