# pandas: Convert string column to ordered Category?
likert_scale = {'strongly agree':2, 'agree':1, 'neither':0, 'disagree':-1, 'strongly disagree':-2}
df['categorical_data'] = df.EasyToUseQuestion.apply(lambda x: likert_scale[x])
