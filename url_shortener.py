import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        # Generate a unique short code using MD5 hash
        short_code = hashlib.md5(original_url.encode()).hexdigest()[:8]

        # Save the mapping between short code and original URL
        self.url_mapping[short_code] = original_url

        # Return the shortened URL
        return f"http://short.url/{short_code}"

    def expand_url(self, short_url):
        # Extract the short code from the URL
        short_code = short_url.split("/")[-1]

        # Look up the original URL using the short code
        original_url = self.url_mapping.get(short_code)

        if original_url:
            return original_url
        else:
            return "URL not found"

def main():
    shortener = URLShortener()

    while True:
        print("URL Shortener Menu:")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            original_url = input("Enter the URL to shorten: ")
            shortened_url = shortener.shorten_url(original_url)
            print(f"Shortened URL: {shortened_url}")
        elif choice == "2":
            short_url = input("Enter the shortened URL: ")
            original_url = shortener.expand_url(short_url)
            print(f"Original URL: {original_url}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
