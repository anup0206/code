

file1 = "1.txt"
file2 = "2.txt"
file3 = "3.txt"
try:
    with(
        open(file1,"r") as f1,
        open(file1,"r") as f2,
        open(file1,"r") as f3):
except Exception as e:
    print("Error " + e)