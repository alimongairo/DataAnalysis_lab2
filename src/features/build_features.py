def feautre_build(df):
    for i in range(df.shape[0]):
        if df['GarageCars'][i] > 1:
            df['FamilySize'] = 1
        else:
            df['FamilySize'] = 0
    return df