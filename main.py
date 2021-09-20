import os

def post_save(path_dir):
    try:
        print("[*] Apache Access Log file \"POST\" method print... ")
        os.system('grep \"POST\" ' + path_dir + ' > ' + path_dir + '_post')
        print("[+] " + path_dir + "_post save!!!")
    except Exception as ex:
        print("[!] ",ex)

def sort_uniq(post_file):
    try:
        print("[*] Normalization Wait Please... ")
        os.system('sort1 -t " " -k 4 ' + post_file + ' | uniq > ' + post_file + '_sort')
        print("[+] " + post_file + "_sort save!!!")
    except Exception as ex:
        print("[!] ",ex)

def search(sort_file):
    try:
        print('[*] Field Split Wait Please... ')
        os.system('gawk -F " " "{print $1, $7}" '+ sort_file + '| cut -c 25- | uniq > ' + sort_file + '_awk')
    except Exception as ex:
        print("[!] ", ex)

def detection(search_file):
    try:
        print("test")
    except Exception as ex:
        print("[!] ", ex)

def main():
    path_dir = input("Apache Access Log File Path >>> ")
    post_save(path_dir)

    post_file = path_dir+'_post'
    sort_uniq(post_file)

    sort_file = post_file+'_sort'
    search(sort_file)

    search_file = sort_file+'_awk'
    detection(search_file)


if __name__ == '__main__':
    main()
