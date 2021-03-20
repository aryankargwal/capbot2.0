def search_word(df, keywords):
    for i in df.index:
        y = df.loc[i, :].values.tolist()
        y = set(y)
        if y.intersection(set(keywords)):
            # return df.iloc[i - 1]["time"], df.iloc[i - 1]["camera"]
            return i
