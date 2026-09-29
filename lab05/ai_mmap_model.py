import mmap
import os
import psutil


def print_memory():
    process = psutil.Process(os.getpid())

    print(
        f"[OS Monitor] Physical RAM Usage: "
        f"{process.memory_info().rss / (1024 * 1024):.2f} MB"
    )


def main():

    file_path = "fake_llm_weights.bin"

    # 1. Create a fake 50MB model weight file on the hard drive
    print("Creating a 50MB fake LLM file on Disk...")

    with open(file_path, "wb") as f:
        f.write(
            b'\x00' * (50 * 1024 * 1024)
        )

    print_memory()

    # 2. Use OS mmap to map the file to Virtual Memory
    print("\nMapping the 50MB file into Virtual Memory...")

    with open(file_path, "r+b") as f:

        mm = mmap.mmap(
            f.fileno(),
            0
        )

        print_memory()

        # 3. Trigger a Page Fault
        print(
            "\nAccessing weight at index 25,000,000 "
            "(Triggers OS Page Fault)..."
        )

        weight = mm[25000000]

        print(
            f"Weight value accessed successfully: {weight}"
        )

        mm.close()

    # Cleanup
    os.remove(file_path)


if __name__ == "__main__":
    main()