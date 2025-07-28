# 1-main.py

from search_replace import search_replace

def main():
    my_list = ["hello", "world", "hello", "python"]
    search_value = "hello"
    replace_value = "hi"
    
    new_list = search_replace(my_list, search_value, replace_value)
    print("Original list:", my_list)
    print("Modified list:", new_list)

if __name__ == "__main__":
    main()