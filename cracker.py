import random
import string
import time

correct_pass = f"1257"


# ---RANDOM PASSWORD CRACKER Warning: BUT NOT PROPERLY DONE YET!!! ---
initial = time.time()
random_pass = f""
while random_pass != correct_pass:
    random_pass = ("".join(random.choices(
        string.digits, k=4)))
    print(random_pass)
    if random_pass == correct_pass:
        print(f"Password cracked! >> PASSWORD: {random_pass}")
        break
endtime = time.time()
print(f"Total Time Consuming: {(endtime - initial)}")
