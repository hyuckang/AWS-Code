from lib.list_gp2_volumes import list_gp2_volumes
from lib.modify_volumes_to_gp3 import modify_volumes_to_gp3

if __name__ == '__main__':
    aws_profile = input('Input aws profile : ')
    gp2_volume_ids = list_gp2_volumes(aws_profile)
    print(gp2_volume_ids)
    modfiy_result = modify_volumes_to_gp3(aws_profile, gp2_volume_ids)
    print(modfiy_result)