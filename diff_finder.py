import os
from glob import glob


prodLoc = f"./CANodeProd"



def pyDiff():
    for singlePyFile in glob(f"{prodLoc}/*.py"):
        print(f"File Name = {singlePyFile.split('/')[-1]}")
        print(f"Command = diff -u {singlePyFile} {singlePyFile.split('/')[-1]}")
        print(f"diff -u {singlePyFile} {singlePyFile.split('/')[-1]}")
        os.system(f"diff -u {singlePyFile} {singlePyFile.split('/')[-1]}")
        print("\n#####################################################################################################\n")
        break



def shDiff():
    for singleShFile in glob(f"{prodLoc}/*.sh"):
        print(f"File Name = {singleShFile.split('/')[-1]}")
        print(f"Command = diff -u {singleShFile} {singleShFile.split('/')[-1]}")
        # print(f"diff -u {singleShFile} {singleShFile.split('/')[-1]}")
        os.system(f"diff -u {singleShFile} {singleShFile.split('/')[-1]}")
        print("\n#####################################################################################################\n")
        # break



def sqlDiff():
    for singleSqlFile in glob(f"{prodLoc}/*.sql"):
        print(f"File Name = {singleSqlFile.split('/')[-1]}")
        print(f"Command = diff -u {singleSqlFile} {singleSqlFile.split('/')[-1]}")
        # print(f"diff -u {singleSqlFile} {singleSqlFile.split('/')[-1]}")
        os.system(f"diff -u {singleSqlFile} {singleSqlFile.split('/')[-1]}")
        print("\n#####################################################################################################\n")
        # break


if __name__ == "__main__":
    pyDiff()
    # shDiff()
    # sqlDiff()
