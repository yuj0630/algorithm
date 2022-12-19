global cnt0

cnt0 = 0
global cnt1
cnt1 = 0

def search(_path):
file_list = os.listdir(_path)
global cnt0
global cnt1
for file in file_list:
full_file_name = os.path.join(_path, file)
if os.path.isdir(full_file_name):
search(full_file_name)
else:
ext = file.split('.')[-1]
if ext == 'txt':
txt_line = open(full_file_name, 'r').readlines()
for txt in txt_line:
label = txt.split(' ')[0]
if label == '0':
cnt0 = cnt0 + 1
elif label == '1':
cnt1 = cnt1 + 1
else:
print(full_file_name)
print('err')


if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help="InputPath")
args = parser.parse_args()

path = args.path

search(path)
# global cnt0
# global cnt1

print('cap count = ', cnt0)
print('no cap count = ', cnt1)
