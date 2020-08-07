def finder(files, queries):
  queries_dict = dict.fromkeys(queries, 1)
  results = []
  for file in files:
    if file.split('/')[-1] in queries_dict:
      results.append(file)
  return results

if __name__ == "__main__":
  files = ['/bin/foo', '/bin/bar', '/usr/bin/baz']
  queries = ["foo", "qux", "baz"]
  print(finder(files, queries))
