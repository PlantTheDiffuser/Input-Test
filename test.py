import struct
with open("/dev/input/event2", "rb") as f:
	while True:
		event = f.read(1)
		code = struct.unpack("c", event)
		print(f"Key Pressed: {code}")
