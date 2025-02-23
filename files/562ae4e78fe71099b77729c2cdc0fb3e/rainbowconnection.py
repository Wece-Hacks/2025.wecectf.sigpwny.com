import hashlib

# this is obfuscated, to get the flag you need to figure out what the input should be!
flag = ['3dba585434d47ea898deb35183ea6810', '8a5eca3d35364f0fdae6c36fb45f6573', 'c4a6a8b16cf8bb6f9d8dc0c6238697a4', '8a5eca3d35364f0fdae6c36fb45f6573', 'e84b190c570669ed7329c7a3d44fa499', 'c9b89de1bf9d79875d64669a395d5089', 'c4a6a8b16cf8bb6f9d8dc0c6238697a4', '869be90a20d7be403b28b8aa0d1ea61a', 'dd729251bf7adcc2c2208797c2eee1ea', 'c4a6a8b16cf8bb6f9d8dc0c6238697a4', 'dff80b0a054c251fdb21ac405df2709b', 'fe5a8f70e95fa3c82a1c70d119c3e516', '975408bf14467ee7b2bf9ce99bb6934c', '4c632b1e86bbd7422710428d83b563e5', '5d6a768adf61ce01c7e7c97ee34dd601', 'e84b190c570669ed7329c7a3d44fa499', '2916c4c4c429bb23bbc71afcf60cbe6c', '43906495e4893d192e3020a1d62120c5', 'af942ba93d7aedd7432f7fdb94e5ccb1', '5d6a768adf61ce01c7e7c97ee34dd601', 'dff80b0a054c251fdb21ac405df2709b', 'e84b190c570669ed7329c7a3d44fa499', '4c632b1e86bbd7422710428d83b563e5', 'fdd5cabc46522d61f4f64acd84215edc', '5d6a768adf61ce01c7e7c97ee34dd601', '3dba585434d47ea898deb35183ea6810', '786179af9d610e2fc0eb19ffd2b53ef8', 'fdd5cabc46522d61f4f64acd84215edc', '5d6a768adf61ce01c7e7c97ee34dd601', 'fdd5cabc46522d61f4f64acd84215edc', 'c4a6a8b16cf8bb6f9d8dc0c6238697a4', '045ea97a67c77a7f7d1921b297a74323', '4c632b1e86bbd7422710428d83b563e5', '43906495e4893d192e3020a1d62120c5', 'dff80b0a054c251fdb21ac405df2709b', 'af942ba93d7aedd7432f7fdb94e5ccb1', '3e1415976b26b5b3d5c867a6556f1212', 'f210fe97b053407d2023011f3e160b0e', 'f210fe97b053407d2023011f3e160b0e', 'f210fe97b053407d2023011f3e160b0e', '2039c86c9634f3f6988a656db658094f']

# function to check if the input is correct
def check_hashes(input):
    for index, letter in enumerate(input):
        if hashlib.md5((str(letter) + "a dash of salt!").encode()).hexdigest() != flag[index]:
            return False
        
    return True

input = input("Enter the flag: ")

if len(input) != len(flag):
    print("Flag length wrong!")
    exit()

if check_hashes(input):
    print("Correct flag! Submit it to the CTFd challenge for points! ")
else:
    print("Incorrect flag!")