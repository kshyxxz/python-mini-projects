from __future__ import annotations

from pathlib import Path
import sys

try:
    import qrcode
except ImportError:
    qrcode = None


def build_qr_code(data: str):
    if qrcode is None:
        raise ImportError(
            "The 'qrcode' package is required. Install it with: pip install qrcode[pil]"
        )

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def prompt_yes_no(message: str):
    while True:
        answer = input(message).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter yes or no.")


def main():
    print("QR Code Generator")
    print("Enter any text, numbers, or symbols to convert into a QR code.")

    data = input("Enter content: ").strip()
    if not data:
        print("No input provided.")
        return 1

    try:
        qr_image = build_qr_code(data)
    except ImportError as exc:
        print(exc)
        return 1

    if prompt_yes_no("Do you want to download/save it as an image? (y/n): "):
        file_name = input("Enter file name (without extension): ").strip() or "qr_code"
        output_path = Path(f"{file_name}.png")
        qr_image.save(output_path)
        print(f"QR code saved to {output_path.resolve()}")
    else:
        print("QR code was generated but not saved.")

if __name__ == "__main__":
    sys.exit(main())
