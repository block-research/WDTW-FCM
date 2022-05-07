import sys
sys.path.append("../..")
import numpy as np
from src.utils import model
from scipy.io import loadmat
# 读取数据
path = "../../data/JapaneseVowels/JapaneseVowels.mat"
raw_data = loadmat(path)
X_test = raw_data["X_test"]
Y_test = raw_data["Y_test"]
label = Y_test.reshape(-1)
data = []
for i in range(X_test.shape[1]):
    tmp = X_test[0, i]
    data.append(tmp)
print("JapaneseVowels clustering")
# 设置参数
c = 9
m = 1.1
q = -10
dc_percent = 30.0
max_iter = 20
print("parameters:", " m:", m, " q:", q, " dc_percent", dc_percent, " max iter:", max_iter)
# 运行模型
opt = model.WDtwFcm(data=data, c=c, m=m, q=q, max_iter=max_iter, label=label, dc_percent=dc_percent)
result = opt.get_w_dtw_fcm()
print("rand index:", result)
# np.save('JapaneseVowels_ri.npy', result)
