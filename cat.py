import sys

BATCH_SIZE = 4096

def cat(file):
    while True:
        batch = file.read(BATCH_SIZE)
        if not batch:
            break
        sys.stdout.buffer.write(batch)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
