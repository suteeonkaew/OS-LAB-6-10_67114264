PAGE_SIZE = 1000

os_page_table = {
    0: 12,
    1: 45,
    2: 8,
    3: 102,
    4: 15,
    5: 33
}


def translate_address(logical_address):
    print(f"\n[MMU] Requesting Logical Address: {logical_address}")

    page_number = logical_address // PAGE_SIZE
    offset = logical_address % PAGE_SIZE

    print(f" -> Computed Page Number: {page_number}")
    print(f" -> Computed Offset: {offset}")

    if page_number not in os_page_table:
        print(
            " -> [OS ERROR] Page Fault! "
            "Data not in RAM (Segmentation Fault)."
        )
        return None

    frame_number = os_page_table[page_number]

    print(
        f" -> Page Table Lookup: "
        f"Found in Frame {frame_number}"
    )

    physical_address = (
        frame_number * PAGE_SIZE
    ) + offset

    print(
        f" -> [SUCCESS] "
        f"Translated Physical Address: "
        f"{physical_address}"
    )

    return physical_address


def main():
    print("--- AI Model Address Translation Simulator ---")

    translate_address(250)
    translate_address(3450)
    translate_address(9999)


if __name__ == "__main__":
    main()