import json
import os

uuid_list=[]

uuid_list+=json.load(open("/Users/dengken/Downloads/DetailGen3D/assets/experiment/list/generate_gpteval3d.json"))
uuid_list+=json.load(open("/Users/dengken/Downloads/DetailGen3D/assets/experiment/list/generate_GSO.json"))
uuid_list+=json.load(open("/Users/dengken/Downloads/DetailGen3D/assets/experiment/list/generate_lyg_my_val.json"))
uuid_list+=json.load(open("/Users/dengken/Downloads/DetailGen3D/assets/experiment/list/neus_GSO.json"))
uuid_list+=json.load(open("/Users/dengken/Downloads/DetailGen3D/assets/experiment/list/neus_lyg_my_val.json"))
uuid_list+=json.load(open("/Users/dengken/Downloads/DetailGen3D/assets/experiment/list/recon_GSO.json"))
uuid_list+=json.load(open("/Users/dengken/Downloads/DetailGen3D/assets/experiment/list/recon_lyg_my_val.json"))

uuid_list=list(set(uuid_list))

def get_all_file_paths(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            # 获取文件的绝对路径并添加到列表中
            file_paths.append(os.path.join(root, file))
    return file_paths

file_path_list=get_all_file_paths("/Users/dengken/Downloads/DetailGen3D/assets/input_images")

for file_path in file_path_list:
    uuid=file_path.split("/")[-1].split(".")[0]
    if uuid not in uuid_list:
        os.remove(file_path)
        print(file_path)
    # import pdb;pdb.set_trace()