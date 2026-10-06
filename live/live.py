import os
import re
import shutil

class Tv:
  '''创建Tv类'''
  
  def __init__(self):
    '''初始化台名列表'''
    self.cctv_names = [f'CCTV{i}' for i in range(1,18)]

    self.sats_names = [
    "安徽卫视", "北京卫视", "重庆卫视", "东方卫视", "东南卫视",
    "广东卫视", "广西卫视", "贵州卫视", "海南卫视", "河北卫视",
    "河南卫视", "黑龙江卫视", "湖北卫视", "湖南卫视", "吉林卫视",
    "江苏卫视", "江西卫视", "辽宁卫视", "内蒙古卫视", "宁夏卫视",
    "青海卫视", "山东卫视", "山西卫视", "陕西卫视", 
    "深圳卫视", "四川卫视", "天津卫视", "新疆卫视", "云南卫视",
    "浙江卫视", "西藏卫视", "兵团卫视", "三沙卫视", "厦门卫视",
    "康巴卫视", "安多卫视", "延边卫视", "海峡卫视", "大湾区卫视",
    "农林卫视", "香港卫视"]

  
  
  def logo_filter(self):
    '''过滤台标文件'''
    os.makedirs("logo", exist_ok=True) #创建台标文件夹
    logo_list = [*self.cctv_names,*self.sats_names] #初始化台名列表

    logo_raw = input("原始台标文件夹名称: ")
    logo_raw_list = os.listdir(logo_raw) #创建原始文件夹的文件列表

    for raw in logo_raw_list: #遍历原始文件列表
      if os.path.splitext(raw)[0] in logo_list : 
        shutil.copy2(os.path.join(logo_raw, raw), os.path.join("logo", raw)) #复制台标到logo文件夹

tv = Tv()
tv.logo_filter()