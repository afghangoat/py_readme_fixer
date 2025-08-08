import io
import os

'''
Turns:
# Good
##Bad
# C# good
##C ### bad
Into:
# Good
## Bad
# C# good
## C ### bad
'''
DEBUG_LEVEL=1

def fix_headers_in_file(file="TEST.md"):
    try:
        with open(file, mode="r", encoding="utf-8") as f:
            oldstr = f.read()
    except UnicodeDecodeError:
        try:
            with open(file, mode="r", encoding="cp1250") as f:
                oldstr = f.read()
        except UnicodeDecodeError:
            with open(file, mode="r", encoding="latin-1") as f:
                oldstr = f.read()

    newstr="";
    for line in oldstr.splitlines(keepends=True):
        if line.startswith("####") and line[4]!=' ' and line[4]!='#':
            line=line.replace("####","#### ",1)
        elif line.startswith("###") and line[3]!=' ' and line[3]!='#':
            line=line.replace("###","### ",1)
        elif line.startswith("##") and line[2]!=' ' and line[2]!='#':
            line=line.replace("##","## ",1)
        elif line.startswith("#") and line[1]!=' ' and line[1]!='#':
            line=line.replace("#","# ",1)
        newstr+=line
    if DEBUG_LEVEL>=1:
        print("Modified file: "+str(file)+"\n")
        if DEBUG_LEVEL==2:
            print("Modified data: "+str(newstr))
    
    with open(file, 'w', encoding='utf-8') as wback:
        wback.write(newstr)

def fix_headers_in_recursive_directory(root_dir):
    total_lines_by_language = {}

    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith('.md'):
                fix_headers_in_file(file_path)

if __name__ == "__main__":
    fix_headers_in_recursive_directory("./portfolio/imports/src")