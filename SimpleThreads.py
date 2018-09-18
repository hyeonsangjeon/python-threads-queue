from queue import Queue
from threading import Thread


exqueue = Queue(1)  # Size 1 queue box, let's change 1 ~ 40

def consumer():
    while True:
        print("[Consumer] I'm Ready")
        woker = exqueue.get()
        print("[Consumer] Working")
        # Some Process Real todo
        # ~~~

        exqueue.task_done()  # If task_done(), producer does not have to queue or poll consuming threads with joins.


        print('[Consumer] Processing Done')

thread = Thread(target=consumer).start()

exqueue.put(object())
print('[Producer] Put into Queue 1st')

exqueue.put(object())
print('[Producer] Put into Queue 2nd')

exqueue.join()
print('[Producer] stand by')
#As is obvious, if the queue is empty, the join method of queue does not complete until all tasks have been added to the queue call task_done.



# Expected Results
# [Producer] Put into Queue 1st
# [Consumer] I'm Ready
# [Consumer] Working
# [Consumer] Processing Done
# [Consumer] I'm Ready
# [Producer] Put into Queue 2nd
# [Consumer] Working
# [Consumer] Processing Done
# [Consumer] I'm Ready
# [Producer] stand by