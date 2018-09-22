# Stanford University
# Cryptography I
# https://www.coursera.org/course/crypto

# Week 3
# Question 1

from Crypto.Hash import SHA256
import sys
import os

def hash_calculate(file_path,block_size):
    l_hash = ""
    file_size = os.path.getsize(file_path)
    last_block_size = file_size % block_size

    fo = open(file_path,'rb')

    for c in reverse_data(fo,file_size,last_block_size,block_size):
        sha256 = SHA256.new()
        sha256.update(c)
        if (l_hash):
            sha256.update(l_hash)
        l_hash = sha256.digest()
    fo.close()

    return l_hash


def reverse_data(file,file_size,l_block_size,block_size):
    count = 0
    last_position = file_size
    while last_position > 0:
        size = block_size
        if count == 0:
            size = l_block_size
        file.seek(last_position-size)
        data = file.read(block_size)
        if not data:
            break
        count += 1
        last_position  -= size
        yield data


if __name__ == '__main__':
    block_size = 1024
    file_target_path = 'file/target.mp4'
    file_check_path  = 'file/check_file.mp4'
    hash_check = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"

    check_h0 = hash_calculate(file_check_path,block_size).encode('hex')
    if str(check_h0) == hash_check:
        print('Hash h0 for check file is correct..!!!')
        target_h0 = hash_calculate(file_target_path,block_size).encode('hex')
        print('Hash h0 for target file is : ', target_h0)
    else:
        print('Something wrong check code again..!!!')

    