import os

def rename_file_names():
    file_list=os.listdir(r"D:\prank")
    print (file_list)
    saved_path=os.getcwd()
    print("current working direcorty is"+saved_path)
    os.chdir(r"D:\prank")
    remove="123456789"
    table=str.maketrans("","",remove)
    for file_name in file_list:
        print("old Name - "+file_name)
        print("New Name -"+file_name.translate(table))
        os.rename(file_name,file_name.translate(table))


rename_file_names()