import pandas as pd
import matplotlib.pyplot as plt

def read_ssv(filename):
    return pd.read_csv(filename, delim_whitespace=True, header=1, index_col=False)

name = '../reports/findTopRandomMarking66'
def read():
    with open(name) as f:
        cur_line = f.readline()
        while not cur_line.startswith('Iter 9 started'):
            cur_line = f.readline()
        return pd.read_csv(f, delim_whitespace=True, header=None, index_col=False)

df = read()
df.dropna(inplace=True)
del df[0]
del df[1]
df.drop(df.index[df[3] == 'cont'], inplace=True)
df.columns = ['filename', 'snr']
df = pd.concat([df['filename'].str.extract('b5_10_\d{4}_(?P<test>\d*)', expand=True),
           df['snr']], axis=1)
df = df.set_index('test')
pd.options.display.max_colwidth = 100
print df.sort_values(by='snr')
