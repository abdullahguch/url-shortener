# URL Shortener

This is a simple URL Shortener implemented in Python. It generates a unique short code for each URL using the MD5 hash and creates a mapping between the short code and the original URL.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener

2. Run the URL Shortener

## Usage
The URL Shortener provides a basic command-line interface with the following options:

1. Shorten URL: Enter a long URL, and the program will generate a shortened URL.
2. Expand URL: Enter a shortened URL, and the program will retrieve the original URL.
3. Quit: Exit the URL Shortener.

### Example
URL Shortener Menu:
1. Shorten URL
2. Expand URL
3. Quit

Enter your choice (1-3): 1
Enter the URL to shorten: https://www.example.com
Shortened URL: http://short.url/2fd4e1c6

URL Shortener Menu:
1. Shorten URL
2. Expand URL
3. Quit

Enter your choice (1-3): 2
Enter the shortened URL: http://short.url/2fd4e1c6
Original URL: https://www.example.com

## Contributing
This is a basic implementation, and in a real-world scenario, we need to handle edge cases, collisions, and we need to use a database to store the mapping between short codes and URLs. Feel free to contribute by opening issues or submitting pull requests. Please follow the code of conduct.

## License
This project is licensed under the MIT License - see the LICENSE file for details.