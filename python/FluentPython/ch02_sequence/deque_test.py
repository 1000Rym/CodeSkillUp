from collections import deque

deq = deque(range(10),maxlen=10)
print(f"original deq: {deq}")
deq.append(11)
print(f"appended deq: {deq}")
deq.appendleft(22)
print(f"appended left deq: {deq}")
deq.rotate(-1)
print(f"after rotate deq: {deq}")
