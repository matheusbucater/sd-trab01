import asyncio
import signal

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected to {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode()
        print(f"Received from {addr}: {message}")
        writer.write(data)
        await writer.drain()

    print(f"Connection closed to {addr}")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8081)
    addr = server.sockets[0].getsockname()
    print(f"Listening on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
