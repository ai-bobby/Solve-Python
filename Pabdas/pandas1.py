import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce



def red_csv_file(data_frame):
    return pd.read_csv(data_frame)





student_Quiz1_csv= r'Pabdas\student_Quiz1.csv'
student_Quiz2_csv = r'Pabdas\student_Quiz2.csv'
student_Project_csv = r'Pabdas\student_Project.csv'
student_Final_Exam_csv = r'Pabdas\student_Final_Exam.csv'
student_Information_csv = r'Pabdas\student_Information.csv'






df_student_Quiz_1 = red_csv_file(student_Quiz1_csv)
df_student_Quiz_2 = red_csv_file(student_Quiz2_csv)
df_student_Project = red_csv_file(student_Project_csv)
df_student_Final_Exam = red_csv_file(student_Final_Exam_csv)
df_student_Information = red_csv_file(student_Information_csv)






def data_clean_change_value(df:object, change_value:str) -> object:
    for index in df.index:
        if df.loc[index,change_value] == 'A':
            df.loc[index,change_value] = 10
        elif df.loc[index,change_value] == 'B':
            df.loc[index,change_value] = 8
        elif df.loc[index,change_value] == 'C':
            df.loc[index,change_value] = 6

    return df

# def data_clean_change_value(df:pd.DataFrame, change_value:str) -> object:
#     df[change_value] = df[change_value].replace('A',10)
#     df[change_value] = df[change_value].replace('B',8)
#     df[change_value] = df[change_value].replace('C',6)






def data_clean_rename_col(data_frame:object,old_name: str,new_name: str) -> object:
    data_frame = data_frame.rename(columns={old_name:new_name})
    return data_frame





def data_clean_fillna(data_frame:object,col_name,value) -> object:
    data_frame = data_frame.fillna({col_name:value})
    return data_frame





def group_by_mean(data_frame:object,col_name:str,value:str) -> list:
    data_frame = data_frame.groupby(col_name)[value].mean().reset_index()
    data_frame = data_frame[data_frame[value] > 80 ]
    return list(data_frame[col_name])



def add_Bonus_Score(data_frame:object,value_column:list,name_column:str = 'Bonus Score') -> object:
    data_frame[name_column] = [1 if x in value_column else 0 for x in data_frame['Group']]
    return data_frame





# ------------------------------------- data frame ------------------------------------------------
df_student_Quiz_2 = data_clean_change_value(df_student_Quiz_2,'Quiz2_Grade')
df_student_Quiz_2= data_clean_rename_col(df_student_Quiz_2,'Quiz2_Grade','Quiz2_Score')
df_student_Quiz_2 = data_clean_fillna(df_student_Quiz_2,'Quiz2_Score',0)
df_student_Quiz_1 = data_clean_fillna(df_student_Quiz_1,'Quiz1_Score',0)
df_student_Project_grouped = group_by_mean(df_student_Project,'Group','Project_Score')
df_student_Project_Bonus_Score = add_Bonus_Score(df_student_Project,df_student_Project_grouped)
df_merge_quiz = pd.merge(df_student_Quiz_1,df_student_Quiz_2)
df_merge_quiz['Quiz_Score'] = df_merge_quiz[['Quiz1_Score','Quiz2_Score']].sum(axis=1)
df_merge_quiz = df_merge_quiz.drop(columns=['Quiz1_Score','Quiz2_Score'])
df_all = [df_merge_quiz,df_student_Project_Bonus_Score,df_student_Information,df_student_Final_Exam]
df_main = reduce(lambda df_1,df_2 : pd.merge(df_1,df_2),df_all)

df_calculate_final_exam = df_student_Final_Exam
df_calculate_final_exam = df_calculate_final_exam.drop('FinalExam_Score',axis=1)
df_calculate_final_exam['Quiz_Score'] = df_merge_quiz[['Quiz_Score']] * 0.25
df_calculate_final_exam['Project_Score'] = df_student_Project[['Project_Score']] * 0.1
df_calculate_final_exam['Final_Exam_Score'] = df_student_Final_Exam[['FinalExam_Score']] * 0.25
df_calculate_final_exam['Bonus Score'] = df_student_Project_Bonus_Score[['Bonus Score']]
df_calculate_final_exam['Sum'] = df_calculate_final_exam[['Quiz_Score','Project_Score','Final_Exam_Score','Bonus Score']].sum(axis=1)
for index in df_calculate_final_exam.index:
    if df_calculate_final_exam.loc[index,'Sum'] > 20:
        df_calculate_final_exam.loc[index,'Sum'] = 20

    if 18 < df_calculate_final_exam.loc[index,'Sum'] and df_calculate_final_exam.loc[index,'Sum'] <=20:
        df_calculate_final_exam.loc[index,'Grade'] = 'A'
    elif 16 < df_calculate_final_exam.loc[index,'Sum'] and df_calculate_final_exam.loc[index,'Sum'] <=18:
        df_calculate_final_exam.loc[index,'Grade'] = 'B'
    elif 14 < df_calculate_final_exam.loc[index,'Sum'] and df_calculate_final_exam.loc[index,'Sum'] <=16:
        df_calculate_final_exam.loc[index,'Grade'] = 'C'
    elif 12 < df_calculate_final_exam.loc[index,'Sum'] and df_calculate_final_exam.loc[index,'Sum'] <=14:
        df_calculate_final_exam.loc[index,'Grade'] = 'D'
    else :
        df_calculate_final_exam.loc[index,'Grade'] = 'E'

plot_grade = df_calculate_final_exam['Grade'].value_counts()
print(plot_grade)
plot_grade.plot.bar()
plt.show()
# ---------------------------------------- print ----------------------------------------------------
# print(df_student_Quiz_1)
# print(df_student_Quiz_2)
# print(df_student_Project_grouped)
# print(df_student_Project_Bonus_Score)
# print(df_merge_quiz)
# print(df_main)
# show all coll we most use to_strin
# print(df_main.to_string())
print(df_calculate_final_exam)
