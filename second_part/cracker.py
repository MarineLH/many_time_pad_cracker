import sys
import base64


def xor_two_str(a, b):
    return "".join(["%x" % (int(x, 16) ^ int(y, 16)) for (x, y) in zip(a, b)])


def decrypt_file(filename, guess, select_line):
    decoded = []
    number_lines = 0

    with open(filename, 'r') as file:
        for line in file.read().split("\n"):
            decoded.append(base64.b64decode(line).encode('hex'))
            number_lines += 1

    for i in range(0, number_lines-1):
        xor = xor_two_str(decoded[int(select_line)], decoded[i])
        print(xor_two_str(xor, guess).decode('hex')[:len(guess)])


def main(argv):
    if len(argv) < 4:
        sys.stderr.write(
            "Usage : %s <filename> <guess> <select_line> \n" % (argv[0]))
        return 1

    decrypt_file(argv[1], argv[2].encode('hex'), argv[3])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
