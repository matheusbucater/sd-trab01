import asyncio
import time

async def tcp_client():
    reader, writer = await asyncio.open_connection('localhost', 8081)

    message = "Hello, World!"
    print(f"Sending message: {message}")
    writer.write(message.encode())
    await writer.drain()
    time.sleep(10)

    data = await reader.read(100)
    print(f"Received message: {data.decode()}")

    print("Closing connection")
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(tcp_client())
