import pdb

def breakpoint():
    pdb.set_trace()

def get(prompt, chars, default=None):
    while True:
        k = input(prompt)
        if k in chars:
            return k

