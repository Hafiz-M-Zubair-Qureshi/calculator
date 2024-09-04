import pyshorteners

def shorten_url(long_url):  

    s = pyshorteners.Shortener()                # Initialize the Shortener instance

    short_url = s.tinyurl.short(long_url)       # Use TinyURL to shorten the URL
    
    return short_url

def main():
    print("Welcome to the URL Shortener!")
    long_url = input("Enter the URL you want to shorten: ")
    
    try:
        short_url = shorten_url(long_url)
        print(f"Shortened URL: {short_url}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
