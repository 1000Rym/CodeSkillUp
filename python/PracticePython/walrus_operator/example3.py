# Simplify File Reader
import sys
import pathlib

for file_name in sys.argv[1:]:
    path = pathlib.Path(file_name)
    file_infos = (
        (file_contents:=path.read_text()).count("\n"),
        len(file_contents.split()),
        len(file_contents) 
    )
    print("file info: ", *file_infos, file_name)