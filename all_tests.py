import unittest
import  argparse

def all_cases(case_path):
    discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    return(discover)
def main():
    parser = argparse.ArgumentParser()                       #创建对象
    parser.add_argument('-d',type=str, help='case_dir')  #添加参数
    args=parser.parse_args()                                #解析参数
    case_path=args.d
    runner=unittest.TextTestRunner()
    runner.run(all_cases(case_path))

if __name__=='__main__':
    main()