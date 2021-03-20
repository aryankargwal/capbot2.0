def search_word(df,keywords):
  l = []
  for i in df.index:
    y = df.loc[i, :].values.tolist()
    y = set(y)
    if y.intersection(set(keywords)):
      l.append(i)
  return l