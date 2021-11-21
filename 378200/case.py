#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance.csv')

print(df.head)

course_math = df[df['test preparation course']=='completed']['math score'].mean()
none_course_math = df[df['test preparation course']=='none']['math score'].mean()
course_reading = df[df['test preparation course']=='completed']['reading score'].mean()
none_course_reading = df[df['test preparation course']=='none']['reading score'].mean()
course_writing =  df[df['test preparation course']=='completed']['writing score'].mean()
none_course_writing = df[df['test preparation course']=='none']['writing score'].mean()
mean_1 = (course_math + course_reading + course_writing) / 3
mean_2 = (none_course_math + none_course_reading + none_course_writing) / 3


print('Результаты математики людей посещающих курсы:', course_math)
print('Результаты математики людей не посещающих курсы:', none_course_math)
print('Результаты чтения людей посещающих курсы:', course_reading)
print('Результаты чтения людей не посещающих курсы:', none_course_reading)
print('Результаты писания людей посещающих курсы:', course_writing)
print('Результаты писания людей не посещающих курсы:', none_course_writing)
print('\nРезультат по всем экзаменам людей посещающих курсы:', mean_1)
print('Результат по всем экзаменам людей не посещающих курсы:', mean_2)
print('\nСредний бал выше у посещающих курсы на ', mean_1 - mean_2)

df['test preparation course'].value_counts().plot(kind='pie')

plt.show()

print(df.head)