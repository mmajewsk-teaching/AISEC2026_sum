import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client.py <ip:port>")
        sys.exit(1)

    API_URL = f"http://{sys.argv[1]}/chat"
    print(f"Streaming Chatbot @ {API_URL} (type '\\q' to quit)")
    while True:
        user_input = input("\n>>: ")
        if user_input == "\\q":
            print("Bye!")
            break

        print("\nAssistant: ", end="", flush=True)
        response = requests.post(API_URL, json={"message": user_input}, stream=True)
        for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
            if chunk:
                print(chunk, end="", flush=True)
        print()
