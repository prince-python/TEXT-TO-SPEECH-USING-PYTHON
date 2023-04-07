import os

if __name__ == '__main__':
    print(' devloped by prince')
    while True:
        x=input('write what you want to pronounce and press q to exit \n')
        if x=="q":
            m="see you later bye "
            command=f"say {m}"
            os.system(command)
            break
        command=f"say {x}"
        os.system(command)