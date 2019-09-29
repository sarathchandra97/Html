import clipboard
from bs4 import BeautifulSoup

def start():
    # get the data from the clipboard 
    # Extract the  links from the html
    # create a complete html string 
    # write the data inside a temp html on the desktop 
    # Show to user that it is done 
    html_content = clipboard.paste();
    soup = BeautifulSoup(html_content,'html.parser')  
    print("Created Soup Successfully")
    all_images_url_containers = soup.find_all(["img"])
    all_anchor_tags_containers = soup.find_all(["a"])

    print(len(all_anchor_tags_containers),len(all_images_url_containers))
    if len(all_images_url_containers) != len(all_anchor_tags_containers) :
        print("Imbalance in the count of anchor tags and Image tags ")
        print("Terminating Program")
        raise Exception("Imbalance in anchor tags and Image tags")
    img_urls = []
    descriptions = []

    # Extract all the useful data 
    for img_url, description  in zip(all_images_url_containers,all_anchor_tags_containers):    
        img_url_string = img_url.get('src')
        description_string =  description.get('aria-label')
        img_urls.append(img_url_string)
        descriptions.append(description_string)
    print(len(descriptions),len(img_urls))
    clipboard_final_string = '';
    for name in descriptions : 
        print(name)
        clipboard_final_string += name + '\n';
        clipboard.copy(clipboard_final_string)
    # user 
    # input cli input is - python img2table names
    # input cli input is - python img2table all
    # input cli input is - python img2table
    # input cli input is - python img2table name 10


import argparse


def hello(args):
    print('Hello, {0}!'.format(args.name))


def names(args):
    print('The following {0} names are added to the clipboard use paste in evernote to see them'.format(args.count))


if __name__ == "__main__":
    print("hello")
    parser = argparse.ArgumentParser()

    # Getting sub parser addition handler
    subparsers = parser.add_subparsers()
    
    # Adding a parser to the main parser 
    name_parser = subparsers.add_parser('name')
    name_parser.add_argument('count')
    name_parser.set_defaults(func=names)
    
    # Adding a web parser to the main parser 
    web_parser = subparsers.add_parser('web')
    web_parser.add_argument(" ")
    web_parser.set_defaults(func=web)
    
    
    args = parser.parse_args()
    args.func(args)  # call the default function


        