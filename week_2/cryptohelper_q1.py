import sys
from cryptohelper import *

k='140b41b22a29beb4061bda66b6747e14'.decode('hex')
ct='4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex')


def main(argv):
	print decrypt_block_CBC(ct[16:], 16, ct[:16], k, decrypt_block_AES)
       

if __name__ == "__main__":
        main(sys.argv)