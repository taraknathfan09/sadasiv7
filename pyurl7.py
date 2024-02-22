import re
import urllib.request
import sys

def main():
    ''' Usage: url_extractor.py "http://example.com/"
        NOTICE: Intended for root urls; ie no */file or /subfolder/*
        In that case, you need to edit this file first
        './abc', '/abc' will be translated to
        'http://example.com/abc' (../ not translated)
        Return value: list
    '''
    if len(sys.argv) != 2:
        print("Usage: pyurl7.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    links_regex = re.compile('<a\s+.*href=[\'"]?([^\'" >]+)', re.IGNORECASE)
    
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.43 Safari/536.11')]
        response = opener.open(url)
        html = response.read().decode('utf-8')  # Decode the HTML content
        links = links_regex.findall(html)
        fixed_links = []

        for link in links:
            if link != "javascript:void(0);":
                full_url = re.sub(r'^\.?/{1,2}', url, link, count=1)
                fixed_links.append(full_url)

        print('\n'.join(fixed_links))
    except urllib.error.URLError:
        print('Can\'t Connect to the website')

if __name__ == '__main__':
    main()

