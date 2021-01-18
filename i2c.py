from smbus2 import SMBus
addr = 0x8
# bus = SMBus(1)
numb = 1
print('Enter 1 for ON and 0 for OFF')
while True:
    try:
        state = int(input('>>>>>> '))
        if state == 1:
            print('led on!')
            # bus.write_byte(addr, 0x1)
        elif state == 0:
            print('led off!')
            # bus.write_byte(addr, 0x0)
        else:
            break
    except ValueError:
        raise Exception('Invalid Format')