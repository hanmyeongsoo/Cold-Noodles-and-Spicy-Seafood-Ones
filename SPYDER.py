import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
%matplotlib inline
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
import numpy as np
import os
os.chdir('/Users/myeongsoohan/Desktop')





'''
1. 용인시_소상공인_ 매출 정보 (파일명: abc.txt)
'''

## (1) Load Data ##

df = pd.read_csv('abc.txt',header=None)
df.drop([66], axis='columns', inplace=True)
df.columns = df.loc[0]
df = df.drop(0)

# Save Data (csv)
if not os.path.exists('df.csv'):
    df.to_csv('/Users/myeongsoohan/Desktop/df.csv', index=False, mode='w', encoding='utf-8-sig')
else:
    df.to_csv('/Users/myeongsoohan/Desktop/df.csv', index=False, mode='a', encoding='utf-8-sig', header=False)


# csv 데이터 불러오기
df = pd.read_csv('/Users/myeongsoohan/Desktop/df.csv')


# df 데이터 복사본 & EDA
df_copy = df
df_copy.shape
df_copy.isnull().sum()
df_copy.info()


## (2) Manipulating Data ## data set의 values의 type를 int로 바꾸기 위한 과정

# 결측 값 0으로 대체 하는 코드
df_copy['indcd_b_yn'].isnull().sum()
df_copy['indcd_a_yn'].fillna(0, inplace=True)
df_copy['indcd_b_yn'].fillna(0, inplace=True)
df_copy['indcd_c_yn'].fillna(0, inplace=True)
df_copy['indcd_d_yn'].fillna(0, inplace=True)
df_copy['indcd_e_yn'].fillna(0, inplace=True)
df_copy['indcd_f_yn'].fillna(0, inplace=True)
df_copy['indcd_g_yn'].fillna(0, inplace=True)
df_copy['indcd_h_yn'].fillna(0, inplace=True)
df_copy['indcd_i_yn'].fillna(0, inplace=True)
df_copy['indcd_j_yn'].fillna(0, inplace=True)
df_copy['indcd_k_yn'].fillna(0, inplace=True)
df_copy['indcd_l_yn'].fillna(0, inplace=True)
df_copy['indcd_m_yn'].fillna(0, inplace=True)
df_copy['indcd_n_yn'].fillna(0, inplace=True)
df_copy['indcd_o_yn'].fillna(0, inplace=True)
df_copy['indcd_p_yn'].fillna(0, inplace=True)
df_copy['indcd_q_yn'].fillna(0, inplace=True)
df_copy['indcd_r_yn'].fillna(0, inplace=True)
df_copy['indcd_s_yn'].fillna(0, inplace=True)
df_copy['indcd_t_yn'].fillna(0, inplace=True)
df_copy['indcd_u_yn'].fillna(0, inplace=True)


# 'Y'를 1로 대체 하는 코드
df_copy['indcd_a_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_c_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_f_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_g_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_h_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_i_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_j_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_k_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_l_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_m_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_n_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_p_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_q_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_r_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_s_yn'].replace(['Y'], ['1'], inplace = True)
df_copy['indcd_t_yn'].replace(['Y'], ['1'], inplace = True)


# 컬럼을 숫자형으로 바꾸는 코드 (str -> int)
df_copy['indcd_c_yn']=df_copy['indcd_c_yn'].astype(int)
df_copy['indcd_f_yn']=df_copy['indcd_f_yn'].astype(int)
df_copy['indcd_g_yn']=df_copy['indcd_g_yn'].astype(int)
df_copy['indcd_h_yn']=df_copy['indcd_h_yn'].astype(int)
df_copy['indcd_i_yn']=df_copy['indcd_i_yn'].astype(int)
df_copy['indcd_j_yn']=df_copy['indcd_j_yn'].astype(int)
df_copy['indcd_k_yn']=df_copy['indcd_k_yn'].astype(int)
df_copy['indcd_l_yn']=df_copy['indcd_l_yn'].astype(int)
df_copy['indcd_m_yn']=df_copy['indcd_m_yn'].astype(int)
df_copy['indcd_n_yn']=df_copy['indcd_n_yn'].astype(int)
df_copy['indcd_p_yn']=df_copy['indcd_p_yn'].astype(int)
df_copy['indcd_q_yn']=df_copy['indcd_q_yn'].astype(int)
df_copy['indcd_r_yn']=df_copy['indcd_r_yn'].astype(int)
df_copy['indcd_s_yn']=df_copy['indcd_s_yn'].astype(int)
df_copy['indcd_t_yn']=df_copy['indcd_t_yn'].astype(int)




'''
2. 유동인구 데이터 (파일명: floating_pop.txt)
'''
## (1) Load Data ##


df_pop = pd.read_csv('floating_pop.txt',header=None)
df_pop.columns = df_pop.loc[0]
df_pop.drop(0, inplace = True)



if not os.path.exists('df_pop.csv'):
    df_pop.to_csv('/Users/myeongsoohan/Desktop/df_pop.csv', index=False, mode='w', encoding='utf-8-sig')
else:
    df_pop.to_csv('/Users/myeongsoohan/Desktop/df_pop.csv', index=False, mode='a', encoding='utf-8-sig', header=False)

df_pop = pd.read_csv('/Users/myeongsoohan/Desktop/df_pop.csv')

# df_pop 데이터 복사본 & EDA
df_pop_copy = df_pop
df_pop_copy.shape
df_pop_copy.isnull().sum()
df_pop_copy.info()



'''
3. 용인시_상권_정보 (파일명: info.csv)
'''

## (1) Load Data ##


df_info = pd.read_csv('info.csv',header=None)
df_info.columns = df_info.loc[0]
df_info = df_info.drop(0)

# df_info 데이터 복사본 & EDA
df_info_copy = df_info
df_info_copy.shape
df_info_copy.isnull().sum()
df_info_copy.info()


'''
4. 용인시_상권_업종코드 (파일명: code.csv)
'''

## (1) Load Data ##


df_code = pd.read_csv('code.csv',header=None)
df_code.columns = df_code.loc[0]
df_code = df_code.drop(0)

# df_code 데이터 복사본 & EDA
df_code_copy = df_code
df_code_copy.shape
df_code_copy.isnull().sum()
df_code_copy.info()




