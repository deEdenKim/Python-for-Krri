import pandas as pd

file_name = 'C:/Users/codus/Desktop/test/100msec.xlsx'

excel = pd.read_excel(file_name,sheet_name='TEST_DATA')
print(excel) #엑셀 전체 출력

#엑셀 범위 추출
clm = excel.columns
readData = excel.iloc[:,range(1,41)]
replaceData = excel.iloc[:,range(42,82)]

print(clm)
print(readData)
print(replaceData)

#Dist
for i in range(len(excel)):
	for j in range(40):
		if excel.at[i, clm[j]] == "-200":
			excel.at[i+40, (clm[j])+40] = "1000";
print(replaceData)
#def reading(df, col):
#for i in df.index:
#val = df.loc[i,col]
#if val == -2000 :
