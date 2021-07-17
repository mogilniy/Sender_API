import sys
# use 1 param -key_webex 2 param - name_room
# print to console list user/emal in ROOM
if __name__ == "__main__":
    i=len(sys.argv)
    ii=1
    while ii<i:
        print(sys.argv[ii])
        ii=ii+1